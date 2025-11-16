import os
from PIL import Image, ImageOps
from abc import abstractmethod, ABC

class ReadAndSaveFile(ABC):
    @abstractmethod
    def input_file():
        pass

class PreprocessImage(ReadAndSaveFile):
    def __init__(self):
        self.image = None
        self.file_name = None

    def convert_grayscale(self):
        img_convert = ImageOps.grayscale(self.image)
        return img_convert
    
    def input_file(self, input_path):
        self.image = Image.open(input_path)
        self.file_name = os.path.splitext(os.path.basename(input_path))[0]
        
        print(self.image.format, self.image.size, self.image.mode)