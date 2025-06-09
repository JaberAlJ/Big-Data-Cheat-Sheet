#!/usr/bib/python
import sys
storecost={}
for line in sys.stdin:
    line = line.strip()
    location, cost = line.split('\t')
    try:
        cost = float(cost)
    except ValueError:
        continue
    try:
        storecost[location] = storecost[location] + cost
    except:
        storecost[location] = cost

for loc in storecost.keys():
        print ('%s\t%f' % (loc, storecost[loc]))
