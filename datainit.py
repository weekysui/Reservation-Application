import sqlite3
import pandas as pd
# connect the sqlitedb
conn = sqlite3.connect('project1.db')
c = conn.cursor()

# create dataframe from csv files:
clientdf = pd.read_csv('MOCK_DATA.csv')
servicedf = pd.read_csv('service.csv')
pricedf = pd.read_csv('price.csv')
typedf = pd.read_csv('type.csv')
durationdf = pd.read_csv('duration.csv')
usersdf = pd.read_csv('users.csv')

# get the date in right format
clientdf['start_date'] = pd.to_datetime(clientdf['start_date'])
clientdf['end_date'] = pd.to_datetime(clientdf['end_date'])

# import csv into table 'clients', 'services', 'price' in sqlite3
clientdf.to_sql('clients', conn, if_exists='replace', index=False)
servicedf.to_sql('services', conn, if_exists='replace', index=False)
pricedf.to_sql('price', conn, if_exists='replace', index=False)
typedf.to_sql('type', conn, if_exists='replace', index=False)
pricedf.to_sql('duration', conn, if_exists='replace', index=False)
usersdf.to_sql('users',conn, if_exists='replace', index=False)
