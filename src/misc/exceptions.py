class Error(Exception):
    """Classe base para as excessões"""
    pass


class SizeError(Error):
    """Erro referente ao tamanho"""

    def __init__(self, param):
        print("SizeError: Invalid size (" + param + ") informed.")


class ColorError(Error):
    """Erro referente à cor informada"""

    def __init__(self, color):
        print("ColorError: Invalid color (" + color + ") informed")


class ImageTypeError(Error):

    def __init__(self, img_type):
        print("ColorError: Invalid type (" + img_type + ") informed")
