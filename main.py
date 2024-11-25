import pandas
import sqlite3 as sql

# create the database
conn = sql.connect('train_db.db')

# get the raw data
train_data = pandas.read_csv('join20240426.csv')
train_data.to_sql('Connections', conn, if_exists='replace', index=False)

train_data = pandas.read_csv('station20240426.csv')
train_data.to_sql('Stations', conn, if_exists='replace', index=False)

train_data = pandas.read_csv('line20240426.csv')
train_data.to_sql('Lines', conn, if_exists='replace', index=False)

train_data = pandas.read_csv('company20240328.csv')
train_data.to_sql('Companies', conn, if_exists='replace', index=False)

cur = conn.cursor()
conn.close()
