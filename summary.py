import sys
from collections import Counter

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))

counts = Counter()
for line in lines:
    print(line)
"""
    fields = line.split()
    if len(fields) > 0:
        key = fields[0]
        counts[key] += 1
print("Top 5:")
for item, n in counts.most_common(5):
    print(item, n)"""