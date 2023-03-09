import os
from pathlib import Path
from typing import Type

import onnxruntime as ort

from .session_base import BaseSession
# from .session_cloth import ClothSession
from .session_simple import SimpleSession


def new_session(model_name: str = "u2net") -> BaseSession:
    session_class: Type[BaseSession]
    # md5 = "60024c5c889badc19c04ad937298a77b"
    # url = "https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx"
    session_class = SimpleSession

    if model_name != "u2net":
        raise NotImplementedError

    u2net_home = os.getenv("U2NET_HOME") or Path(__file__).parent

    fname = f"{model_name}.onnx"
    path = Path(u2net_home).expanduser()
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
