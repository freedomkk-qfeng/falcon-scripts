#!/usr/bin/python
#coding:utf-8
import json
import copy
import time
import os

endpoint = "bind9"
name_stats_path = "/var/named/data/named_stats.txt"

def main():
	if os.path.isfile(name_stats_path):
		os.remove(name_stats_path)
	os.system("rndc stats")

	ts = int(time.time())
	payload = []
	data = {"endpoint":endpoint,"metric":"","timestamp":ts,"step":60,"value":"","counterType":"COUNTER","tags":""}

	f = open(name_stats_path)

	for line in f:
		if "++ Incoming Requests ++" in line:
			data["tags"] = "tag=Incoming_Requests"
			continue
		elif "++ Incoming Queries ++" in line:
			data["tags"] = "tag=Incoming_Queries"
			continue
		elif "++ Outgoing Queries ++" in line:
			data["tags"] = "tag=Outgoing_Queries"
			continue
		elif "++ Name Server Statistics ++" in line:
			data["tags"] = "tag=Name_Server_Statistics"
			continue
		elif "++ Zone Maintenance Statistics ++" in line:
			data["tags"] = "tag=Zone_Maintenance_Statistics"
			continue
		elif "++ Resolver Statistics ++" in line:
			data["tags"] = "tag=Resolver_Statistics"
			continue
		elif "++ Cache DB RRsets ++" in line:
			data["tags"] = "tag=Cache DB RRsets"
			continue
		elif "++ Socket I/O Statistics ++" in line:
			data["tags"] = "tag=Socket_I/O_Statistics"
			continue
		named_stats = line.strip().split(' ')
		if named_stats[0].isdigit() != True:
			continue
		data["value"] = named_stats[0]
		data["metric"] = string_join(named_stats)
		payload.append(copy.copy(data))

	os.remove(name_stats_path)
	print json.dumps(payload,indent=4)

def string_join(split_list):
	num = 0
	join_str = split_list[1]
	for string in split_list:
		num = num + 1
		if num <= 2:
			continue
		join_str = join_str + "_" + string
	return join_str

if __name__ == "__main__":
	main()
