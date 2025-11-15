import os
import numpy as np
from image_compressor import PreprocessImage

if __name__ == "__main__":
    process = PreprocessImage()
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "inputs"))

    for file in os.listdir(input_dir):
        process.input_file(os.path.join(input_dir, file))
        process.convert_grayscale()