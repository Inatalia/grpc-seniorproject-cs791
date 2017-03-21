from __future__ import print_function
import sys
import grpc
import unicode_pb2
import unicode_pb2_grpc

def run():
  _unicode = ''
  for l in open(sys.argv[1],'r'):
    _unicode = _unicode + unicode(l)
  channel = grpc.insecure_channel('localhost:50051')
  stub = unicode_pb2_grpc.SenderStub(channel)
  response = stub.SendUnicode(unicode_pb2.Unicode(n=_unicode))
  print("Status: " + response.message)

if __name__ == '__main__':
  run()
