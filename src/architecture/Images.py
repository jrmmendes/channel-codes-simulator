import numpy as np
import src.misc.exceptions as exception
from abc import ABC, ABCMeta


class GenericImage(ABC):
    """Classe genérica que serve de base para as outras e possui os métodos de tratamento"""

    def __init__(self, rows, cols):
        if rows <= 0:
            raise exception.SizeError("rows")

        if cols <= 0:
            raise exception.SizeError("cols")

        self.__rows__ = rows
        self.__cols__ = cols

    def getRows(self):
        return self.__rows__

    def getCols(self):
        return self.__cols__


class MatrixBasedImage(GenericImage):
    """Representação de imagens por matrizes RGB"""

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.__red__ = np.zeros((rows, cols), 'int8')
        self.__green__ = np.zeros((rows, cols), 'int8')
        self.__blue__ = np.zeros((rows, cols), 'int8')
        self.__colors__ = (self.__red__, self.__green__, self.__blue__)

    def getRedMatrix(self):
        return self.__colors__[0]

    def getGreenMatrix(self):
        return self.__colors__[1]

    def getBlueMatrix(self):
        return self.__colors__[2]

    def getColor(self, x, y):
        if x <= 0 or x > self.getRows():
            raise exception.SizeError("x")
        if y <= 0 or y > self.getRows():
            raise exception.SizeError("y")

        return self.getRedMatrix()[x, y], self.getGreenMatrix()[x, y], self.getBlueMatrix()[x, y]

    def setColor(self, x, y, red, green, blue):
        if x <= 0 or x > self.getRows():
            raise exception.SizeError("x")

        if y <= 0 or y > self.getRows():
            raise exception.SizeError("y")

        if red < 0 or red > 255:
            raise exception.ColorError("red")

        if green < 0 or green > 255:
            raise exception.ColorError("green")

        if blue < 0 or blue > 255:
            raise exception.ColorError("blue")

        self.getRedMatrix()[x, y] = red
        self.getGreenMatrix()[x, y] = green
        self.getBlueMatrix()[x, y] = blue


class BinVecBasedImage(GenericImage):
    """Representação de imagens por vetores binários"""

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.__binVector__ = np.zeros(24 * rows * cols, 'int8')


class ImageConverter(ABC):
    """Converte a representação da imagem"""

    @staticmethod
    def RGBMatrix2BinVec(rgb_matrix):
        if not rgb_matrix.type(MatrixBasedImage):
            raise exception.ImageTypeError("is not a RGBMatrix")

        for i in range(rgb_matrix.getRows()):
            for j in range(rgb_matrix.getCols()):
                pass


    @staticmethod
    def BinVec2RGBMatrix(bin_vec):
        if not bin_vec.type(BinVecBasedImage):
            raise exception.ImageTypeError("is not a BinVec")

def __bin2dec__(bin):
    pass

def __dec2bin__(dec):
    pass