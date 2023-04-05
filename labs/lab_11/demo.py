from PIL import Image  # import the submodule Image from PIL
import numpy as np

FILENAME = "cow.jpg"

# open an image filestream
filestream = Image.open(FILENAME)

# convert the filestream to a numpy array
img_array = np.array(filestream)

# check the dimension
img_array.shape

# remember to close the file stream
filestream.close()

# visualization
import matplotlib.pyplot as plt

plt.imshow(img_array)

# crop the image
# we want all RGB channels,
# so we put : in the third dimension
plt.imshow(img_array[500:830, 1800:, :])

# lecture 11.2

import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

img = np.zeros((10, 10))
img[5:8, 5:8] = 1
plt.imshow(img)

# kernel 1
kernel = np.array([[7, 1, 7], [1, -32, 1], [7, 1, 7]])
output = convolve2d(img, kernel, mode="same")
plt.imshow(output)

# kernel 2
kernel = np.array([[-7, -1, -7], [1, -2, 1], [7, 1, 7]])
output = convolve2d(img, kernel, mode="same")
plt.imshow(output)
