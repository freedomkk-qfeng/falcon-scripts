import requests
import time
import json
from multiprocessing.dummy import Pool as ThreadPool

hostlist = [
			{"endpoint":"endpoint1","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint2","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint3","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint4","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint5","url":"http://agent_host:1988/health"}]
push_url = "http://agent_host/v1/push"

#################################################################

def main():
	time_start = time.clock()
	pool = ThreadPool(8)
	pool.map(push_payload,hostlist)
	pool.close()
	pool.join()
	#print time.clock()-time_start


def push_payload(host):
	ts = int(time.time())
	delay = agent_healh_delay(host["url"])
	payload = [{"endpoint":host["endpoint"],"metric":"agent.delay","timestamp":ts,"step":60,"value":delay,"counterType":"GAUGE","tags":""}]
	#print json.dumps(payload,indent=4)
	r = requests.post(push_url, data=json.dumps(payload))

def agent_healh_delay(url):
	result = -1
	try:
		r = requests.get(url,timeout=3)
		if r.status_code == 200:
			result = r.elapsed.microseconds/1000
			return result
	except Exception,e:
		return result

if __name__ == '__main__':
	main()
