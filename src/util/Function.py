import random as rd

from src.architecture.Images import BinVecBasedImage


def bin2dec(binary_str):
    """Função para converter valor binário em decimal"""
    binary_str = str(binary_str)
    binary_str = binary_str[::-1]
    n = len(binary_str)
    decimal_str = 0
    for i in range(n):
        if binary_str[i] == "1":
            decimal_str += 2**int(i)

    return int(decimal_str)


def dec2bin(decimal):
    """Função para converter de decimal para binário"""
    binary_str = ""
    while True:
        binary_str = binary_str + str(decimal % 2)
        decimal = decimal // 2
        if decimal == 0:
            break
    binary_str = binary_str[::-1]
    return int(binary_str)


def noise(p, size):
    """Função que gera um ruido"""
    e = BinVecBasedImage(size)

    for i in range(e.getLength()):
        e.setBitValue(i, bit(p))

    return e


def bit(p):
    """Função para obter um bit com probabilidade 1E-10 < p <= 1"""
    if p < 1E-5 or p > 1:
        raise OverflowError("The value of p is out of bounds")

    if rd.randrange(1E10) <= p * 1E10:
        return 1
    else:
        return 0


def apply_noise(img, e):
    length = img.getLength()

    for i in range(length):
        b = img.getBitValue(i) ^ e.getBitValue(i)
        img.setBitValue(i, b)
