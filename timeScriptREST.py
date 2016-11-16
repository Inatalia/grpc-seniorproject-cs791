#!/usr/bin/python

import time as t
import os

times = []

for n in range( 0 , 9999):
  start = t.time()
  os.system("curl -silent localhost:8080/rest/hello/intextform >> /dev/null")
  end = t.time()
  times.append(end-start)

sum = 0.0
for n in range(0, len(times)):
  sum += times[n]
print(sum/len(times))
print("For ", len(times)," k")
