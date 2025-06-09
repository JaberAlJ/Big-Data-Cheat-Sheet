#!/usr/bin/python
import sys

prev_word = None
prev_count = 0
word = None


for line in sys.stdin:
   line = line.strip()            
   word, count = line.split('\t') 
   count = int(count)             

   if word == prev_word:
      prev_count += count
   else:
      if prev_word:
         print('{0}\t{1}'.format(prev_word, prev_count))
      prev_word = word
      prev_count = count


if prev_word == word:	
   print('{0}\t{1}'.format(prev_word, prev_count))
