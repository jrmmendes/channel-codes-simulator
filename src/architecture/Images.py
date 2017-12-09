import numpy as np
import src.misc.exceptions as exception

class MatrixBasedImage:
    """Representação de imagens por matrizes RGB"""

    def __init__(self, rows, col):
        if rows <= 0:
            raise exception.SizeError("rows")

        if col <= 0:
            raise exception.SizeError("collumns")

        self.__rows__ = rows
        self.__col__ = col
        self.__red__ = np.zeros((rows, col), 'int8')
        self.__green__ = np.zeros((rows, col), 'int8')
        self.__blue__ = np.zeros((rows, col), 'int8')
        self.__colors__ = (self.__red__, self.__green__, self.__blue__)

    def getRedMatrix(self):
        return self.__colors__[0]

    def getGreenMatrix(self):
        return self.__colors__[1]

    def getBlueMatrix(self):
        return self.__colors__[2]
