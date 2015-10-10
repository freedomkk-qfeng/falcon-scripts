#!/usr/bin/python
#coding:utf-8
import time
import json
import copy
import ping
from multiprocessing.dummy import Pool as ThreadPool

hostlist = ['10.10.10.1','10.10.11.2','10.10.31.1','10.10.41.1','10.10.55.1','10.10.23.1','10.100.9.2','202.120.95.245']

#################################################################

payload = []
data = {"endpoint":"","metric":"switch.pkt.lost.percent","timestamp":"","step":60,"value":"","counterType":"GAUGE","tags":""}

def main():
	#time_start = time.clock()
	pool = ThreadPool(8)
	pool.map(get_payload,hostlist)
	pool.close()
	pool.join()
	#print time.clock()-time_start
	print json.dumps(payload,indent=4)


def get_payload(host):
	ts = int(time.time())
	pkt_lost_percent = switch_pkt_lost(host)
	data["endpoint"] = host
	data["value"] = pkt_lost_percent
	data["timestamp"] = ts
	payload.append(copy.copy(data))

def switch_pkt_lost(host):
	result = ping.quiet_ping(host,count=10)
	return result[0]

if __name__ == '__main__':
	main()
	
