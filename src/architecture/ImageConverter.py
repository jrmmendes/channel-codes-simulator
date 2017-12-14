from src.architecture.Images import BinVecBasedImage, MatrixBasedImage
import src.util.Function as Function


def RGBMatrix2BinVec(rgb_matrix):
    bin_vec = BinVecBasedImage(rgb_matrix.getRows(), rgb_matrix.getCols())

    n = 0

    for i in range(rgb_matrix.getRows()):
        for j in range(rgb_matrix.getCols()):
            pixel = rgb_matrix.getColor(i, j)

            red = str(Function.dec2bin(pixel[0]))
            green = str(Function.dec2bin(pixel[1]))
            blue = str(Function.dec2bin(pixel[2]))

            while len(red) < 8:
                red = "0" + red

            while len(green) < 8:
                green = "0" + green

            while len(blue) < 8:
                blue = "0" + blue

            color = red + green + blue

            for t in range(len(color)):
                bin_vec.setBitValue(n, int(color[t]))
                n += 1

    return bin_vec


def BinVec2RGBMatrix(bin_vec):
    rgb_image = MatrixBasedImage(bin_vec.getRows(), bin_vec.getCols())

    binary_str = ""
    aux = str(bin_vec.getBinVec())[1:-1].split(" ")

    for i in range(len(aux)):
        binary_str += aux[i]

    n = 0

    red = ""
    green = ""
    blue = ""

    for i in range(bin_vec.getRows()):
        for j in range(bin_vec.getCols()):
            for k in range(8):
                red += binary_str[n]
                n += 1

            for k in range(8):
                green += binary_str[n]
                n += 1

            for k in range(8):
                blue += binary_str[n]
                n += 1

            red = Function.bin2dec(int(red))
            green = Function.bin2dec(int(green))
            blue = Function.bin2dec(int(blue))

            rgb_image.setColor(i, j, red, green, blue)

    return rgb_image


