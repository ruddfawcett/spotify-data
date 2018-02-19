#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas as pd

data = csv.DictReader(open('billboard_spotify_matched_data.csv', encoding='utf-8'))

cleaned_data = []

for datum in data:
    if int(datum['debut_year']) < 1968 or int(datum['debut_year']) > 2017:
        continue

    cleaned_data.append(datum)

print(len(cleaned_data))

db = pd.DataFrame(cleaned_data, columns=cleaned_data[0].keys())
db.set_index('id', inplace=True)
db = db.drop('del1', 1)
db = db.drop('del2', 1)
db.to_csv('cleaned_data.csv', float_format='%.6f')
