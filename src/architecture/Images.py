import numpy as np
import src.misc.exceptions as exception
from abc import ABC


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
        self.__red__ = np.zeros((rows, cols), 'int32')
        self.__green__ = np.zeros((rows, cols), 'int32')
        self.__blue__ = np.zeros((rows, cols), 'int32')
        self.__colors__ = (self.__red__, self.__green__, self.__blue__)

    def getRedMatrix(self):
        return self.__colors__[0]

    def getGreenMatrix(self):
        return self.__colors__[1]

    def getBlueMatrix(self):
        return self.__colors__[2]

    def getColor(self, x, y):
        if x < 0 or x >= self.getRows():
            raise exception.SizeError("x")
        if y < 0 or y >= self.getRows():
            raise exception.SizeError("y")

        return self.getRedMatrix()[x, y], self.getGreenMatrix()[x, y], self.getBlueMatrix()[x, y]

    def setColor(self, x, y, red, green, blue):
        if x < 0 or x >= self.getRows():
            raise exception.SizeError("x")

        if y < 0 or y >= self.getRows():
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

    def getBitValue(self, bit):
        if bit >= self.getLength():
            raise exception.SizeError("bit position")

        return self.__binVector__[bit]

    def setBitValue(self, bit, value):

        if bit >= self.getLength():
            raise exception.SizeError("bit position")

        if not (value == 1 or value == 0):
            raise AttributeError("The informed value in setBitValue function is not a binary value")

        self.__binVector__[bit] = value

    def getLength(self):
        return self.getRows()*self.getCols()*24


class ImageConverter(ABC):
    """Converte a representação da imagem"""

    @staticmethod


    def RGBMatrix2BinVec(rgb_matrix):

        bin_vec = BinVecBasedImage(rgb_matrix.getRows(), rgb_matrix.getCols())

        n = 0

        for i in range(rgb_matrix.getRows()):
            for j in range(rgb_matrix.getCols()):
                pixel = rgb_matrix.getColor(j, i)

                red = str(dec2bin(pixel[0]))
                green = str(dec2bin(pixel[1]))
                blue = str(dec2bin(pixel[2]))

                while len(red) < 8:
                    red = "0"+red

                while len(green) < 8:
                    green = "0"+green

                while len(blue) < 8:
                    blue = "0"+blue

                color = red + green + blue

                for t in range(len(color)):
                    bin_vec.setBitValue(n, int(color[t]))
                    n += 1

        return bin_vec

    @staticmethod
    def BinVec2RGBMatrix(bin_vec):
        if not bin_vec.type(BinVecBasedImage):
            raise exception.ImageTypeError("is not a BinVec")


def bin2dec(number):
    """Função para converter valor binário em decimal"""
    binary = str(number)
    binary = binary[::-1]
    n = len(binary)
    decimal = 0
    for i in range(n):
        if binary[i] == "1":
            decimal += 2**int(i)

    return int(decimal)


def dec2bin(number):
    """Função para converter de decimal para binário"""
    binary = ""
    while True:
        binary = binary + str(number % 2)
        number = number // 2
        if number == 0:
            break
    binary = binary[::-1]
    return int(binary)
