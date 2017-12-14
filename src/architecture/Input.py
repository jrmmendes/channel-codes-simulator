import numpy as np
import scipy.ndimage.io as imageio
import src.architecture.Images as Images
from scipy import misc


def importImage(file):
    im = imageio.imread(file)

    rows = im.shape[0]
    cols = im.shape[1]

    image = Images.MatrixBasedImage(rows, cols)

    for i in range(rows):
        for j in range(cols):
            color = im[i, j]
            image.setColor(i, j, color[0], color[1], color[2])

    return image


def exportImage(file, image):
    rgb = np.zeros((image.getRows(), image.getCols(), 3), dtype=np.uint8)
    rgb[..., 0] = image.getRedMatrix()
    rgb[..., 1] = image.getGreenMatrix()
    rgb[..., 2] = image.getBlueMatrix()

    misc.imsave(file, rgb)
