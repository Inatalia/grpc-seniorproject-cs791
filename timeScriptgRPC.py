#!/usr/bin/python

import time as t
import os
import grpc
#import helloworld_pb2

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2.GreeterStub(channel)
  response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))

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
