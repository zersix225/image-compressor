import os
from image_compressor import PreprocessImage

if __name__ == "__main__":
    input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "inputs"))

    for file in os.listdir(input_dir):
        process = PreprocessImage()
        process.input_file(os.path.join(input_dir, file))

        process.convert_grayscale


    # input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "inputs"))
    # output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "img", "outputs"))

    # for file in os.listdir(input_dir):
    #     if file.endswith(".jpg"):
    #         input_path = os.path.join(input_dir, file)

    #         process.input_file(input_path)
    #         process.output_file(output_dir)