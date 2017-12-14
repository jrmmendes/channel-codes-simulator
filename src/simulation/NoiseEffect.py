from src.architecture.ImageConverter import BinVec2RGBMatrix, RGBMatrix2BinVec
from src.architecture.Input import importImage, exportImage
from src.util import Function as Function


def simulateNoiseEffect(p, input_file, output_file):
    image = importImage(input_file)
    bin_image = RGBMatrix2BinVec(image)

    rows = image.getRows()
    cols = image.getCols()

    e = Function.noise(p, 24 * rows * cols)
    e.setRows(rows)
    e.setCols(cols)

    Function.apply_noise(bin_image, e)

    result = BinVec2RGBMatrix(bin_image)
    exportImage(output_file, result)
