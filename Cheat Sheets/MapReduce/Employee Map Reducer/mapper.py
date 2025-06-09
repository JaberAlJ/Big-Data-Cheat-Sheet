import string
import fileinput

for line in fileinput.input():
    data = line.strip().split(",")
    if len(data) == 4:
        empId, empName, sal, dept = data
        print("{0}\t{1}".format(empName, dept))
