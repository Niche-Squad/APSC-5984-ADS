ls_x = [2, 3, 4, 6, "abc", "def"]

ls_x[4]  # fifth element: abc


ls_x[1:5]
ls_x[1:-1]
# index: 1:5 -> 1, 2, 3, 4
# target: 3, 4, 6, "abc"

# numpy
import numpy as np

np.__version__


np_x = np.arange(1, 11)
np_x[3:6]  # 4, 5, 6
np_x[:4]

np_x = np.arange(1, 29)

# ".": pipe the result to the next command (function)
mat_x = np_x.reshape(4, 7)
mat_x
# [[3, 10, 17, 24], [6, 13, 20, 27]]
mat_x[:, [2, 5]]
mat_x[:, 2::3]

# statistics
mat_x.mean()
mat_x.std()
mat_x.max()
mat_x.min()

# summarize the average of every column (axis=1)
# compressing the information from the rows (axis=0)
mat_x.mean(axis=0)

# compressing (summarizing) the info from columns (axis=1)
mat_x.mean(axis=1)
