import requests
import pandas as pd

# !python -m pip install "requests[security]"
# !python -m pip install pyopenssl idna

import requests

API = "ooPHlu1UfS"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://www.google.com/",
}
params = {"apikey": API, "y": 37.221508, "x": -80.423857, "radius": 100}
base_url = "https://www.usdalocalfoodportal.com/api/farmersmarket/"
response = requests.get(base_url, headers=headers, params=params)
response

json_data = response.json()
df = pd.DataFrame(json_data["data"])

# check the columns
df.columns
df.info()

# encounter error
df.query("distance < 30")

# cast
df["distance"] = df["distance"].astype(float)
df.query("distance < 30")  # 30 miles

# select cols
cols = [
    "listing_name",
    "brief_desc",
    "contact_name",
    "contact_phone",
    "media_website",
    "media_facebook",
    "media_twitter",
    "location_city",
    "location_state",
    "location_y",
    "location_x",
]

df.loc[1, cols]

# your turn
base_url = "https://www.usdalocalfoodportal.com/api/onfarmmarket/"


# ARMS
import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://www.google.com/",
}
API = "FXfemZwMCc2geLcixYpbmxviFihEUJmpU99yBPlw"


# arms/year
params = {"api_key": API}
url = "https://api.ers.usda.gov/data/arms/year"
response = requests.get(url, headers=headers, params=params)
json_data = response.json()
json_data

# get all report
params = {"api_key": API}
url = "https://api.ers.usda.gov/data/arms/report"
response = requests.get(url, headers=headers, params=params)
js = response.json()
js.keys()
df = pd.DataFrame(response.json()["data"])
df

# arms/surveydata
params = {"api_key": API, "Year": 2019}
url = "https://api.ers.usda.gov/data/arms/surveydata"
response = requests.get(url, headers=headers, params=params)
json_data = response.json()
json_data


params = {
    "api_key": API,
    "Year": 2018,
    "report": "Farm Business Income Statement",
}
url = "https://api.ers.usda.gov/data/arms/surveydata"
response = requests.get(url, headers=headers, params=params)
json_data = response.json()
data = pd.DataFrame(json_data["data"])
data

data.columns

data["farmtype"].unique()

data["category"].unique()

data.query("variable_name == 'Gross cash farm income'").query(
    "category == 'Operator Age'"
)


data.query("variable_name == 'Gross cash farm income'").query(
    "category == 'Farm Typology'"
)

data.query("variable_name == 'Gross cash farm income'").query(
    "category == 'Collapsed Farm Typology'"
)

data.query("variable_name == 'Gross cash farm income'").query(
    "category == 'Production Specialty'"
)


data["category_value"].unique()


data["variable_name"].unique()
data


def query_data(year, API, report="Farm Business Income Statement"):
    # inputs
    params = {
        "api_key": API,
        "Year": year,
        "report": report,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Referer": "https://www.google.com/",
    }
    url = "https://api.ers.usda.gov/data/arms/surveydata"
    # query
    response = requests.get(url, headers=headers, params=params)
    print("status code:", response.status_code)
    json_data = response.json()
    data = pd.DataFrame(json_data["data"])
    # parse output
    data = data.query("variable_name == 'Gross cash farm income'")
    return data


def post_process(data):
    cols = ["year", "category", "category_value", "estimate", "median", "rse"]
    datasub = data.loc[:, cols]
    datasub["se"] = datasub["estimate"] * (datasub["rse"] / 100)
    datasub["upper"] = datasub["estimate"] + datasub["se"] * 1.96  # 95% CI
    datasub["lower"] = datasub["estimate"] - datasub["se"] * 1.96  # 95% CI
    return datasub


data18 = query_data(2018, API)
data18 = post_process(data18)
data18

import time

data = pd.DataFrame()
for year in range(2008, 2022):  # only 2008-2021
    print("Loading data for year", year)
    data_query = query_data(year, API)
    data_query = post_process(data_query)
    data = pd.concat([data, data_query], axis=0)
    time.sleep(1)


dataplot = data.query("category in ['NASS Region', 'Production Specialty']")

from plotnine import *

dataplot["group"] = dataplot["category"] + " - " + dataplot["category_value"]

# 95% CI
(
    ggplot(
        dataplot.query("category == 'NASS Region'"),
        aes(x="year", color="category_value", group="group"),
    )
    + geom_line(aes(y="estimate", color="category_value"))
    + geom_line(aes(y="median", color="category_value"))
    + geom_ribbon(aes(ymin="lower", ymax="upper", fill="category_value"), alpha=0.2)
    + facet_grid("category ~ .", scales="free")
    # figure size
    + theme(
        figure_size=(10, 10),
    )
)

# original scale
(
    ggplot(
        dataplot.query(
            "category == 'Production Specialty' and category_value in ['Dairy', 'Cattle', 'Hogs', 'Poultry']"
        ),
        aes(
            x="year",
            color="category_value",
            fill="category_value",
            group="category_value",
        ),
    )
    + geom_line(aes(y="log_estimate"))
    + geom_line(aes(y="median"))
    + geom_ribbon(aes(ymin="lower", ymax="upper"), alpha=0.2)
    + facet_grid("category ~ .", scales="free")
    # color theme
    + scale_color_brewer(type="qual", palette="Set2")
    + scale_fill_brewer(type="qual", palette="Set2")
    + theme(
        figure_size=(10, 10),
    )
)


import numpy as np

dataplot["log_estimate"] = np.log(dataplot["estimate"])
dataplot["log_upper"] = np.log(dataplot["upper"])
dataplot["log_lower"] = np.log(dataplot["lower"])
dataplot["log_median"] = np.log(dataplot["median"])
(
    ggplot(
        dataplot.query(
            "category == 'Production Specialty' and category_value in ['Dairy', 'Cattle', 'Hogs', 'Poultry']"
        ),
        aes(
            x="year",
            color="category_value",
            fill="category_value",
            group="category_value",
        ),
    )
    + geom_line(aes(y="log_estimate"), size=1)
    + geom_line(aes(y="log_median"))
    + geom_ribbon(aes(ymin="log_lower", ymax="log_upper"), alpha=0.2)
    + facet_grid("category ~ .", scales="free")
    # color theme
    + scale_color_brewer(type="qual", palette="Set2")
    + scale_fill_brewer(type="qual", palette="Set2")
    + theme(
        figure_size=(10, 10),
    )
)
