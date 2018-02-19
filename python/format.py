import csv

track_list = csv.DictReader(open('debut_year_matched.csv'));

'''
Generate the total number of streaks for each one...
'''

# bins = [0] * 87

# biggest = 0
#
# for track in track_list:
#     streak = int(track['streak'])
#     if streak > biggest:
#         biggest = streak
#
#     bins[streak-1] += 1
#
# print(bins)
#
# for i in range(0, len(bins)):
#     bins[i] = str(i+1)
#
# print(bins)

'''
Generate the number of hits to reach number one.
'''

bins = [0] * 100

for track in track_list:
    if int(track['debut_year']) < 1967 or int(track['debut_year']) > 2017:
        continue

    peak_pos = int(track['peak_pos'])
    bins[peak_pos-1] += 1

print(bins)

# for i in range(0, len(bins)):
#     bins[i] = str(i+1)

# print(bins)

tot = 0
for num in bins:
    tot += int(num)

print(tot)
