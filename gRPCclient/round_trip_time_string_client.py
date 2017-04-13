from __future__ import print_function
import sys
import time
import grpc
import grpc
import unicode_pb2
import unicode_pb2_grpc




def run():
  _unicode = ''
  for l in open(sys.argv[1],'r'):
    _unicode = _unicode + unicode(l, 'utf-8')
  channel = grpc.insecure_channel('localhost:50051')
  stub = unicode_pb2_grpc.SenderStub(channel)
  total_time = 0.0
  #for x in range(1,10):
  start = time.time()
  response = stub.SendUnicode(unicode_pb2.Unicode(n=_unicode))
  end = time.time()
  total_time += (end - start)

  total_time = total_time/10000
  print(total_time)

if __name__ == '__main__':
  run()
