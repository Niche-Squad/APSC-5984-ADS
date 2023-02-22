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

# tidy_2_bboard.csv ---- ---- ---- ---- ---- ---- ----
filepath = os.path.join("data", "tidy_2_bboard.csv")
data = pd.read_csv(filepath)

# define tidy data components
id_var = data.columns[:7]
var_name = "week"
value_name = "rank"

# melt the data
df_tidy = data.melt(id_vars=id_var, var_name=var_name, value_name=value_name)
df_tidy

# to clean the "week" column
new_col = []
for val_wk in df_tidy["week"]:
    # val_wk is "x1st.week"
    new_value = re.findall(r"\d+", val_wk)[0]  # get the first item
    new_value = int(new_value)
    new_col.append(new_value)

# assign the new column values to the existing one "week"
df_tidy["week"] = new_col

df_tidy.dropna()
df_tidy["rank"].isna()

# little experiment
sample_string = "x10987st.week"
import re

# +: repeat 1 or more {either 1-digit or 2-digit}
# ?: repeat 0 or 1
# *: repeat 0 or more
re.findall(r"\d+", sample_string)

# tidy_3_tb.csv ---- ---- ---- ---- ---- ---- ----
filepath = os.path.join("data", "tidy_3_tb.csv")
data = pd.read_csv(filepath)

# define the components of a tidy data and tidy it
col_names = data.columns
id_vars = col_names[:2]
df_tidy = data.melt(id_vars=id_vars)

# check the messy part of the column "variable"
df_tidy["variable"].unique()
df_tidy2 = df_tidy.query("variable not in ['new_sp', 'new_sp_mu', 'new_sp_fu']")

# little experiment
sample_str = "new_sp_m04"
str_1 = sample_str.replace("new_sp_", "")
age = re.findall(r"\d+", str_1)
gender = re.findall(r"[mf]+", str_1)

# breakdown the column
ls_age = []
ls_gender = []
for item in df_tidy2["variable"]:
    str_1 = item.replace("new_sp_", "")
    age = re.findall(r"\d+", str_1)[0]  # grab on the 1st item
    gender = re.findall(r"[mf]+", str_1)[0]
    ls_age.append(age)
    ls_gender.append(gender)

ls_age
ls_gender
df_tidy2["age"] = ls_age
df_tidy2["gender"] = ls_gender
