#!/usr/bin/python

import time as t
import os
#import grpc
#import helloworld_pb2

def run():
  os.system("grpc/example/helloworld/python greeter-client.py >> /dev/null")

times = []

for n in range( 0 , 9):
  start = t.time()
  run()
  end = t.time()
  times.append(end-start)

sum = 0.0
for n in range(0, len(times)):
  sum += times[n]
print(sum/len(times))
print("For ", len(times)," k")
