class Error(Exception):
    """Classe base para as excessões"""
    pass


class SizeError(Error):
    """Tamanho referente ao erro"""

    def __init__(self, param):
        print("SizeError: Invalid size ("+ param +")informed.")
