# APSC-5984 Lab 7: API and Database

- [APSC-5984 Lab 7: API and Database](#apsc-5984-lab-7-api-and-database)
  - [0. Overview](#0-overview)
  - [1. USDA local food portal API](#1-usda-local-food-portal-api)
    - [Configuration](#configuration)
    - [Request responses](#request-responses)
    - [Parsing JSON](#parsing-json)
    - [Rearranging the data](#rearranging-the-data)
  - [2. Agricultural Resource Management Survey (ARMS) API](#2-agricultural-resource-management-survey-arms-api)
    - [API key](#api-key)
    - [Use `arms/year` to get the list of available years](#use-armsyear-to-get-the-list-of-available-years)
    - [Use `arms/report` to get the list of available reports](#use-armsreport-to-get-the-list-of-available-reports)
    - [Farm Business Income Statement](#farm-business-income-statement)
    - [Check the data](#check-the-data)
    - [Functions](#functions)
    - [Query multiple years](#query-multiple-years)
    - [Visualize the data](#visualize-the-data)
  - [3. SQLite3](#3-sqlite3)
    - [Create a database](#create-a-database)
    - [Save the database](#save-the-database)
    - [Insert data](#insert-data)
    - [Add constraints to columns](#add-constraints-to-columns)
    - [Reference integrity](#reference-integrity)
    - [SQlite3 VS. Pandas](#sqlite3-vs-pandas)
      - [Sorting](#sorting)
      - [Filtering](#filtering)
      - [Grouping](#grouping)
    - [sqlite\_master](#sqlite_master)
    - [Collection of functions](#collection-of-functions)


## 0. Overview

API stands for Application Programming Interface. It is a set of tools meant to interact with other software or database. In this lab, we will use `requests` to interact with two USDA APIs. Later this week, we will also use `sqlite3` to practice building a database on our own.



```python
import pandas as pd
import numpy as np
import requests
```

## 1. USDA local food portal API

### Configuration

Before you can use the API, you need to get an API key and essentail parameters, such as the database you want to interact with and the query you want to run. Please treat the API key as a password and do not share it with others. Go to the [USDA local food portal](https://www.usdalocalfoodportal.com/fe/fregisterpublicapi) to register for an API key.


```python
API = "xxxxxxx" # fill in your API key
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://www.google.com/",
}
params = {"apikey": API, "y": 37.221508, "x": -80.423857, "radius": 100}
base_url = "https://www.usdalocalfoodportal.com/api/farmersmarket/"
```

### Request responses

The responses are usually coded as 3-digit numbers. The most common ones are:

* 1xx - Informational response - the request was received, continuing process
* 2xx - Success - the request was successfully received, understood, and accepted
* 3xx - Redirection - further action needs to be taken in order to complete the request
* 4xx - Client error - the request contains bad syntax or cannot be fulfilled
* 5xx - Server error - the server failed to fulfill an apparently valid request

In most cases, you want to get a 2xx response. If you get a 4xx or 5xx response, you need to check your code and make sure you are using the API correctly.


```python
response = requests.get(base_url, headers=headers, params=params)
response
```




    <Response [200]>



### Parsing JSON

The response from the API is usually in JSON format. JSON stands for JavaScript Object Notation. It is a lightweight data-interchange format. It is not easy for humans to read and write, hense we can call `.json()` and `pd.DataFrame()` to parse the response into a tabular format.


```python
json = response.json()
df = pd.DataFrame(json["data"])
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>directory_type</th>
      <th>directory_name</th>
      <th>updatetime</th>
      <th>listing_image</th>
      <th>listing_id</th>
      <th>listing_name</th>
      <th>listing_desc</th>
      <th>brief_desc</th>
      <th>mydesc</th>
      <th>contact_name</th>
      <th>...</th>
      <th>media_blog</th>
      <th>location_address</th>
      <th>location_state</th>
      <th>location_city</th>
      <th>location_street</th>
      <th>location_zipcode</th>
      <th>location_x</th>
      <th>location_y</th>
      <th>distance</th>
      <th>term</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>farmersmarket</td>
      <td>farmers market</td>
      <td>Jan 26th, 2021</td>
      <td>default-farmersmarket-4-3.jpg</td>
      <td>300156</td>
      <td>Salem Farmers Market</td>
      <td>None</td>
      <td>Open: April to December; January to March; &lt;br...</td>
      <td></td>
      <td>Market Manager</td>
      <td>...</td>
      <td>None</td>
      <td>3 East Main Street, Salem, Virginia 24153</td>
      <td>Virginia</td>
      <td>Salem</td>
      <td>3 East Main Street</td>
      <td>24153</td>
      <td>-80.058606</td>
      <td>37.292997</td>
      <td>20.684638895041772</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>farmersmarket</td>
      <td>farmers market</td>
      <td>Feb 1st, 2021</td>
      <td>default-farmersmarket-4-3.jpg</td>
      <td>300469</td>
      <td>Grandin Village Farmers Market</td>
      <td>None</td>
      <td>Open: April to November; November to March; &lt;b...</td>
      <td></td>
      <td>Sam Lev</td>
      <td>...</td>
      <td>None</td>
      <td>2080 Westover Ave SW, Roanoke, Virginia 24015</td>
      <td>Virginia</td>
      <td>Roanoke</td>
      <td>2080 Westover Ave SW</td>
      <td>24015</td>
      <td>-79.978064</td>
      <td>37.265053</td>
      <td>24.703908391067827</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>farmersmarket</td>
      <td>farmers market</td>
      <td>Sep 27th, 2021</td>
      <td>default-farmersmarket-4-3.jpg</td>
      <td>301601</td>
      <td>The Historic City Market</td>
      <td>None</td>
      <td>Open: Year-round&lt;br&gt;Available Products: Fresh ...</td>
      <td></td>
      <td>Eric L Pendleton</td>
      <td>...</td>
      <td>None</td>
      <td>213 Market St SE 3rd Floor, Downtown Roanoke I...</td>
      <td>Virginia</td>
      <td>Roanoke</td>
      <td>213 Market St SE 3rd Floor, Downtown Roanoke Inc.</td>
      <td>24011</td>
      <td>-79.939064</td>
      <td>37.271606</td>
      <td>26.88770808513208</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>farmersmarket</td>
      <td>farmers market</td>
      <td>Aug 23rd, 2021</td>
      <td>default-farmersmarket-4-3.jpg</td>
      <td>301590</td>
      <td>Rocky Mount Farmers Market</td>
      <td>None</td>
      <td>Open: April to December; &lt;br&gt;Available Product...</td>
      <td></td>
      <td>Paul Cauley</td>
      <td>...</td>
      <td>None</td>
      <td>435 Franklin St, Rocky Mount, Virginia 24151</td>
      <td>Virginia</td>
      <td>Rocky Mount</td>
      <td>435 Franklin St</td>
      <td>24151</td>
      <td>-79.888073</td>
      <td>36.994866</td>
      <td>33.41846778835633</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>farmersmarket</td>
      <td>farmers market</td>
      <td>Jan 7th, 2021</td>
      <td>default-farmersmarket-4-3.jpg</td>
      <td>300467</td>
      <td>Wytheville Farmers Market</td>
      <td>None</td>
      <td>Open: Year-round&lt;br&gt;Available Products: Fresh ...</td>
      <td></td>
      <td>Joanne McNulty</td>
      <td>...</td>
      <td>None</td>
      <td>210 W. Spring Street, Wytheville , Virginia 24368</td>
      <td>Virginia</td>
      <td>Wytheville</td>
      <td>210 W. Spring Street</td>
      <td>24368</td>
      <td>-81.083367</td>
      <td>36.9486397</td>
      <td>40.94927484093051</td>
      <td></td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>



### Rearranging the data

The data might contain more information than you need. We can use Pandas techniques we learned before to rearrange the data.


```python
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

df.loc[:, cols]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>listing_name</th>
      <th>brief_desc</th>
      <th>contact_name</th>
      <th>contact_phone</th>
      <th>media_website</th>
      <th>media_facebook</th>
      <th>media_twitter</th>
      <th>location_city</th>
      <th>location_state</th>
      <th>location_y</th>
      <th>location_x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Salem Farmers Market</td>
      <td>Open: April to December; January to March; &lt;br...</td>
      <td>Market Manager</td>
      <td>540-375-4098</td>
      <td>market.salemva.gov</td>
      <td>https://www.facebook.com/SalemVaMarket</td>
      <td>https://twitter.com/SalemVaMarket</td>
      <td>Salem</td>
      <td>Virginia</td>
      <td>37.292997</td>
      <td>-80.058606</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Grandin Village Farmers Market</td>
      <td>Open: April to November; November to March; &lt;b...</td>
      <td>Sam Lev</td>
      <td>540-632-1360</td>
      <td>www.leapforlocalfood.org/grandin</td>
      <td>facebook.com/grandinvillagecommunitymarket</td>
      <td>@leapforlocal</td>
      <td>Roanoke</td>
      <td>Virginia</td>
      <td>37.265053</td>
      <td>-79.978064</td>
    </tr>
    <tr>
      <th>2</th>
      <td>The Historic City Market</td>
      <td>Open: Year-round&lt;br&gt;Available Products: Fresh ...</td>
      <td>Eric L Pendleton</td>
      <td>5403422028</td>
      <td>Downtownroanoke.org</td>
      <td>The Historic City Market</td>
      <td>None</td>
      <td>Roanoke</td>
      <td>Virginia</td>
      <td>37.271606</td>
      <td>-79.939064</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rocky Mount Farmers Market</td>
      <td>Open: April to December; &lt;br&gt;Available Product...</td>
      <td>Paul Cauley</td>
      <td>540-488-2023</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>Rocky Mount</td>
      <td>Virginia</td>
      <td>36.994866</td>
      <td>-79.888073</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wytheville Farmers Market</td>
      <td>Open: Year-round&lt;br&gt;Available Products: Fresh ...</td>
      <td>Joanne McNulty</td>
      <td>276-620-4095</td>
      <td>www.wythevillefarmersmarket.com</td>
      <td>Wytheville Farmers Market</td>
      <td>None</td>
      <td>Wytheville</td>
      <td>Virginia</td>
      <td>36.9486397</td>
      <td>-81.083367</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Galax Farmers Market</td>
      <td>Open: 05/11/2023 to 10/28/2023; &lt;br&gt;Available ...</td>
      <td>Jordan Shaw</td>
      <td>276.733.4145</td>
      <td>https://visitgalax.com/</td>
      <td>https://www.facebook.com/search/top?q=galaxfar...</td>
      <td></td>
      <td>Galax</td>
      <td>VA</td>
      <td>36.6632146</td>
      <td>-80.925742</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Forest farmers market</td>
      <td>Open: April to October; November to December; ...</td>
      <td>Dorothy McIntyre</td>
      <td>434-665-5475</td>
      <td>www.forestfarmersmarket.com</td>
      <td>https://www.facebook.com/pages/Forest-farmers-...</td>
      <td>https://twitter.com/FFM221</td>
      <td>Forest</td>
      <td>Virginia</td>
      <td>37.3643700</td>
      <td>-79.285443</td>
    </tr>
    <tr>
      <th>7</th>
      <td>King Farmers' Market</td>
      <td>Open: May to September; &lt;br&gt;Available Products...</td>
      <td>Deb Fox</td>
      <td>336-618-1086</td>
      <td>www.kingfarmersmarket.com</td>
      <td>www.facebook.com/KingFarmersMarket</td>
      <td>https://twitter.com/KingFarmersMkt</td>
      <td>King</td>
      <td>North Carolina</td>
      <td>36.276367</td>
      <td>-80.341178</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Lynchburg Community Market</td>
      <td>Open: Year-round&lt;br&gt;Available Products: Fresh ...</td>
      <td>Ricky Kowalewski</td>
      <td>434.455.3962</td>
      <td>http://lynchburgcommunitymarket.com/</td>
      <td>https://www.facebook.com/LynchburgCommunityMar...</td>
      <td>None</td>
      <td>Lynchburg</td>
      <td>Virginia</td>
      <td>37.411517</td>
      <td>-79.140379</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Market at Second Stage</td>
      <td>Open: May to October; November to April; &lt;br&gt;A...</td>
      <td>Mary Hurst</td>
      <td>434.941.0997</td>
      <td>https://secondstageamherst.org/markets</td>
      <td>https://www.facebook.com/The-Market-at-Second-...</td>
      <td>None</td>
      <td>Amherst</td>
      <td>Virginia</td>
      <td>37.583162</td>
      <td>-79.048809</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Piedmont Triad Farmers Market</td>
      <td>Open: Year-round&lt;br&gt;Available Products: Fresh ...</td>
      <td>Rick Cecil</td>
      <td>(336) 605-9157</td>
      <td>www.triadfarmersmarket.com</td>
      <td>https://www.facebook.com/pages/Robert-G-Shaw-P...</td>
      <td>None</td>
      <td>Colfax</td>
      <td>North Carolina</td>
      <td>36.087691</td>
      <td>-79.992657</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Wilkes County Farmers' Market</td>
      <td>Open: April to October; ; &lt;br&gt;Available Produc...</td>
      <td>Garrett Griffin</td>
      <td>3366677129</td>
      <td>www.downtownnorthwilkesboro.com</td>
      <td>https://www.facebook.com/wilkescountyfarmersma...</td>
      <td>None</td>
      <td>North Wilkesboro</td>
      <td>North Carolina</td>
      <td>36.159075</td>
      <td>-81.145200</td>
    </tr>
    <tr>
      <th>12</th>
      <td>The Corner Farmers Market</td>
      <td>Open: Year-round&lt;br&gt;Available Products: Fresh ...</td>
      <td>Kathy Newsom</td>
      <td>3365586924</td>
      <td>www.cornermarketgso.com</td>
      <td>https://www.facebook.com/walkerelamcornermarket/</td>
      <td>None</td>
      <td>Greensboro</td>
      <td>North Carolina</td>
      <td>36.069019</td>
      <td>-79.828293</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Webster Springs Farmer's Market</td>
      <td>Open: July to October; &lt;br&gt;Available Products:...</td>
      <td>Mike Hall</td>
      <td>304-847-2727</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>Webster Springs</td>
      <td>West Virginia</td>
      <td>38.478420</td>
      <td>-80.415459</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Boone Winter Farmers Market</td>
      <td>Open: 12/03/2022 to 03/25/2023; &lt;br&gt;Available ...</td>
      <td>Rachel Kinard</td>
      <td>803-429-3943</td>
      <td>https://www.brwia.org/wintermarket.html</td>
      <td>https://www.facebook.com/BooneWinterFM</td>
      <td></td>
      <td>Boone</td>
      <td>North Carolina</td>
      <td>36.2204478</td>
      <td>-81.6887158</td>
    </tr>
    <tr>
      <th>15</th>
      <td>King Street Farmers Market</td>
      <td>Open: 05/03/2022 to 10/25/2022; &lt;br&gt;Available ...</td>
      <td>Rachel Kinard</td>
      <td>8034293943</td>
      <td>https://www.brwia.org/ksm.html</td>
      <td>https://www.facebook.com/KingStreetMkt</td>
      <td></td>
      <td>Boone</td>
      <td>North Carolina</td>
      <td>36.2198305</td>
      <td>-81.69312339999999</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Verona Farmers Market</td>
      <td>Open: May to October; &lt;br&gt;Available Products: ...</td>
      <td>Georgia Meyer</td>
      <td>651-356-2410</td>
      <td>https://www.projectgrows.org/food-access/north...</td>
      <td>https://www.facebook.com/NAFarmMarket/?ref=boo...</td>
      <td>None</td>
      <td>Verona</td>
      <td>Virginia</td>
      <td>38.193744</td>
      <td>-79.010219</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Carrboro Farmers' Market</td>
      <td>Open: January to March; March to October; Nove...</td>
      <td>Maggie Funkhouser</td>
      <td>9192803326</td>
      <td>www.carrborofarmersmarket.com</td>
      <td>https://www.facebook.com/carrborofarmersmarket</td>
      <td>None</td>
      <td>Carrboro</td>
      <td>North Carolina</td>
      <td>35.910781</td>
      <td>-79.077607</td>
    </tr>
    <tr>
      <th>18</th>
      <td>The Chapel Hill Farmers' Market</td>
      <td>Open: 04/02/2022 to 11/19/2022; 12/03/2022 to ...</td>
      <td>Kate Underhill</td>
      <td>9195339496</td>
      <td>https://www.thechapelhillfarmersmarket.com/</td>
      <td>https://www.facebook.com/TheChapelHillFarmersM...</td>
      <td>https://twitter.com/chfarmersmarket</td>
      <td>Chapel Hill</td>
      <td>North Carolina</td>
      <td>35.927587</td>
      <td>-79.026717</td>
    </tr>
  </tbody>
</table>
</div>



## 2. Agricultural Resource Management Survey (ARMS) API

### API key

Go to [ARMS API](https://www.ers.usda.gov/developer/data-apis/arms-data-api/#apiForm) to obtain an API key for the USDA ARMS API.


```python
API = "xxxxxxx" # fill in your API key
params = {"api_key": API}
```

### Use `arms/year` to get the list of available years

This API has a lot of data. Based on the documentation https://www.ers.usda.gov/developer/data-apis/arms-data-api/#apiForm, we can use `arms/year` to get the list of available years.


```python
# arms/year
url = "https://api.ers.usda.gov/data/arms/year"
response = requests.get(url, headers=headers, params=params)
json_data = response.json()
json_data
```




    {'status': 'ok',
     'info': {'timing': {'executing': 93, 'unit': 'ms'},
      'result_coverage': 'total',
      'total': {'record_count': 26}},
     'data': [2021,
      2020,
      2019,
      2018,
      2017,
      2016,
      2015,
      2014,
      2013,
      2012,
      2011,
      2010,
      2009,
      2008,
      2007,
      2006,
      2005,
      2004,
      2003,
      2002,
      2001,
      2000,
      1999,
      1998,
      1997,
      1996]}



### Use `arms/report` to get the list of available reports

To make sure we are using the API correctly, we can use `arms/report` to get the list of available reports. We will later need to use the correct report name to get the data.


```python
# get all report
url = "https://api.ers.usda.gov/data/arms/report"
response = requests.get(url, headers=headers, params=params)
js = response.json()
df = pd.DataFrame(response.json()["data"])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>desc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Farm Business Balance Sheet</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Farm Business Income Statement</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Farm Business Financial Ratios</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Structural Characteristics</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Farm Business Debt Repayment Capacity</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Government Payments</td>
      <td>None</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Operator Household Income</td>
      <td>None</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Operator Household Balance Sheet</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>



### Farm Business Income Statement

Let's say we want to get the farm business income statement for all farms in the US for the years 2008 to 2022. We can start with a single year, say 2018.


```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>state</th>
      <th>report</th>
      <th>farmtype</th>
      <th>category</th>
      <th>category_value</th>
      <th>category2</th>
      <th>category2_value</th>
      <th>variable_id</th>
      <th>variable_name</th>
      <th>...</th>
      <th>variable_group_id</th>
      <th>variable_unit</th>
      <th>variable_description</th>
      <th>variable_is_invalid</th>
      <th>estimate</th>
      <th>median</th>
      <th>statistic</th>
      <th>rse</th>
      <th>unreliable_estimate</th>
      <th>decimal_display</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Operator Age</td>
      <td>55 to 64 years old</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>kount</td>
      <td>Farms</td>
      <td>...</td>
      <td>None</td>
      <td>Number</td>
      <td>Estimated number of farms.</td>
      <td>False</td>
      <td>694246.0</td>
      <td>NaN</td>
      <td>TOTAL</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Farm Typology</td>
      <td>Retirement farms (2011 to present)</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>kount</td>
      <td>Farms</td>
      <td>...</td>
      <td>None</td>
      <td>Number</td>
      <td>Estimated number of farms.</td>
      <td>False</td>
      <td>250289.0</td>
      <td>NaN</td>
      <td>TOTAL</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Farm Typology</td>
      <td>Farming occupation/lower-sales farms (2011 to ...</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>kount</td>
      <td>Farms</td>
      <td>...</td>
      <td>None</td>
      <td>Number</td>
      <td>Estimated number of farms.</td>
      <td>False</td>
      <td>640223.0</td>
      <td>NaN</td>
      <td>TOTAL</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Collapsed Farm Typology</td>
      <td>Intermediate farms</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>kount</td>
      <td>Farms</td>
      <td>...</td>
      <td>None</td>
      <td>Number</td>
      <td>Estimated number of farms.</td>
      <td>False</td>
      <td>742931.0</td>
      <td>NaN</td>
      <td>TOTAL</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>NASS Region</td>
      <td>Atlantic region</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>kount</td>
      <td>Farms</td>
      <td>...</td>
      <td>None</td>
      <td>Number</td>
      <td>Estimated number of farms.</td>
      <td>False</td>
      <td>400703.0</td>
      <td>NaN</td>
      <td>TOTAL</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1483</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Economic Class</td>
      <td>Less than $100,000</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>infi</td>
      <td>Net farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>Net farm income indicates the profit or loss a...</td>
      <td>False</td>
      <td>3060.0</td>
      <td>1763.0</td>
      <td>MEAN</td>
      <td>20.5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1484</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Production Specialty</td>
      <td>Soybean</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>infi</td>
      <td>Net farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>Net farm income indicates the profit or loss a...</td>
      <td>False</td>
      <td>52760.0</td>
      <td>16317.0</td>
      <td>MEAN</td>
      <td>9.1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1485</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Production Specialty</td>
      <td>Tobacco, Cotton, Peanuts</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>infi</td>
      <td>Net farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>Net farm income indicates the profit or loss a...</td>
      <td>False</td>
      <td>96513.0</td>
      <td>30838.0</td>
      <td>MEAN</td>
      <td>26.8</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1486</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Production Specialty</td>
      <td>Poultry</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>infi</td>
      <td>Net farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>Net farm income indicates the profit or loss a...</td>
      <td>False</td>
      <td>47773.0</td>
      <td>13140.0</td>
      <td>MEAN</td>
      <td>17.5</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1487</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Production Specialty</td>
      <td>All other livestock</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>infi</td>
      <td>Net farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>Net farm income indicates the profit or loss a...</td>
      <td>False</td>
      <td>2657.0</td>
      <td>-848.0</td>
      <td>MEAN</td>
      <td>108.6</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1488 rows × 23 columns</p>
</div>



### Check the data

You can check the data by inspecting the unique values of each column of interest. For example, if you want to know any category other than "Operator Age", you can use the following code:


```python
data["category"].unique()
```




    array(['Operator Age', 'Farm Typology', 'Collapsed Farm Typology',
           'NASS Region', 'Farm Resource Region', 'Economic Class',
           'Production Specialty', 'All Farms'], dtype=object)



You may also want to know what `Production Specialty` was recorded as. You can combine `df.query()` and `df.unique()`.


```python
data.query("category == 'Production Specialty'").loc[:, "category_value"].unique()
```




    array(['Corn', 'Tobacco, Cotton, Peanuts', 'Other Field Crops', 'Cattle',
           'Hogs', 'Dairy', 'All other livestock', 'General Cash Grains',
           'Wheat', 'Soybean', 'Specialty Crops (F,V,N)', 'Poultry'],
          dtype=object)



We can check variables to know what attributes are available for that category.


```python
data.query("category == 'Production Specialty'").loc[:, "variable_name"].unique()
```




    array(['Farms', 'Gross cash farm income', 'Livestock income',
           'Crop sales', 'Government payments', 'Other farm-related income',
           'Total cash expenses', 'Variable expenses', 'Livestock purchases',
           'Feed', 'Other livestock-related', 'Seed and plants',
           'Fertilizer and chemicals', 'Utilities', 'Labor', 'Fuels and oils',
           'Repairs and maintenance', 'Machine-hire and custom work',
           'Other variable expenses', 'Fixed expenses',
           'Real estate and property taxes', 'Interest', 'Insurance premiums',
           'Rent and lease payments', 'Net cash farm income',
           'Nonmoney income', 'Value of inventory change', 'Depreciation',
           'Labor, non-cash benefits', 'Adjusted breeding livestock income',
           'Net farm income'], dtype=object)



### Functions

It is a good idea to wrap up the code into functions so that you can reuse them later. Especially when we deal with the queries with repeated patterns, we can use functions to make the code more concise.

To design a function, first thing we can to define is the input and output. In our case, we provide API key and parameters (year, report name, etc.) as input and get a parsed dataframe as output.


```python
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
```

Validate the function


```python
data = query_data(2018, API)
data.head()
```

    status code: 200





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>state</th>
      <th>report</th>
      <th>farmtype</th>
      <th>category</th>
      <th>category_value</th>
      <th>category2</th>
      <th>category2_value</th>
      <th>variable_id</th>
      <th>variable_name</th>
      <th>...</th>
      <th>variable_group_id</th>
      <th>variable_unit</th>
      <th>variable_description</th>
      <th>variable_is_invalid</th>
      <th>estimate</th>
      <th>median</th>
      <th>statistic</th>
      <th>rse</th>
      <th>unreliable_estimate</th>
      <th>decimal_display</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>48</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Operator Age</td>
      <td>34 years or younger</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>igcfi</td>
      <td>Gross cash farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>For farms participating in government programs...</td>
      <td>False</td>
      <td>212459.0</td>
      <td>30102.0</td>
      <td>MEAN</td>
      <td>11.8</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>49</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Operator Age</td>
      <td>55 to 64 years old</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>igcfi</td>
      <td>Gross cash farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>For farms participating in government programs...</td>
      <td>False</td>
      <td>188384.0</td>
      <td>7140.0</td>
      <td>MEAN</td>
      <td>4.0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Operator Age</td>
      <td>65 years or older</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>igcfi</td>
      <td>Gross cash farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>For farms participating in government programs...</td>
      <td>False</td>
      <td>108034.0</td>
      <td>8865.0</td>
      <td>MEAN</td>
      <td>6.3</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>51</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Farm Typology</td>
      <td>Farming occupation/lower-sales farms (2011 to ...</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>igcfi</td>
      <td>Gross cash farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>For farms participating in government programs...</td>
      <td>False</td>
      <td>27750.0</td>
      <td>9800.0</td>
      <td>MEAN</td>
      <td>4.1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2018</td>
      <td>All survey states</td>
      <td>Farm Business Income Statement</td>
      <td>All Farms</td>
      <td>Farm Typology</td>
      <td>Very large farms (2011 to present)</td>
      <td>All Farms</td>
      <td>TOTAL</td>
      <td>igcfi</td>
      <td>Gross cash farm income</td>
      <td>...</td>
      <td>None</td>
      <td>Dollars per farm</td>
      <td>For farms participating in government programs...</td>
      <td>False</td>
      <td>11634254.0</td>
      <td>7404800.0</td>
      <td>MEAN</td>
      <td>11.3</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>



We can define another function to process the data we get from the API. In this example, we will do the following processing:

- Select the columns of interest
- calculate standard deviation of the income statement
- calculate 95% confidence interval of the standard deviation


```python
def post_process(data):
    cols = ["year", "category", "category_value", "estimate", "median", "rse"]
    datasub = data.loc[:, cols]
    datasub["se"] = datasub["estimate"] * (datasub["rse"] / 100)
    datasub["upper"] = datasub["estimate"] + datasub["se"] * 1.96  # 95% CI
    datasub["lower"] = datasub["estimate"] - datasub["se"] * 1.96  # 95% CI
    return datasub
```

Always check the results to make sure the function works as expected.


```python
data18 = query_data(2018, API)
data18 = post_process(data18)
data18.head()
```

    status code: 200





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>category</th>
      <th>category_value</th>
      <th>estimate</th>
      <th>median</th>
      <th>rse</th>
      <th>se</th>
      <th>upper</th>
      <th>lower</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>48</th>
      <td>2018</td>
      <td>Operator Age</td>
      <td>34 years or younger</td>
      <td>212459.0</td>
      <td>30102.0</td>
      <td>11.8</td>
      <td>25070.162</td>
      <td>2.615965e+05</td>
      <td>1.633215e+05</td>
    </tr>
    <tr>
      <th>49</th>
      <td>2018</td>
      <td>Operator Age</td>
      <td>55 to 64 years old</td>
      <td>188384.0</td>
      <td>7140.0</td>
      <td>4.0</td>
      <td>7535.360</td>
      <td>2.031533e+05</td>
      <td>1.736147e+05</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2018</td>
      <td>Operator Age</td>
      <td>65 years or older</td>
      <td>108034.0</td>
      <td>8865.0</td>
      <td>6.3</td>
      <td>6806.142</td>
      <td>1.213740e+05</td>
      <td>9.469396e+04</td>
    </tr>
    <tr>
      <th>51</th>
      <td>2018</td>
      <td>Farm Typology</td>
      <td>Farming occupation/lower-sales farms (2011 to ...</td>
      <td>27750.0</td>
      <td>9800.0</td>
      <td>4.1</td>
      <td>1137.750</td>
      <td>2.997999e+04</td>
      <td>2.552001e+04</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2018</td>
      <td>Farm Typology</td>
      <td>Very large farms (2011 to present)</td>
      <td>11634254.0</td>
      <td>7404800.0</td>
      <td>11.3</td>
      <td>1314670.702</td>
      <td>1.421101e+07</td>
      <td>9.057499e+06</td>
    </tr>
  </tbody>
</table>
</div>



### Query multiple years

With the functions we defined, it is now easier to query multiple years. We can use a for loop to iterate through the years and use the functions we defined to get the data. To avoid overloading the server, we can use `time.sleep()` to pause the code for one second between each query.


```python
import time

data = pd.DataFrame()
for year in range(2008, 2022):  # only 2008-2021
    print("Loading data for year", year)
    data_query = query_data(year, API)
    data_query = post_process(data_query)
    data = pd.concat([data, data_query], axis=0)
    time.sleep(1)
```

    Loading data for year 2008
    status code: 200
    Loading data for year 2009
    status code: 200
    Loading data for year 2010
    status code: 200
    Loading data for year 2011
    status code: 200
    Loading data for year 2012
    status code: 200
    Loading data for year 2013
    status code: 200
    Loading data for year 2014
    status code: 200
    Loading data for year 2015
    status code: 200
    Loading data for year 2016
    status code: 200
    Loading data for year 2017
    status code: 200
    Loading data for year 2018
    status code: 200
    Loading data for year 2019
    status code: 200
    Loading data for year 2020
    status code: 200
    Loading data for year 2021
    status code: 200


Check the result


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>category</th>
      <th>category_value</th>
      <th>estimate</th>
      <th>median</th>
      <th>rse</th>
      <th>se</th>
      <th>upper</th>
      <th>lower</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>47</th>
      <td>2008</td>
      <td>Operator Age</td>
      <td>45 to 54 years old</td>
      <td>155557.0</td>
      <td>6892.0</td>
      <td>4.1</td>
      <td>6377.837</td>
      <td>1.680576e+05</td>
      <td>1.430564e+05</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2008</td>
      <td>Farm Typology</td>
      <td>Retirement farms (1996 through 2010)</td>
      <td>13992.0</td>
      <td>4000.0</td>
      <td>4.3</td>
      <td>601.656</td>
      <td>1.517125e+04</td>
      <td>1.281275e+04</td>
    </tr>
    <tr>
      <th>49</th>
      <td>2008</td>
      <td>Collapsed Farm Typology</td>
      <td>Intermediate farms</td>
      <td>57234.0</td>
      <td>22000.0</td>
      <td>2.4</td>
      <td>1373.616</td>
      <td>5.992629e+04</td>
      <td>5.454171e+04</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2008</td>
      <td>Collapsed Farm Typology</td>
      <td>Commercial farms</td>
      <td>813566.0</td>
      <td>414011.0</td>
      <td>2.4</td>
      <td>19525.584</td>
      <td>8.518361e+05</td>
      <td>7.752959e+05</td>
    </tr>
    <tr>
      <th>51</th>
      <td>2008</td>
      <td>NASS Region</td>
      <td>Atlantic region</td>
      <td>67912.0</td>
      <td>5200.0</td>
      <td>3.6</td>
      <td>2444.832</td>
      <td>7.270387e+04</td>
      <td>6.312013e+04</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>91</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Tobacco, Cotton, Peanuts</td>
      <td>886937.0</td>
      <td>522000.0</td>
      <td>14.0</td>
      <td>124171.180</td>
      <td>1.130313e+06</td>
      <td>6.435615e+05</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Other Field Crops</td>
      <td>53155.0</td>
      <td>5000.0</td>
      <td>9.7</td>
      <td>5156.035</td>
      <td>6.326083e+04</td>
      <td>4.304917e+04</td>
    </tr>
    <tr>
      <th>93</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Specialty Crops (F,V,N)</td>
      <td>447255.0</td>
      <td>16904.0</td>
      <td>13.3</td>
      <td>59484.915</td>
      <td>5.638454e+05</td>
      <td>3.306646e+05</td>
    </tr>
    <tr>
      <th>94</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Poultry</td>
      <td>183738.0</td>
      <td>21000.0</td>
      <td>16.8</td>
      <td>30867.984</td>
      <td>2.442392e+05</td>
      <td>1.232368e+05</td>
    </tr>
    <tr>
      <th>95</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Dairy</td>
      <td>1565673.0</td>
      <td>332890.0</td>
      <td>7.2</td>
      <td>112728.456</td>
      <td>1.786621e+06</td>
      <td>1.344725e+06</td>
    </tr>
  </tbody>
</table>
<p>669 rows × 9 columns</p>
</div>



### Visualize the data

Now, let's focus on the two categories: `NASS Region` and `Production Specialty`. We will use ggplot2 (`plotnine` library) to visualize the income statement for each category across years.


```python
from plotnine import *
dataplot = data.query("category in ['NASS Region', 'Production Specialty']")
dataplot["group"] = dataplot["category"] + " - " + dataplot["category_value"]
dataplot
```

    /var/folders/0k/_fn4_dgn04b2b44_sfhbshzr0000gp/T/ipykernel_59862/1007048301.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>category</th>
      <th>category_value</th>
      <th>estimate</th>
      <th>median</th>
      <th>rse</th>
      <th>se</th>
      <th>upper</th>
      <th>lower</th>
      <th>group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>51</th>
      <td>2008</td>
      <td>NASS Region</td>
      <td>Atlantic region</td>
      <td>67912.0</td>
      <td>5200.0</td>
      <td>3.6</td>
      <td>2444.832</td>
      <td>7.270387e+04</td>
      <td>6.312013e+04</td>
      <td>NASS Region - Atlantic region</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2008</td>
      <td>NASS Region</td>
      <td>South region</td>
      <td>92042.0</td>
      <td>4800.0</td>
      <td>8.2</td>
      <td>7547.444</td>
      <td>1.068350e+05</td>
      <td>7.724901e+04</td>
      <td>NASS Region - South region</td>
    </tr>
    <tr>
      <th>53</th>
      <td>2008</td>
      <td>NASS Region</td>
      <td>Midwest region</td>
      <td>140805.0</td>
      <td>12600.0</td>
      <td>2.4</td>
      <td>3379.320</td>
      <td>1.474285e+05</td>
      <td>1.341815e+05</td>
      <td>NASS Region - Midwest region</td>
    </tr>
    <tr>
      <th>54</th>
      <td>2008</td>
      <td>NASS Region</td>
      <td>Plains region</td>
      <td>116175.0</td>
      <td>8203.0</td>
      <td>3.2</td>
      <td>3717.600</td>
      <td>1.234615e+05</td>
      <td>1.088885e+05</td>
      <td>NASS Region - Plains region</td>
    </tr>
    <tr>
      <th>55</th>
      <td>2008</td>
      <td>NASS Region</td>
      <td>West region</td>
      <td>215985.0</td>
      <td>7465.0</td>
      <td>3.8</td>
      <td>8207.430</td>
      <td>2.320716e+05</td>
      <td>1.998984e+05</td>
      <td>NASS Region - West region</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>91</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Tobacco, Cotton, Peanuts</td>
      <td>886937.0</td>
      <td>522000.0</td>
      <td>14.0</td>
      <td>124171.180</td>
      <td>1.130313e+06</td>
      <td>6.435615e+05</td>
      <td>Production Specialty - Tobacco, Cotton, Peanuts</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Other Field Crops</td>
      <td>53155.0</td>
      <td>5000.0</td>
      <td>9.7</td>
      <td>5156.035</td>
      <td>6.326083e+04</td>
      <td>4.304917e+04</td>
      <td>Production Specialty - Other Field Crops</td>
    </tr>
    <tr>
      <th>93</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Specialty Crops (F,V,N)</td>
      <td>447255.0</td>
      <td>16904.0</td>
      <td>13.3</td>
      <td>59484.915</td>
      <td>5.638454e+05</td>
      <td>3.306646e+05</td>
      <td>Production Specialty - Specialty Crops (F,V,N)</td>
    </tr>
    <tr>
      <th>94</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Poultry</td>
      <td>183738.0</td>
      <td>21000.0</td>
      <td>16.8</td>
      <td>30867.984</td>
      <td>2.442392e+05</td>
      <td>1.232368e+05</td>
      <td>Production Specialty - Poultry</td>
    </tr>
    <tr>
      <th>95</th>
      <td>2021</td>
      <td>Production Specialty</td>
      <td>Dairy</td>
      <td>1565673.0</td>
      <td>332890.0</td>
      <td>7.2</td>
      <td>112728.456</td>
      <td>1.786621e+06</td>
      <td>1.344725e+06</td>
      <td>Production Specialty - Dairy</td>
    </tr>
  </tbody>
</table>
<p>238 rows × 10 columns</p>
</div>



By region


```python
(
    ggplot(
        dataplot.query("category == 'NASS Region'"),
        aes(x="year", color="category_value", group="group"),
    )
    + geom_line(aes(y="estimate", color="category_value"))
    + geom_line(aes(y="median", color="category_value"))
    + geom_ribbon(aes(ymin="lower", ymax="upper", fill="category_value"), alpha=0.2)
    + theme(figure_size=(10, 10))
)
```


    
![png](readme_files/readme_39_0.png)
    





    <ggplot: (685146251)>



By production specialty. We only show the livestock categories.


```python
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
    + geom_line(aes(y="estimate"))
    + geom_line(aes(y="median"))
    + geom_ribbon(aes(ymin="lower", ymax="upper"), alpha=0.2)
    # color theme
    + scale_color_brewer(type="qual", palette="Set2")
    + scale_fill_brewer(type="qual", palette="Set2")
    + theme(figure_size=(10, 10))
)
```


    
![png](readme_files/readme_41_0.png)
    





    <ggplot: (685147956)>



We can apply a log transformation to the data to make the plot more readable.


```python
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
    + scale_color_brewer(type="qual", palette="Set2")
    + scale_fill_brewer(type="qual", palette="Set2")
    + theme(figure_size=(10, 10))
)

```

    /var/folders/0k/_fn4_dgn04b2b44_sfhbshzr0000gp/T/ipykernel_59862/885553557.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    /var/folders/0k/_fn4_dgn04b2b44_sfhbshzr0000gp/T/ipykernel_59862/885553557.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    /Users/niche/miniforge3/envs/niche/lib/python3.9/site-packages/pandas/core/arraylike.py:402: RuntimeWarning: invalid value encountered in log
    /var/folders/0k/_fn4_dgn04b2b44_sfhbshzr0000gp/T/ipykernel_59862/885553557.py:5: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    /Users/niche/miniforge3/envs/niche/lib/python3.9/site-packages/pandas/core/arraylike.py:402: RuntimeWarning: divide by zero encountered in log
    /var/folders/0k/_fn4_dgn04b2b44_sfhbshzr0000gp/T/ipykernel_59862/885553557.py:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy



    
![png](readme_files/readme_43_1.png)
    





    <ggplot: (685725654)>



## 3. SQLite3

After we learn how to interact with an existing database through API, we can also build our own database using our own data. In this section, we will use `sqlite3` to build a database and query the data.



```python
import sqlite3
```

### Create a database

Creating a database is as simple as creating a file. We can use `sqlite3.connect()` to create a database file.


```python
conn = sqlite3.connect("demo.db") # conn stands for connection
```

Like we learned in the previous section, a database can contain multiple tables (or surveys, reports). To craete a table, we need to specify the name of the columns and the data type. We also need to specify the primary key, which is a unique identifier for each row. We can create a table named `users` with the following columns:

- `id` - INTEGER (PRIMARY KEY)
- `name` - TEXT
- `gender` - TEXT
- `age` - INTEGER


```python
cur = conn.cursor() # cur stands for cursor
cur.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT,
        age INTEGER
    )
    """
)
```




    <sqlite3.Cursor at 0x28fdb7c70>



Check the table columns


```python
cur.execute("PRAGMA table_info(users)")
cur.fetchall()
```




    [(0, 'id', 'INTEGER', 0, None, 1),
     (1, 'name', 'TEXT', 1, None, 0),
     (2, 'gender', 'TEXT', 0, None, 0),
     (3, 'age', 'INTEGER', 0, None, 0)]



If you think the command is too complicated, we can use a function to simplify the process.


```python
def list_cols(cur, table):
    cur.execute("PRAGMA table_info(%s)" % table)
    return display([x[1:3] for x in cur.fetchall()])

list_cols(cur, "users")
```


    [('id', 'INTEGER'), ('name', 'TEXT'), ('gender', 'TEXT'), ('age', 'INTEGER')]


### Save the database

We can use `conn.commit()` to save the changes to the database. Like how we deal with a file, we need to close `conn.close()` the database after we are done with it.


```python
conn.commit()
conn.close()
```

Or we can use a `with` statement to automatically close the database after we are done with it.


```python
with sqlite3.connect("demo.db") as conn:
    cur = conn.cursor()
    list_cols(cur, "users")
```


    [('id', 'INTEGER'), ('name', 'TEXT'), ('gender', 'TEXT'), ('age', 'INTEGER')]


### Insert data

There are two ways to insert data into a table:

Provide information for all columns
- `INSERT INTO users VALUES (1, 'John', 'M', 20)`

Provide information for some columns
- `INSERT INTO users (name, gender) VALUES ('John', 'M')`


```python
cur.execute("INSERT INTO users VALUES (1, 'Mary', 'F', 25)")
cur.execute("INSERT INTO users (name) VALUES ('John')")
```




    <sqlite3.Cursor at 0x28fdb7c70>



Check the data


```python
cur.execute("SELECT * FROM users")
cur.fetchall()
```




    [(1, 'Mary', 'F', 25), (2, 'John', None, None)]



Or wrap it up in a function


```python
def print_table(cur, table):
    cur.execute("SELECT * FROM %s" % table)
    display(cur.fetchall())

print_table(cur, "users")
```


    [(1, 'Mary', 'F', 25),
     (2, 'John', None, None),
     (3, 'Camille', 'female', 40),
     (4, 'Mike', 'male', 25),
     (5, 'Jason', 'male', 35),
     (6, 'Maria', 'female', 20)]


You can actually use `df.to_sql()` to insert data into a table. Parameters we need to consider:

- `if_exists`: If the table already exists, we can choose to `replace` the table, or `append` the data to the existing table.
- `index`: whether to include the index of the dataframe as a column in the table.


```python
df = pd.DataFrame(
    {
        "name": ["Camille", "Mike", "Jason", "Maria"],
        "gender": ["female", "male", "male", "female"],
        "age": [40, 25, 35, 20],
    }
)
df.to_sql("users", conn, if_exists="append", index=False)  # if_exists="replace"
```




    4




```python
print_table(cur, "users")
```


    [(1, 'Mary', 'F', 25),
     (2, 'John', None, None),
     (3, 'Camille', 'female', 40),
     (4, 'Mike', 'male', 25),
     (5, 'Jason', 'male', 35),
     (6, 'Maria', 'female', 20)]


### Add constraints to columns

You might notice that the gender values were not in a consistent format, which should either be [`M`, `F`] or [`Male`, `Female`]. We can use `CHECK` to add constraints to the columns.

Before re-creating the table, we need to drop the table first.


```python
cur.execute("DROP TABLE users")
```




    <sqlite3.Cursor at 0x28fdb7b20>



Then create a new table with the constraints:

* id - INTEGER (PRIMARY KEY)
* name - TEXT - NOT NULL
* gender - TEXT - can only be either 'male' or 'female'
* age - INTEGER - must be in the range of 0 to 150
* weight - REAL - must be in the range of 0 to 300


```python
cur.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT CHECK(gender IN ("male", "female")),
        age INTEGER CHECK(age >= 0 AND age <= 150),
        weight REAL CHECK(weight >= 0 AND weight <= 300)
    )
    """
)
```




    <sqlite3.Cursor at 0x28fdb7b20>



Now, let's try to insert data again. We can start with expected values:


```python
cur.execute("INSERT INTO users VALUES (1, 'Mary', 'female', 25, 150)")
```




    <sqlite3.Cursor at 0x28fdb7b20>




```python
print_table(cur, "users")
```


    [(1, 'Mary', 'female', 25, 150.0)]


Let's try different exceptions:


```python
cur.execute("INSERT INTO users VALUES (2, 'Mary', 'f', 25, 150)")
```


    ---------------------------------------------------------------------------

    IntegrityError                            Traceback (most recent call last)

    Cell In[112], line 1
    ----> 1 cur.execute("INSERT INTO users VALUES (2, 'Mary', 'f', 25, 150)")


    IntegrityError: CHECK constraint failed: gender IN ("male", "female")



```python
cur.execute("INSERT INTO users VALUES (2, 'Mary', 'female', -3, 200)")
```


    ---------------------------------------------------------------------------

    IntegrityError                            Traceback (most recent call last)

    Cell In[114], line 1
    ----> 1 cur.execute("INSERT INTO users VALUES (2, 'Mary', 'female', -3, 200)")


    IntegrityError: CHECK constraint failed: age >= 0 AND age <= 150


By setting constraints to the columns, it is easier to ensure the data quality when the database is growing. Here is a complete code for creating a `user` table with data inserted.


```python
with sqlite3.connect("demo.db") as conn:
    cur = conn.cursor()
    cur.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        gender TEXT CHECK(gender IN ("male", "female")),
        age INTEGER CHECK(age >= 0 AND age <= 150),
        weight REAL CHECK(weight >= 0 AND weight <= 300)
    )
    """)

    df = pd.DataFrame(
        {
            "name": ["Camille", "Mike", "Jason", "Maria"],
            "gender": ["female", "male", "male", "female"],
            "age": [40, 25, 35, 20],
            "weight": [150, 200, 180, 120],
        }
    )
    df.to_sql("users", conn, if_exists="append", index=False)
    print_table(cur, "users")
```

### Reference integrity

We already have a table `users` to define users' information. Now, let's create another table `walks` to record the walking activity.


```python
conn = sqlite3.connect("demo.db")
cur = conn.cursor()
cur.execute(
    """
    CREATE TABLE walks (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        distance FLOAT NOT NULL,
        duration INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id))
    """
)
```

You may notice that we set `user_id` as the foreign key. This means that the value of `user_id` must correspond to the value of `id` in the `users` table when we need to consider the relationship between the two tables. This is called a `reference integrity`. We can use `REFERENCES` to set the reference integrity.

The `walks` table include the information of the walking date, distance, and duration.Let's insert data into this `walks` table.


```python
data = pd.DataFrame(
    data={
        "user_id": [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
        "date": [
            "02-26-2023",
            "02-27-2023",
            "02-28-2023",
            "02-26-2023",
            "02-27-2023",
            "02-26-2023",
            "02-27-2023",
            "02-26-2023",
            "02-27-2023",
            "02-28-2023",
        ],
        "distance": [1.2, 1.5, 1.7, 2.2, 2.5, 3.2, 3.5, 4.2, 4.5, 4.7],
        "duration": [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
    }
)
data.to_sql("walks", conn, if_exists="append", index=False)
```




    10




```python
print_table(cur, "walks")
```


    [(1, '02-26-2023', 1.2, 30),
     (1, '02-27-2023', 1.5, 40),
     (1, '02-28-2023', 1.7, 50),
     (2, '02-26-2023', 2.2, 60),
     (2, '02-27-2023', 2.5, 70),
     (3, '02-26-2023', 3.2, 80),
     (3, '02-27-2023', 3.5, 90),
     (4, '02-26-2023', 4.2, 100),
     (4, '02-27-2023', 4.5, 110),
     (4, '02-28-2023', 4.7, 120)]


Ok, now we have two tables with data inserted. We can use `JOIN` to put the data from two tables together.


```python
cur.execute(
    """
    SELECT * FROM walks JOIN users
    ON walks.user_id = users.id
    """
)
cur.fetchall()
```




    [(1, '02-26-2023', 1.2, 30, 1, 'Camille', 'female', 40, 150.0),
     (1, '02-27-2023', 1.5, 40, 1, 'Camille', 'female', 40, 150.0),
     (1, '02-28-2023', 1.7, 50, 1, 'Camille', 'female', 40, 150.0),
     (2, '02-26-2023', 2.2, 60, 2, 'Mike', 'male', 25, 200.0),
     (2, '02-27-2023', 2.5, 70, 2, 'Mike', 'male', 25, 200.0),
     (3, '02-26-2023', 3.2, 80, 3, 'Jason', 'male', 35, 180.0),
     (3, '02-27-2023', 3.5, 90, 3, 'Jason', 'male', 35, 180.0),
     (4, '02-26-2023', 4.2, 100, 4, 'Maria', 'female', 20, 120.0),
     (4, '02-27-2023', 4.5, 110, 4, 'Maria', 'female', 20, 120.0),
     (4, '02-28-2023', 4.7, 120, 4, 'Maria', 'female', 20, 120.0)]



You see that the user information was added to the `walks` table. This is similar to how we use `df.merge()` to combine two dataframes in Pandas.


```python
df_users = pd.read_sql("SELECT * FROM users", conn)
df_walks = pd.read_sql("SELECT * FROM walks", conn)
pd.merge(df_walks, df_users, left_on="user_id", right_on="id")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>date</th>
      <th>distance</th>
      <th>duration</th>
      <th>id</th>
      <th>name</th>
      <th>gender</th>
      <th>age</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>02-26-2023</td>
      <td>1.2</td>
      <td>30</td>
      <td>1</td>
      <td>Camille</td>
      <td>female</td>
      <td>40</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>02-27-2023</td>
      <td>1.5</td>
      <td>40</td>
      <td>1</td>
      <td>Camille</td>
      <td>female</td>
      <td>40</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>02-28-2023</td>
      <td>1.7</td>
      <td>50</td>
      <td>1</td>
      <td>Camille</td>
      <td>female</td>
      <td>40</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>02-26-2023</td>
      <td>2.2</td>
      <td>60</td>
      <td>2</td>
      <td>Mike</td>
      <td>male</td>
      <td>25</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>02-27-2023</td>
      <td>2.5</td>
      <td>70</td>
      <td>2</td>
      <td>Mike</td>
      <td>male</td>
      <td>25</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>02-26-2023</td>
      <td>3.2</td>
      <td>80</td>
      <td>3</td>
      <td>Jason</td>
      <td>male</td>
      <td>35</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>02-27-2023</td>
      <td>3.5</td>
      <td>90</td>
      <td>3</td>
      <td>Jason</td>
      <td>male</td>
      <td>35</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4</td>
      <td>02-26-2023</td>
      <td>4.2</td>
      <td>100</td>
      <td>4</td>
      <td>Maria</td>
      <td>female</td>
      <td>20</td>
      <td>120.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4</td>
      <td>02-27-2023</td>
      <td>4.5</td>
      <td>110</td>
      <td>4</td>
      <td>Maria</td>
      <td>female</td>
      <td>20</td>
      <td>120.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4</td>
      <td>02-28-2023</td>
      <td>4.7</td>
      <td>120</td>
      <td>4</td>
      <td>Maria</td>
      <td>female</td>
      <td>20</td>
      <td>120.0</td>
    </tr>
  </tbody>
</table>
</div>



### SQlite3 VS. Pandas

Here we will put the major functionalities of SQLite3 and Pandas side by side to see how they compare.

#### Sorting

SQLite3


```python
cur.execute("SELECT * FROM users ORDER BY age DESC")  # or ASC
cur.fetchall()
```




    [(1, 'Camille', 'female', 40, 150.0),
     (3, 'Jason', 'male', 35, 180.0),
     (2, 'Mike', 'male', 25, 200.0),
     (4, 'Maria', 'female', 20, 120.0)]



Pandas


```python
df_users.sort_values(by="age", ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>gender</th>
      <th>age</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Camille</td>
      <td>female</td>
      <td>40</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Jason</td>
      <td>male</td>
      <td>35</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Mike</td>
      <td>male</td>
      <td>25</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Maria</td>
      <td>female</td>
      <td>20</td>
      <td>120.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Filtering

SQLite3


```python
cur.execute("SELECT age, gender FROM users WHERE age > 30")
cur.fetchall()
```




    [(40, 'female'), (35, 'male')]



Pandas


```python
df_users.loc[:, ["age", "gender"]].query("age > 30")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>40</td>
      <td>female</td>
    </tr>
    <tr>
      <th>2</th>
      <td>35</td>
      <td>male</td>
    </tr>
  </tbody>
</table>
</div>



SQLite3


```python
cur.execute(
    """
    SELECT name, weight FROM users
    WHERE name LIKE '%m%'
    OR name LIKE '%n%'
    """
)
cur.fetchall()
```




    [('Camille', 150.0), ('Mike', 200.0), ('Jason', 180.0), ('Maria', 120.0)]



Pandas


```python
df_users.loc[:, ["name", "weight"]].query(
    """
    name.str.upper().str.contains('M') |\
    name.str.upper().str.contains('N')
    """
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Camille</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mike</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jason</td>
      <td>180.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Maria</td>
      <td>120.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Grouping

SQLite3


```python
cur.execute(
    """
    SELECT user_id, avg(distance), sum(duration), count(distance)
    FROM walks GROUP BY user_id
    """
)
cur.fetchall()
```




    [(1, 1.4666666666666668, 120, 3),
     (2, 2.35, 130, 2),
     (3, 3.35, 170, 2),
     (4, 4.466666666666666, 330, 3)]



Pandas


```python
df_walks.groupby("user_id").aggregate(
    distance_mean=("distance", "mean"),
    duration_sum=("duration", "sum"),
    distance_count=("distance", "count"),
)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>distance_mean</th>
      <th>duration_sum</th>
      <th>distance_count</th>
    </tr>
    <tr>
      <th>user_id</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1.466667</td>
      <td>120</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.350000</td>
      <td>130</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.350000</td>
      <td>170</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.466667</td>
      <td>330</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### sqlite_master

`sqliet_master` is a system table that contains the information of all tables in the database. We can use `SELECT * FROM sqlite_master` to get the information of all tables. The output will look like this:

* `type`: the type of the object. In this case, it is `table`.
* `name`: the name of the table.
* `tbl_name`: the name of the table.
* `rootpage`: the page number of the root b-tree page for the table.
* `sql`: the SQL statement used to create the table.


```python
cur.execute("SELECT * FROM sqlite_master")
cur.fetchall()
```




    [('table',
      'users',
      'users',
      2,
      'CREATE TABLE users (\n        id INTEGER PRIMARY KEY,\n        name TEXT NOT NULL,\n        gender TEXT CHECK(gender IN ("male", "female")),\n        age INTEGER CHECK(age >= 0 AND age <= 150),\n        weight REAL CHECK(weight >= 0 AND weight <= 300)\n    )'),
     ('table',
      'walks',
      'walks',
      3,
      'CREATE TABLE "walks" (\n"user_id" INTEGER,\n  "date" TEXT,\n  "distance" REAL,\n  "duration" INTEGER\n)')]



Or simply list all the tables in the database.


```python
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
cur.fetchall()
```




    [('users',), ('walks',)]



### Collection of functions


```python
def list_cols(cur, table):
    cur.execute("PRAGMA table_info(%s)" % table)
    cols = [x[1:3] for x in cur.fetchall()]
    return display(cols)

def print_table(cur, table):
    cur.execute("SELECT * FROM %s" % table)
    output = cur.fetchall()
    display(output)

def clean_table(cur, table):
    cur.execute("DELETE FROM %s" % table)

def drop_table(cur, table):
    cur.execute("DROP TABLE %s" % table)
```
