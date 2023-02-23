import pandas as pd
import numpy as np
import os

os.listdir("data")

data = pd.read_csv("data/tidy_X.csv")
data
# query the conditon for the verification
data.query("cod == 'A01' and hod == 1")
data_grp = data.groupby(["cod", "hod"]).agg(freq_by_codhod=("cod", "size"))
data_grp = data_grp.reset_index()

sum_cod = (
    data_grp.groupby("cod").agg(sum_by_cod=("freq_by_codhod", "sum")).reset_index()
)

# left table: data_grp
data_grp
# right table: sum_cod
sum_cod

# we want to add the column: "sum_by_cod" from the dataframe 'sum_cod' to the dataframe 'data_grp'
data_grp2 = pd.merge(data_grp, sum_cod, on="cod")
