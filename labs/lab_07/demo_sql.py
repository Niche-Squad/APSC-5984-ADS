# !python -m pip install "requests[security]"
# !python -m pip install pyopenssl idna
import requests
import pandas as pd
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://www.google.com/",
}


API = "XXXXXXX"
params = {"apikey": API, "y": 37.221508, "x": -80.423857, "radius": 100}
base_url = "https://www.usdalocalfoodportal.com/api/onfarmmarket/"
response = requests.get(base_url, headers=headers, params=params)
response

# parse it to JSON format
res_j = response.json()

res_j.keys()
data = pd.DataFrame(res_j["data"])
data.head()
data["distance"] = data["distance"].astype("float32")
data_sort = data.sort_values("distance")
data_sort.iloc[0]


# params = {"apikey": API, "zip": 24060}
params = {"apikey": API, "city": "Blacksburg"}
base_url = "https://www.usdalocalfoodportal.com/api/onfarmmarket/"
response = requests.get(base_url, headers=headers, params=params)
response
rjson = response.json()
rjson

pd.DataFrame(rjson["data"])
