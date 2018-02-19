import csv

data = csv.DictReader(open('cleaned_data.csv', encoding='utf-8'))

# minor = 0
# major = 0
#
# for datum in data:
#     if datum['mode']:
#         if int(datum['debut_year']) < 2007:
#             if float(datum['mode']) == 0:
#                 minor += 1
#             elif float(datum['mode']) == 1:
#                 major += 1
#             else:
#                 print('Discovered something that is not major or minor.')
#
# tot = major+minor
#
# print('Major: {0}, Minor: {1}. Major %: {2}, Minor %: {3}'.format(major, minor, (major/tot)*100, (minor/tot)*100))
#
#
# sums = {}

tot = 0

for datum in data:
    if int(datum['peak_pos']) == 1:
        tot += 1

print(tot)
