import sys

employee = {}

for line in sys.stdin:
    line = line.strip()
    dept, sal = line.split("\t")
    
    try:
        employee[dept] = employee[dept] + int(sal)
    except:
        employee[dept] = int(sal)

for x in employee.keys():
    print("{0}\t{1}".format(x, employee[x]))
