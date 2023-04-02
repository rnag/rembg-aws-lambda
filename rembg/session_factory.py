import os
from pathlib import Path
from typing import Type

import onnxruntime as ort

from .session_base import BaseSession
from .session_simple import SimpleSession

script_dir = Path(__file__).parent


def new_session(model_name: str = "u2net") -> BaseSession:
    session_class: Type[BaseSession]
    # md5 = "60024c5c889badc19c04ad937298a77b"
    # url = "https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx"
    session_class = SimpleSession

    if model_name != "u2net":
        raise NotImplementedError

    if "U2NET_HOME" in os.environ:
        u2net_home = os.environ["U2NET_HOME"]
        path = Path(u2net_home).expanduser()
    else:
        path = script_dir

    fname = f"{model_name}.onnx"
    full_path = path / fname

    sess_opts = ort.SessionOptions()

    if "OMP_NUM_THREADS" in os.environ:
        sess_opts.inter_op_num_threads = int(os.environ["OMP_NUM_THREADS"])

    return session_class(
        model_name,
        ort.InferenceSession(
            str(full_path),
            providers=ort.get_available_providers(),
            sess_options=sess_opts,
        ),
    )
