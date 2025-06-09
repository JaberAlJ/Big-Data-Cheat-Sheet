#/usr/bin/python
import sys

callsabove =  {}
for line in sys.stdin:
   line = line.strip()
   caller,secs = line.split('\t')
   try:
      secs = int(secs)
   except ValueError:
      continue
   try:
      callsabove[caller] = callsabove[caller] + secs
   except:
      callsabove[caller] = secs

for caller in callsabove.keys():
   if (callsabove[caller] / 60   > 60):
      print'%s\t%d'% (caller, callsabove[caller] / 60)