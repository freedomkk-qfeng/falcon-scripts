windows 监控脚本
================================

依赖
--------------------------------
python >= 2.6
[psutil](https://pypi.python.org/pypi/psutil)
[request](https://pypi.python.org/pypi/requests)

上报字段
--------------------------------
| key |  tag | type | note |
|-----|------|------|------|
|cpu.user|/|GAUGE|CPU user 使用百分比|
|cpu.system|/|GAUGE|CPU system 使用百分比|
|cpu.idle|/|GAUGE|CPU 空闲百分比|
|mem.memused.percent|/|GAUGE|内存使用百分比 |
|mem.swapused.idle|/|GAUGE|swap 使用百分比|
|df.free.percent|disk.device|GAUGE|分区剩余空间百分比|
|df.byte.total|disk|GAUGE|分区总容量|
|df.byte.used|disk|GAUGE|分区使用量|
|df.byte.free|disk|GAUGE|分区剩余量|
|disk.io.read_count|device|counter|磁盘读 IO count|
|disk.io.write_count|device|counter|磁盘写 IO count|
|disk.io.read_bytes|device|counter|磁盘读 IO bytes|
|disk.io.write_bytes|device|counter|磁盘写 IO bytes|
|disk.io.read_time|device|counter|磁盘读 IO time|
|disk.io.write_time|device|counter|磁盘写 IO time|
|net.if.in.bytes|interface|counter|网卡进流量|
|net.if.out.bytes|interface|counter|网卡出流量|
|net.if.in.packets|interface|counter|网卡进包数|
|net.if.out.packets|interface|counter|网卡出包数|
|net.if.in.error|interface|counter|网卡进错包数|
|net.if.out.error|interface|counter|网卡出错包数|
|net.if.in.drop|interface|counter|网卡进弃包数|
|net.if.in.drop|interface|counter|网卡出弃包数|


使用方式
--------------------------------
1. 根据实际部署情况，修改脚本开头的配置参数
2. 测试： python windows_collect.py
3. 丢进 windows 计划任务完事
