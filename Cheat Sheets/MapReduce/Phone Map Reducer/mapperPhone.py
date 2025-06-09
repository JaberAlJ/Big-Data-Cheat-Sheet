#/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    if words[4] == '1':
        v1 = datetime.strptime(words[2],"%Y-%m-%d %H:%M:%S")
        v2 = datetime.strptime(words[3],"%Y-%m-%d %H:%M:%S")
        D = v2-v1
        strtime = D.__str__()
        total_sec = int(strtime[0:1]) * 60 * 60 + int(strtime[3:4])* 60 + int(strtime[6:7])
        print('%s\t%s' % (words[0], total_sec))
    else:
        pass