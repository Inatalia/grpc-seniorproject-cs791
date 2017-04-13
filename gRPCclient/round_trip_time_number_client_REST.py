import urllib2
import json
import sys
import time

def run():
  payload = ''
  with open(sys.argv[1]) as json_data:
    payload = json.load(json_data)

  url = 'http://localhost:8080/rest/numbers'
  req = urllib2.Request(url)
  req.add_header('Content-Type','application/json')
  data = json.dumps(payload)
  
  total_time = 0.0
  for x in range(1,10001):
    start = time.time()
    response = urllib2.urlopen(req,data)
    end = time.time()
    total_time += (end - start)
  
  total_time = total_time/10000
  print(total_time)

if __name__ == '__main__':
  run()
