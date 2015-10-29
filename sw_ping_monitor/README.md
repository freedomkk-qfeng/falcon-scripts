交换机的存活监控脚本
================================

nodata已经发布了，建议使用官方的nodata来做存活判断。

依赖
--------------------------------
python >= 2.6

[ping](https://pypi.python.org/pypi/ping)

ping 非常小，就一个文件几百行，也可以不安装直接引用。

工作逻辑
--------------------------------
ping 交换机，返回丢包率（ping 10 个包）

##### 上报字段 #####

| key |  tag | type | note |
|-----|------|------|------|
|switch.pkt.lost.percent|/|GAUGE|丢包率|

可以根据丢包率来告警。

使用方式
--------------------------------
1. 根据实际部署情况，修改脚本开头的配置参数
2. 测试： python 60_sw_ping_monitor.py
3. 开启脚本所在服务器 agent 的 plugin,并将脚本放入 agent 的 plugin 中。详见[plugin 的机制](http://book.open-falcon.com/zh/philosophy/plugin.html)

