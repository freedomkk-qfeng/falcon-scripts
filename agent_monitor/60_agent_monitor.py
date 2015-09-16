#!/usr/bin/python
#coding:utf-8
import requests
import time
import json
import copy
from multiprocessing.dummy import Pool as ThreadPool

hostlist = [
			{"endpoint":"endpoint1","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint2","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint3","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint4","url":"http://agent_host:1988/health"},
			{"endpoint":"endpoint5","url":"http://agent_host:1988/health"}
			]
push_url = "http://agent_host/v1/push"

#################################################################

payload = []
data = {"endpoint":"","metric":"agent.latency","timestamp":"","step":60,"value":"","counterType":"GAUGE","tags":""}

def main():
	time_start = time.clock()
	pool = ThreadPool(8)
	pool.map(push_payload,hostlist)
	pool.close()
	pool.join()
	#print time.clock()-time_start
	print json.dumps(payload)


def push_payload(host):
	ts = int(time.time())
	delay = agent_healh_delay(host["url"])
	data["endpoint"] = host["endpoint"]
	data["value"] = delay
	data["timestamp"] = ts
	payload.append(copy.copy(data))

	#r = requests.post(push_url, data=json.dumps(payload))

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
