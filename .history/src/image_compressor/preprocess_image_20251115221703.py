import os
import math
from PIL import Image
from abc import abstractmethod, ABC

class ReadAndSaveFile(ABC):
    @abstractmethod
    def input_file(self):
        pass

    @abstractmethod
    def output_file():
        pass

class PreprocessImage(ReadAndSaveFile):
    def __init__(self):
        self.image = None
        self.file_name = None

    def convert_grayscale(self):
        pass
    

    def input_file(self, input_path):
        self.image = Image.open(input_path)
        self.file_name = os.path.splitext(os.path.basename(input_path))[0]
        print(self.image.format, self.image.size, self.image.mode)

    def output_file(self, output_path):
        output_folder = os.path.join(output_path, self.file_name)
        os.makedirs(output_folder, exist_ok=True)

        result = self.convert_grayscale()
        save_path = os.path.join(output_folder, "convert_gray.jpg")
        result.save(save_path)