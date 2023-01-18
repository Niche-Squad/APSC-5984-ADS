# partial leaat square method
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
import os
import string
import random
import pandas as pd

X = np.array(
    [[7, 7, 13, 7], [4, 3, 14, 7], [10, 5, 12, 5], [16, 7, 11, 3], [13, 3, 10, 3]]
)

Y = np.array([[14, 7, 8], [10, 7, 6], [8, 5, 5], [2, 4, 7], [6, 2, 4]])

pls = PLSRegression(n_components=3)
pls.fit(X, Y)
W = pls.x_loadings_
C = pls.y_loadings_
T = pls.x_scores_
U = pls.y_scores_

Xw = pls.x_weights_
Yw = pls.y_weights_

pls.predict(X)
((X - X.mean()) / X.std()) @ pls._coef_.T + pls.intercept_

pls.x_weights_

# plot a scatter plot of Val 1 vs Val 2
plt.scatter(T[:, 0], T[:, 1])
plt.xlabel("Val 1")
plt.ylabel("Val 2")
plt.show()
