import os
import math
import re
from PIL import Image, ImageOps
from abc import abstractmethod, ABC

class ReadAndSaveFile(ABC):
    @abstractmethod
    def input_file():
        pass

    @abstractmethod
    def output_file():
        pass

class PreprocessImage(ReadAndSaveFile):
    def __init__(self):
        self.image = None
        self.file_name = None

    def convert_grayscale(self):
        img_convert = ImageOps.grayscale(self.image)
        dim = max(img_convert.size)  # Find the largest dimension
        new_dim = 2 ** int(math.ceil(math.log(dim, 2)))  # Find the next power of 2
        return ImageOps.pad(img_convert, (new_dim, new_dim))
    
    def input_file(self, input_path):
        self.image = Image.open(input_path)
        self.file_name = os.path.splitext(os.path.basename(input_path))[0]

    def output_file(self, output_path):
        output_folder = os.path.join(output_path, self.file_name)
        os.makedirs(output_folder, exist_ok=True)

        result = self.convert_grayscale()
        save_path = os.path.join(output_folder, "convert_gray.jpg")
        result.save(save_path)