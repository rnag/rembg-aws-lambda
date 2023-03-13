# Rembg (AWS Lambda)

[![Downloads](https://pepy.tech/badge/rembg-aws-lambda)](https://pepy.tech/project/rembg-aws-lambda)
[![Downloads](https://pepy.tech/badge/rembg-aws-lambda/month)](https://pepy.tech/project/rembg-aws-lambda)
[![Downloads](https://pepy.tech/badge/rembg-aws-lambda/week)](https://pepy.tech/project/rembg-aws-lambda)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://img.shields.io/badge/License-MIT-blue.svg)
[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/KenjieDec/RemBG)
[![Streamlit App](https://img.shields.io/badge/🎈%20Streamlit%20Community-Cloud-blue)](https://bgremoval.streamlit.app/)


> This is a *stripped-down* fork of [`danielgatis/rembg`](https://github.com/danielgatis/rembg)
> designed for [AWS Lambda](https://aws.amazon.com/lambda/) environments.

[`rembg-aws-lambda`](https://pypi.org/project/rembg-aws-lambda/) is a tool to remove images background.

<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/car-1.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/car-1.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/car-2.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/car-2.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/car-3.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/car-3.out.png" width="100" />
</p>

<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/animal-1.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/animal-1.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/animal-2.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/animal-2.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/animal-3.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/animal-3.out.png" width="100" />
</p>

<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/girl-1.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/girl-1.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/girl-2.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/girl-2.out.png" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/girl-3.jpg" width="100" />
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/examples/girl-3.out.png" width="100" />
</p>

[//]: # (**If this project has helped you, please consider making a [donation]&#40;https://www.buymeacoffee.com/danielgatis&#41;.**)

## Requirements

```
python: >3.7, <3.11
```

## Installation

CPU support:

```bash
pip install rembg-aws-lambda
```

GPU support:

First of all, you need to check if your system supports the `onnxruntime-gpu`.

Go to https://onnxruntime.ai and check the installation matrix.

<p style="display: flex;align-items: center;justify-content: center;">
  <img src="https://raw.githubusercontent.com/rnag/rembg-aws-lambda/master/onnxruntime-installation-matrix.png" width="400" />
</p>

If yes, just run:

```bash
pip install rembg-aws-lambda[gpu]
```

## Usage as a library

Input and output as bytes

```python
from rembg import remove

input_path = 'input.png'
output_path = 'output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
```

Input and output as a PIL image

```python
from rembg import remove
from PIL import Image

input_path = 'input.png'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
```

Input and output as a numpy array

```python
from rembg import remove
import cv2

input_path = 'input.png'
output_path = 'output.png'

input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)
```

How to iterate over files in a performatic way

```python
from pathlib import Path
from rembg import remove, new_session

session = new_session()

for file in Path('path/to/folder').glob('*.png'):
    input_path = str(file)
    output_path = str(file.parent / (file.stem + ".out.png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session)
            o.write(output)
```

## Models

All models are downloaded and saved in the user home folder in the `.u2net` directory.

The available models are:

-   u2net ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx), [source](https://github.com/xuebinqin/U-2-Net)): A pre-trained model for general use cases.
-   u2netp ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx), [source](https://github.com/xuebinqin/U-2-Net)): A lightweight version of u2net model.
-   u2net_human_seg ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_human_seg.onnx), [source](https://github.com/xuebinqin/U-2-Net)): A pre-trained model for human segmentation.
-   u2net_cloth_seg ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_cloth_seg.onnx), [source](https://github.com/levindabhi/cloth-segmentation)): A pre-trained model for Cloths Parsing from human portrait. Here clothes are parsed into 3 category: Upper body, Lower body and Full body.
-   silueta ([download](https://github.com/danielgatis/rembg/releases/download/v0.0.0/silueta.onnx), [source](https://github.com/xuebinqin/U-2-Net/issues/295)): Same as u2net but the size is reduced to 43Mb.

### How to train your own model

If You need more fine tunned models try this:
https://github.com/danielgatis/rembg/issues/193#issuecomment-1055534289


## Some video tutorials

- https://www.youtube.com/watch?v=3xqwpXjxyMQ
- https://www.youtube.com/watch?v=dFKRGXdkGJU
- https://www.youtube.com/watch?v=Ai-BS_T7yjE
- https://www.youtube.com/watch?v=dFKRGXdkGJU
- https://www.youtube.com/watch?v=D7W-C0urVcQ

## References

- https://arxiv.org/pdf/2005.09007.pdf
- https://github.com/NathanUA/U-2-Net
- https://github.com/pymatting/pymatting

## Buy me a coffee

Liked some of my work? Buy me a coffee (or more likely a beer)

<a href="https://www.buymeacoffee.com/ritviknag" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;"></a>

## License

Copyright:
  * (c) 2020-present  [Daniel Gatis](https://github.com/danielgatis)
  * (c) 2023-present  [Ritvik Nag](https://github.com/rnag)

Licensed under [MIT License](./LICENSE.txt)
