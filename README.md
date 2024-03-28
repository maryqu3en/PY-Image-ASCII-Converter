# Image to ASCII Converter

This is a simple Python script that converts an image into ASCII art.

## Requirements

- Python 3
- Pillow library

## Installation

1. Clone this repository.
2. Install the **Pillow** library using pip:

```bash
pip install pillow
```

## Usage

1.  Open main.py in any editor.
2.  Set the image variable to the path of the image you want to convert.
3.  Set the type variable to the type of the image (e.g., "png", "jpg").
4.  Set the saveas variable to the path where you want to save the ASCII art (txt file).
5.  Set the scale variable to the scale factor for the ASCII art. A higher number will result in smaller output.
6.  Run main.py:

    ```bash
    python main.py
    ```

The ASCII art will be saved to the file specified in the `saveas` variable.

## Example

Here's an example of how to convert an image named "example.png" into ASCII art and save it as "example.txt":

```python
image = "example.png"
type = "png"
saveas = "example.txt"
scale = 8
asciiConvert(image, type, saveas, scale)
```

Then run `main.py`:

```bash
python main.py
```

***Note:*** *The script may take some time to convert the image, depending on the size and complexity of the image.***
