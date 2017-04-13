from __future__ import print_function
import sys
import time
import grpc
import numbers_pb2
import numbers_pb2_grpc
from grpc._cython.cygrpc import CompressionAlgorithm
from grpc._cython.cygrpc import CompressionLevel


def run():
  numbers = [long(l.rstrip('\n\r')) for l in open(sys.argv[1],'r')]
  chan_ops = [('grpc.default_compression_algorithm', CompressionAlgorithm.none),
                ('grpc.grpc.default_compression_level', CompressionLevel.none)]
  channel = grpc.insecure_channel('localhost:50051', chan_ops)
  stub = numbers_pb2_grpc.SenderStub(channel)
  total_time = 0.0
  for x in range(1,10001):
    start = time.time()
    response = stub.SendNumbers(numbers_pb2.Numbers(n=numbers))
    end = time.time()
    total_time += (end - start)

  total_time = total_time/10000
  print(total_time)

if __name__ == '__main__':
  run()
