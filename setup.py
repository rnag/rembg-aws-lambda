import os
import pathlib
import sys

sys.path.append(os.path.dirname(__file__))
from setuptools import setup

import versioneer

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="rembg-aws-lambda",
    description="Remove image background",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rnag/rembg-aws-lambda",
    author="Daniel Gatis",
    author_email="danielgatis@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="remove, background, u2net",
    packages=["rembg"],
    package_data={'': ['*.onnx']},
    include_package_data=True,
    python_requires=">3.7, <3.11",
    install_requires=[
        "numpy~=1.23.5",
        "onnxruntime~=1.13.1",
        "opencv-python-headless~=4.6.0.66",
        "pillow~=9.3.0",
    ],
    extras_require={
        "gpu": ["onnxruntime-gpu~=1.13.1"],
    },
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
