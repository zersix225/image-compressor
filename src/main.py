import os
import numpy as np
from image_compressor import PreprocessImage
from image_compressor import CompressImage

if __name__ == "__main__":
    process = PreprocessImage()
    compress = CompressImage()

    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "inputs"))

    for file in os.listdir(input_dir):
        process.input_file(os.path.join(input_dir, file))
        gray_image = process.convert_grayscale()

        compress.set_image(gray_image)
        compress.rank_image()