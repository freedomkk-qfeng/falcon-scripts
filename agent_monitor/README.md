agent 监控脚本
================================

依赖
--------------------------------
python >= 2.6

[requests](https://pypi.python.org/pypi/requests)

工作逻辑
--------------------------------
http 请求 agent 的 health 接口 (http://agent:1988/health)

返回 http 连接的延迟作为参数上报。

##### 上报字段 #####

| key |  tag | type | note |
|-----|------|------|------|
|agent.latency|/|GAUGE|从脚本服务器到 agent 的延迟|

当 http 请求异常时，则 agent.latency 上报为 -1 。可以在 portal 内对此进行告警。

使用方式1
--------------------------------
1. 根据实际部署情况，修改脚本开头的配置参数
2. 测试： python agent_monitor.py
3. 丢进 crontab 任务完事

使用方式2
--------------------------------
1. 根据实际部署情况，修改脚本开头的配置参数
2. 测试： python 60_agent_monitor.py
3. 开启脚本所在服务器 agent 的 plugin,并将脚本放入 agent 的 plugin 中。详见[plugin 的机制](http://book.open-falcon.com/zh/philosophy/plugin.html)

