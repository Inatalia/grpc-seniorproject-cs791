from __future__ import print_function
import sys
import grpc
import numbers_pb2
import numbers_pb2_grpc

def run():
  numbers = [long(l.rstrip('\n\r')) for l in open(sys.argv[1],'r')]
  channel = grpc.insecure_channel('localhost:50051')
  stub = numbers_pb2_grpc.SenderStub(channel)
  response = stub.SendNumbers(numbers_pb2.Numbers(n=numbers))
  print("Status: " + response.message)

if __name__ == '__main__':
  run()
