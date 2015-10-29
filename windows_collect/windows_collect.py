#coding=utf8
import psutil
import time
import json
import requests
import copy


cpu_interval = 60
push_interval = 300
zh_decode = "gbk"
endpoint = "YOUR_HOSTNAME"
ignore_interface = ["Loopback","Teredo Tunneling","isatap","6TO4 Adapter"]
push_url = "http://agent_host:1988/v1/push"

#######################################################

def main():

	ts = int(time.time())
	payload = []
	data = {"endpoint":endpoint,"metric":"","timestamp":ts,"step":push_interval,"value":"","counterType":"","tags":""}


	cpu_status = psutil.cpu_times_percent(interval=cpu_interval)
	mem_status = psutil.virtual_memory()
	swap_status = psutil.swap_memory()
	disk_io_status = psutil.disk_io_counters(perdisk=True)
	net_io_status = psutil.net_io_counters(pernic=True)

	data["metric"] = "cpu.user"
	data["value"] = cpu_status.user
	data["counterType"] = "GAUGE"
	payload.append(copy.copy(data))

	data["metric"] = "cpu.system"
	data["value"] = cpu_status.system
	payload.append(copy.copy(data))

	data["metric"] = "cpu.idle"
	data["value"] = cpu_status.idle
	payload.append(copy.copy(data))

	data["metric"] = "mem.memused.percent"
	data["value"] = mem_status.percent
	payload.append(copy.copy(data))

	data["metric"] = "mem.swapused.percent"
	data["value"] = swap_status.percent
	payload.append(copy.copy(data))

	disk_status = psutil.disk_partitions()
	for disk in disk_status:
		if 'cdrom' in disk.opts or disk.fstype == '':
			continue
		disk_info = psutil.disk_usage(disk.mountpoint)

		data["metric"] = "df.used.percent"
		data["value"] = disk_info.percent
		data["tags"] = "disk=" + disk.device.split(":")[0]
		payload.append(copy.copy(data))
		
		data["metric"] = "df.byte.total"
		data["value"] = disk_info.total
		payload.append(copy.copy(data))
		
		data["metric"] = "df.byte.used"
		data["value"] = disk_info.used
		payload.append(copy.copy(data))
		
		data["metric"] = "df.byte.free"
		data["value"] = disk_info.free
		payload.append(copy.copy(data))


	for key in disk_io_status:
		#print "device_name = %s" % key
		data["metric"] = "disk.io.read_count"
		data["value"] = disk_io_status[key].read_count
		data["tags"] = "device=" + key
		data["counterType"] = "COUNTER"
		payload.append(copy.copy(data))
		
		data["metric"] = "disk.io.write_count"
		data["value"] = disk_io_status[key].write_count
		payload.append(copy.copy(data))
		
		data["metric"] = "disk.io.read_bytes"
		data["value"] = disk_io_status[key].read_bytes
		payload.append(copy.copy(data))
		
		data["metric"] = "disk.io.write_bytes"
		data["value"] = disk_io_status[key].write_bytes
		payload.append(copy.copy(data))
		
		data["metric"] = "disk.io.read_time"
		data["value"] = disk_io_status[key].read_time
		payload.append(copy.copy(data))
		
		data["metric"] = "disk.io.write_time"
		data["value"] = disk_io_status[key].write_time
		payload.append(copy.copy(data))

	for key in net_io_status:
		if is_interface_ignore(key) == True:
			continue

		data["metric"] = "net.if.in.bytes"
		data["value"] = net_io_status[key].bytes_recv
		data["tags"] = "interface=" + key.decode(zh_decode)
		payload.append(copy.copy(data))
		
		data["metric"] = "net.if.out.bytes"
		data["value"] = net_io_status[key].bytes_sent
		payload.append(copy.copy(data))
		
		data["metric"] = "net.if.in.packets"
		data["value"] = net_io_status[key].packets_recv
		payload.append(copy.copy(data))
		
		data["metric"] = "net.if.out.packets"
		data["value"] = net_io_status[key].packets_sent
		payload.append(copy.copy(data))
		
		data["metric"] = "net.if.in.error"
		data["value"] = net_io_status[key].errin
		payload.append(copy.copy(data))
		
		data["metric"] = "net.if.out.error"
		data["value"] = net_io_status[key].errout
		payload.append(copy.copy(data))
		
		data["metric"] = "net.if.in.drop"
		data["value"] = net_io_status[key].dropin
		payload.append(copy.copy(data))
		
		data["metric"] = "net.if.out.drop"
		data["value"] = net_io_status[key].dropout
		payload.append(copy.copy(data))
	#print json.dumps(payload,indent=4)
	r = requests.post(push_url, data=json.dumps(payload))
	#print r.text

def is_interface_ignore(key):
	for ignore_key in ignore_interface:
		if ignore_key in key:
			return True

if __name__ == "__main__":
	main()
