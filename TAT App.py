# %%
import psycopg2
import pandas as pd
import streamlit as st

# %%
#conn = psycopg2.connect(
#  database="AllTables", user='readonlyuser@datamartreplica', password='Apollo@1read', host='datamartreplica.postgres.database.azure.com', port= '5432'
#)
#cursor = conn.cursor()

# %%
masterDos = pd.read_excel("masterDos.xlsx")

# %%
tatFile = pd.read_csv("latestTat.csv")

# %%
pricingFile = pd.read_excel("pricingFile.xlsx")

# %%
allItemIds = tatFile['ItemId'].unique()

# %%
itemNameDict = {}
notFoundItem = []
for i in allItemIds:
    if i in pricingFile['itemId'].values:
        itemName = pricingFile[pricingFile['itemId']==i]['itemName'].unique()
        if len(itemName)==0:
            print(itemName)
            print(i)
        itemNameDict[i] = str(itemName[0])
    else:
        notFoundItem.append(i)

# %%
for i in notFoundItem:
    if i in masterDos.Itemid.values:
        itemName = masterDos[masterDos['Itemid']==i]['InvestigationName'].unique()
        itemNameDict[i] = str(itemName[0])

# %%
cityName = tatFile['City'].unique()

# %%
cityNameDict = {}
for i in cityName:
    cityId = tatFile[tatFile['City']==i]['CityId'].unique()
    cityNameDict[cityId[0]] = i

# %%
testName = st.selectbox("Select a test name",itemNameDict.values())

# %%

st.text(testName)


