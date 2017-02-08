#!/usr/bin/python
import threading

ITERATIONS = 12
THREADNUMBER = 8
times = []
for x in range(0,ITERATIONS):
  times.append([])
  for n in range(0,THREADNUMBER):
    times[x].append([])

f = open('results.txt','w')

def work(tid, iid, numberOfIterations, timesRef):
  import time as t
  import os
  localTimes = []
  for n in range( 0 , numberOfIterations):
    start = t.time()
    os.system("python greeter_client.py >> /dev/null")
    end = t.time()
    localTimes.append(end-start)
  timesRef[iid][tid] = localTimes

for n in range(0,ITERATIONS):
  threads = []
  for i in range(0,THREADNUMBER):
    t = threading.Thread(target=work, args=(i,n,2**n,times))
    threads.append(t)
  for x in threads:
     x.start()
  for x in threads:
     x.join()
  f.write("Iteration number " + str(n) + " : " + str(THREADNUMBER*(2**n)) + " total times\n")
  for x in range(0,THREADNUMBER):
    for y in range(0,len(times[n][x])):
      f.write( str(times[n][x][y])+ "\n")

f.close()
