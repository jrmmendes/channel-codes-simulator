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


class BinVecBasedImage(GenericImage):
    """Representação de imagens por vetores binários"""

    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.__binVector__ = np.zeros(24*rows*cols, 'int8')
