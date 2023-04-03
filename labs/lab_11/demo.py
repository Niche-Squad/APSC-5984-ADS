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

#
