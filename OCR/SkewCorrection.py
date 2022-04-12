'''
Image Pre-Processing
- Skew Correction
-> Projection profile method

참고
https://towardsdatascience.com/pre-processing-in-ocr-fc231c6035a7
https://sachithppp.medium.com/projection-histogram-of-binary-image-e4e9eabb7c9d
'''

import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
from scipy.ndimage import interpolation as inter

# 이미지 경로
input_image = r'PATH'

image = im.open(input_image)

# convert to binary
width, height = image.size
pixel = np.array(image.convert('1').getdata(), np.uint8)
binary_image = 1 - (pixel.reshape((height, width)) / 255.0)


def find_score(array, angle):
    data = inter.rotate(array, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:]-hist[:-1]) ** 2)
    return hist, score


delta = 1
limit = 5
angles = np.arange(-limit, limit+delta, delta)
scores = []
for angle in angles:
    hist, score = find_score(binary_image, angle)
    scores.append(score)

best_score = max(scores)
best_angle = angles[scores.index(best_score)]

# correct skew
data = inter.rotate(binary_image, best_angle, reshape=False, order=0)
image = im.fromarray((255*data).astype("uint8")).convert("RGB")

# 저장 경로
image.save(r'PATH/skew_corrected.png')