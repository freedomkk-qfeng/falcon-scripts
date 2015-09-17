bind9 监控插件
================================

依赖
--------------------------------
python >= 2.6

工作逻辑
--------------------------------
分析处理 bind9 的 named_stats.txt 文件来生成上报数据

##### 上报字段 #####

在 dns 服务器上运行 rndc stats，然后访问 named_stats.txt （默认路径是"/var/named/data/named_stats.txt")

上报字段基本照搬此文件，根据++ xxxx ++ 的内容打 tag。

例如
++ Incoming Queries ++
           199590680 A

则上报为 A/tag=Incoming_Queries

++ Outgoing Queries ++
            54927599 A
则上报为 A/tag=Outgoing Queries



使用方式
--------------------------------
1. 根据实际部署情况，修改脚本开头的配置参数
2. 测试： python 60_named_stats.py
3. 开启脚本所在服务器 agent 的 plugin,并将脚本放入 agent 的 plugin 中。详见[plugin 的机制](http://book.open-falcon.com/zh/philosophy/plugin.html)

