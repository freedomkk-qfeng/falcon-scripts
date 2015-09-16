windows 监控脚本
================================

依赖
--------------------------------
python >= 2.6

[requests](https://pypi.python.org/pypi/requests)

上报字段
--------------------------------
| key |  tag | type | note |
|-----|------|------|------|
|agent.delay|/|GAUGE|从脚本服务器到 agent 的延迟|

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

