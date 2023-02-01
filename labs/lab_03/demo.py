# list (indexing, slicing)
ls_x = [2, 3, 4, 6, "abc", "def"]
ls_x[4]  # fifth element: "abc"
ls_x[1:5]
ls_x[1:-1]  # equivalent to ls_x[1:5]
# index: 1:5 -> 1, 2, 3, 4
# target: 3, 4, 6, "abc"

# numpy
from os import listxattr
import numpy as np

np.__version__

# 1d example
np_x = np.arange(1, 11)
np_x[3:6]  # 4, 5, 6
np_x[:4]

# 2d example
np_x = np.arange(1, 29)
# ".": pipe the result to the next command (function)
mat_x = np_x.reshape(4, 7)  # equivalent to np.reshape(np_x, (4, 7))
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

# 3d example -----------------------

# 3 x 5 x 4 :60
import numpy as np

mat_3d = np.arange(60).reshape((3, 5, 4))
# when axis=0,
# outcome should have a dimension of the remaining dimensions, which is (5, 4)
sum_3d_axis0 = mat_3d.sum(axis=0)
mat_3d
sum_3d_axis0
mat_3d.std(axis=0)

# dictionary -----------------------
dict_demo = {"Apple": "red", "Banana": "yellow"}

ls_keys = dict_demo.keys()
ls_keys = list(ls_keys)
ls_keys[0]

dict_demo = {"John": 20, "Mary": 25, "Michael": 30, "Elizabeth": 35, "David": 40}

# list all the keys (or values) and use negative index to fetch the key (or value)
lk = list(dict_demo.keys())[-1]
lv = list(dict_demo.values())[-1]
print(lk, lv)

# for-loop
ls_numbers = np.arange(1, 15, 2)

for num in ls_numbers:
    print(num)

# what if we only want to print out the first five elements?
# key argument is 5
for num in ls_numbers:
    if num > 9:
        break
    print(num)

counter = 0
for num in ls_numbers:
    if counter >= 5:  # num = 0, 1, 2, 3, 4
        break
    print(num)
    # counter = counter + 1
    counter += 1

# turn the example above to a while-loop statement
counter = 0
while counter < 5:
    print(ls_numbers[counter])
    counter += 1
