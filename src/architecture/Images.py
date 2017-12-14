import numpy as np
from abc import ABC


class GenericImage(ABC):
    """Classe genérica que serve de base para as outras e possui os métodos de tratamento"""

    def __init__(self, rows, cols):
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
        return self.getRedMatrix()[x, y], self.getGreenMatrix()[x, y], self.getBlueMatrix()[x, y]

    def setColor(self, x, y, red, green, blue):
        self.getRedMatrix()[x, y] = red
        self.getGreenMatrix()[x, y] = green
        self.getBlueMatrix()[x, y] = blue


class BinVecBasedImage(GenericImage):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.__binVector__ = np.zeros(24 * rows * cols, 'int8')

    def getBitValue(self, bit):
        return self.__binVector__[bit]

    def setBitValue(self, bit, value):
        self.__binVector__[bit] = value

    def getLength(self):
        return self.getRows()*self.getCols()*24

    def getBinVec(self):
        return self.__binVector__