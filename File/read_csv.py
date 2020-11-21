import csv

with open('files/data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import pandas as pd

df = pd.read_csv('files/data.csv')
print(type(df))
print(df)
