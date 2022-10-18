import cv2
import numpy as np
from matplotlib import pyplot as plt

def remove_bg(src):
    image_bgr = cv2.imread(src)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    rectangle = (0, 0, 400, 400)
    mask = np.zeros(image_rgb.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    cv2.grabCut(image_rgb, mask, rectangle, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask_2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    image_rgd_nobg = image_rgb * mask_2[:, :, np.newaxis]

    plt.imshow(image_rgd_nobg), plt.axis('off')
    plt.show()

img_src = r'c:/Users/BiggerBob/Desktop/links/Code/Python/xdworld/static/inputs/boldans_reper.png'

# remove_bg(img_src)