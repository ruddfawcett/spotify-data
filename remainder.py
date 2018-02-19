import csv
import pandas as pd

data = csv.DictReader(open('cleaned_data.csv', encoding='utf-8'))

toppers = []
remainder = []

for datum in data:
    if int(datum['peak_pos']) < 6:
        toppers.append(datum)

    remainder.append(datum)

db = pd.DataFrame(toppers, columns=toppers[0].keys())
db.set_index('id', inplace=True)
db.to_csv('toppers.csv')

db2 = pd.DataFrame(remainder, columns=remainder[0].keys())
db2.set_index('id', inplace=True)
db2.to_csv('remainder.csv')
