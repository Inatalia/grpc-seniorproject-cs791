#!/usr/bin/python

import time as t
import os
#import grpc
#import helloworld_pb2

def runClient():
  os.system("python greeter_client.py >> /dev/null")

times = []

for n in range( 0 , 7):
  start = t.time()
  runClient()
  end = t.time()
  times.append(end-start)

sum = 0.0
for n in range(0, len(times)):
  sum += times[n]
  print(times[n])
print(sum/len(times))
