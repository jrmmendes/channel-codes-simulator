import numpy as np
import src.misc.exceptions as exception

class MatrixBasedImage:
    """Representação de imagens por matrizes RGB"""

    def __init__(self, rows, collumns):
        if rows <= 0:
            raise exception.SizeError("rows")

        if collumns <= 0:
            raise exception.SizeError("collumns")

        self.__rows__ = rows
        self.__collumns__ = collumns

        """Red = 0, Green = 1, Blue = 2"""
        self.__colors__ = np.zeros((rows, collumns), 3)

