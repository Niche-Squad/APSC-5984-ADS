# make sure the install pandas before running this script
# installation command:
#   python -m pip install pandas

import pandas as pd
import os

os.getcwd()

path = os.path.join("data", "file_D.csv")
print(path)

data = pd.read_csv(path)

# iloc: get the 6th row
data.iloc[5, :]["factor"]

# loc: get the column factor
data.loc[:, "factor"]
data["factor"]

data.loc[:, "new_column_A"] = data["factor"] + data["id"]
new_col = []
for f, i in zip(data["factor"], data["id"]):
    new_value = f + "-" + i
    print("assigning value: ", new_value)
    new_col.append(new_value)

data.loc[:, "new_column_B"] = new_col
data

# query
data_q = data.query("env == 'env_2'")
data_q[:3]

# get the 3rd row
data_q.iloc[2, :]
# equivalent
data_q.loc[5, :]

# hardcopy

# if we make any change to the new dataframe, will it affect the original data?
# it is a hardcopy
data_q.loc[3, "factor"] = "aaaaabbbccc"
data["factor"].value_counts()
data_q["factor"].value_counts()

# group
data.groupby("new_column_A").agg("mean")
dt_pivot = data.groupby(["factor", "id"]).agg("mean")

dt_pivot.loc["B"].loc["id_2"]
data_new = dt_pivot.reset_index()
data_new.query("factor == 'B' and id == 'id_2'")
