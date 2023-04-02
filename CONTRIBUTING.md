# Contributing

> **Note**: please keep in mind, this project repo is an *unofficial* fork
> of [`danielgatis/rembg`].

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

[`danielgatis/rembg`]: https://github.com/danielgatis/rembg

## Types of Contributions

### Report Bugs

Report bugs at <https://github.com/rnag/rembg-aws-lambda/issues>.

If  this is a general `rembg` issue, report it
on [`danielgatis/rembg`] instead.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to
implement it.

### Write Documentation

`rembg-aws-lambda` could always use more documentation, whether as part of the
official docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/rnag/rembg-aws-lambda/issues>.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up [rembg-aws-lambda](#contributing) for
local development.

1.  Fork the [rembg-aws-lambda](#contributing) repo on GitHub.

2.  Clone your fork locally:

    ```shell
    $ git clone git@github.com:your_name_here/rembg-aws-lambda.git
    ```
    #### Workaround for LFS Bandwidth
    > **_NOTE_**: If you run into issues with `git-lfs` when downloading the `*.onnx`
    model file(s), or if you've reached your LFS data quota, try the
    following steps instead.

    ```shell
    # clone/pull the repo without LFS - https://stackoverflow.com/a/42021818/10237506
    $ GIT_LFS_SKIP_SMUDGE=1 git@github.com:your_name_here/rembg-aws-lambda.git
    # use curl to manually download the model (*.onnx) file
    $ curl https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx \
        -o rembg-aws-lambda/rembg/u2net.onnx
    # fix permissions
    $ chmod 777 rembg-aws-lambda/rembg/*.onnx
    ```

3. Install your local copy into a virtualenv. Assuming you have
    virtualenvwrapper installed, this is how you set up your fork for
    local development:

    ``` shell
    $ mkvirtualenv rembg-aws-lambda
    $ cd rembg-aws-lambda/
    $ pip install -r requirements.txt -r requirements-dev.txt
    ```

4.  Create a branch for local development:

    ``` shell
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

5.  When you're done making changes, check that your changes pass
    the tests, including testing other Python versions with
    tox:

    ``` shell
    $ pytest
    ```

6.  Commit your changes and push your branch to GitHub:

    ``` shell
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

7.  Submit a pull request through the GitHub website.

# Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.rst.
3.  The pull request should work for Python 3.8, 3.9 and 3.10, and
    for PyPy. Check the following workflows, and make
    sure that they pass for all supported Python versions.

    - [Lint](https://github.com/rnag/rembg-aws-lambda/actions/workflows/lint_python.yml)
    - [Test in specific environment](https://github.com/rnag/rembg-aws-lambda/actions/workflows/test-specific-environment.yml)
    - [Test installation](https://github.com/rnag/rembg-aws-lambda/actions/workflows/test-install.yml)

## Tips

To run a subset of tests:

``` shell
$ pytest tests/unit/test_rembg-aws-lambda.py::test_my_func
```

## Deploying

---
**NOTE**

**Tip:** The last command below is used to push both the commit and the
new tag to the remote branch simultaneously. There is also a simpler
alternative as mentioned in [this
post](https://stackoverflow.com/questions/3745135/push-git-commits-tags-simultaneously),
which involves running the following command:

``` shell
$ git config --global push.followTags true
```

After that, you should be able to simply run the below command to push
*both the commits and tags* simultaneously:

``` shell
$ git push
```
---

A reminder for the maintainers on how to deploy. Make sure all your
changes are committed (including an entry in HISTORY.rst). Then run:

``` shell
$ bump2version patch # possible: major / minor / patch
$ git push && git push --tags
```

GitHub Actions will then [deploy to
PyPI](https://github.com/rnag/rembg-aws-lambda/actions/workflows/publish_pypi.yml) if
tests pass.
