"""
Python Automation Script, designed to sync changes from:
    upstream (https://github.com/danielgatis/rembg)
to
    our "non-official" fork (https://github.com/rnag/rembg-aws-lambda)

Returns 0 (SUCCESS) if changes are detected, else returns 1.

---

**NOTE**: Pass ``-d | --debug`` to the script, to see the full output.

---

"""
from __future__ import annotations

import os.path
import shutil
from argparse import ArgumentParser
from logging import getLogger, DEBUG, basicConfig, INFO

from os import chdir, listdir, rmdir, unlink, pardir, getcwd, curdir
from os.path import isfile, islink
from pathlib import Path
from shlex import split
from string import ascii_letters
from subprocess import check_output, STDOUT, CalledProcessError


LOG = getLogger()
basicConfig(level=DEBUG, format='[%(levelname)s] %(message)s')

module = Path('rembg')
root_dir = Path(__file__).parent.parent
upstream_dir = Path('rembg-upstream')


def main():
    args = get_parsed_args()
    LOG.setLevel(DEBUG if args.debug else INFO)

    path_to_root = os.path.relpath(root_dir)

    if path_to_root != curdir:
        chdir_with_info(root_dir)

    shutil.rmtree(upstream_dir, ignore_errors=True)

    # Credits: https://stackoverflow.com/a/54910376/10237506
    run_cmd(f"""
    git clone
        --depth 1
        --filter=blob:none
        --sparse
        https://github.com/danielgatis/rembg
        {upstream_dir}
    """)

    chdir_with_info(upstream_dir)

    delete_all_files_in_cwd()

    run_cmd(f"""
    git
        sparse-checkout
        set
        {module}
    """)

    chdir_with_info(pardir)

    move_child_to_parent(upstream_dir, module)

    files_to_copy = ['session_simple.py', 'session_base.py']

    for file in files_to_copy:
        copy_file(upstream_dir / file, module / file)

    merge_main_module()

    if git_has_folder_changed('rembg'):
        LOG.debug('Changes Detected in rembg/ folder')
        exit(0)
    else:
        LOG.debug('No Changes Detected')
        exit(1)


def get_parsed_args():
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true')

    return parser.parse_args()


def merge_main_module(file='bg.py'):
    src = upstream_dir / file
    dst = module / file

    LOG.debug(f'$ merge {src} {dst}')

    prefixes_to_comment = [
        'from pymatting',
        'from scipy',
        'alpha_matting_',
    ]

    functions_to_comment = [
        'alpha_matting_cutout',
    ]

    lines = []
    in_remove_phase = False
    prev_leading_spaces = 0
    comment_lvl = None

    with open(src) as f:
        for line in f:
            comment_line = False

            line = line.rstrip()
            stripped = line.lstrip()
            leading_spaces = len(line) - len(stripped)
            indent = leading_spaces * ' '

            if in_remove_phase:
                if (leading_spaces == prev_leading_spaces
                        and stripped
                        and stripped[0] in ascii_letters):
                    in_remove_phase = False
                    comment_lvl = None
                else:
                    comment_line = True

            elif any(stripped.startswith(prefix) for prefix in prefixes_to_comment):
                comment_line = True

            elif any(stripped.startswith(f'def {func}(') for func in functions_to_comment):
                comment_line = True
                in_remove_phase = True
                prev_leading_spaces = 0
                comment_lvl = 0

            elif stripped.startswith('elif alpha_matting:'):
                in_remove_phase = True
                prev_leading_spaces = leading_spaces
                next_line_indent = 4
                comment_lvl = prev_leading_spaces + next_line_indent
                lines.append(line)
                lines.append(f'{indent}{" " * next_line_indent}raise NotImplementedError')
                continue

            if comment_line and stripped:
                if comment_lvl is None:
                    lines.append(f'{indent}# {stripped}')
                else:
                    remaining_indent = abs(leading_spaces - comment_lvl)
                    lines.append(f'{" " * comment_lvl}# {" " * remaining_indent}{stripped}')
                continue

            lines.append(line)

    # add a trailing newline
    lines.append('')

    with open(dst, 'w') as f:
        f.write('\n'.join(lines))


def copy_file(src: Path[str] | str, dst: Path[str] | str):
    LOG.debug(f'$ cp {src} {dst}')
    shutil.copyfile(src, dst)


def chdir_with_info(to: Path | str):
    LOG.debug(f'$ cd {to}')
    chdir(to)


# Credits: https://stackoverflow.com/a/8429176/10237506
def move_child_to_parent(root: Path[str], child: Path[str] | str):
    path_to_child = root / child

    for filename in listdir(path_to_child):
        shutil.move(path_to_child / filename, root / filename)

    rmdir(path_to_child)


# Credits: https://stackoverflow.com/a/185941/10237506
def delete_all_files_in_cwd():
    for filename in listdir('.'):
        try:
            if isfile(filename) or islink(filename):
                unlink(filename)
        except Exception as e:
            LOG.error(f'Failed to delete {filename}. Reason: {e}')


def run_cmd(cmd: str, capture_stderr=True) -> str:
    stderr = STDOUT if capture_stderr else None

    cmd_list = split(cmd.strip())
    LOG.debug(f'$ {" ".join(cmd_list)}')

    return check_output(cmd_list, stderr=stderr).decode().strip()


def git_has_folder_changed(folder: str):
    """Use `git` to check if a folder has changes."""
    try:
        run_cmd(f"""
        git diff
            --quiet
            HEAD
            --
            {folder}
        """)
        return False

    except CalledProcessError:
        return True


if __name__ == '__main__':
    main()
