from concurrent import futures
import time
import grpc
import unicode_pb2
import unicode_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Sender(unicode_pb2_grpc.SenderServicer):

  def SendUnicode(self, request, context):
    for x in request.n:
      print x,
    return unicode_pb2.Confirmation(message='Data Received')


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  unicode_pb2_grpc.add_SenderServicer_to_server(Sender(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
