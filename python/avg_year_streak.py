import csv
import pandas as pd

data = csv.DictReader(open('debut_year_matched.csv'))

sums = {}
count = {}

for entry in data:
    if str(entry['debut_year']) in sums:
        sums[str(entry['debut_year'])] += int(entry['streak'])
        count[str(entry['debut_year'])] += 1
    else:
        sums[str(entry['debut_year'])] = int(entry['streak'])
        count[str(entry['debut_year'])] = 1

avg = {}
matched = []

for year in sorted(sums, reverse=True):
    matched.append({
        'year': year,
        'avg_streak': sums[year]/count[year]
    })

db = pd.DataFrame(matched, columns=matched[0].keys())
db.set_index('year', inplace=True)
db.to_csv('year_avg_streak.csv')
