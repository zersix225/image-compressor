import os
import numpy as np
from image_compressor import PreprocessImage

if __name__ == "__main__":
    process = PreprocessImage()
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "inputs"))
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "outputs"))

    arrays = []

    for file in os.listdir(input_dir):
        if file.endswith(".jpg"):
            input_path = os.path.join(input_dir, file)
            process.input_file(input_path)

            arr = process.output_file(output_dir)
            arrays.append(arr)
            print(input_path)

    arrays = np.array(arrays)
    
    for row in arrays:
        for item in row:
            print(item, end="")
        print()