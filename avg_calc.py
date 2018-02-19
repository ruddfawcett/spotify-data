import csv
import pandas as pd

topper = True

def generate():
    pois = ['streak', 'danceability', 'energy', 'valence', 'tempo', 'duration_ms', 'time_signature']
    if topper:
        source = 'toppers.csv'
    else:
        source='remainder.csv'

    for poi in pois:
        with open(source) as f:
            data = csv.DictReader(f)
            sums = {}
            count = {}

            for datum in data:
                if str(datum['debut_year']) in sums:
                    if datum[poi] == '':
                        sums[str(datum['debut_year'])] += 0
                    else:
                        sums[str(datum['debut_year'])] += float(datum[poi])
                    count[str(datum['debut_year'])] += 1
                else:
                    if datum[poi] == '':
                        sums[str(datum['debut_year'])] = 0
                    else:
                        sums[str(datum['debut_year'])] = float(datum[poi])
                    count[str(datum['debut_year'])] = 1

            avg = {}
            matched = []

            for year in sorted(sums, reverse = True):
                matched.append({
                    'year': year,
                    'avg_{0}'.format(poi): sums[year]/count[year]
                })

            db = pd.DataFrame(matched, columns = matched[0].keys())
            db.set_index('year', inplace=True)

            if topper:
                db.to_csv('avgs_toppers/avg_{0}.csv'.format(poi))
            else:
                db.to_csv('avgs/avg_{0}.csv'.format(poi))

            f.seek(0)
            sums = {}
            count = {}

generate()
topper = False
generate()
