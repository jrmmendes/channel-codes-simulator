import numpy as np


class Parameters:
    __matriz_geradora__ = np.array(
        [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]], dtype=np.int32)

    __matriz_paridade__ = np.array(
        [[1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
         [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
         [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
         [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]], dtype=np.int32)

    __matriz_ver_paridade__ = np.array(
        [[1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
         [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0],
         [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0],
         [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1]], dtype=np.int32)

    def getMatrizGeradora(self):
        return self.__matriz_geradora__

    def getMatrizParidade(self):
        return self.__matriz_paridade__

    def getMatrizVerParidade(self):
        return self.__matriz_ver_paridade__

    def __init__(self):
        pass
