# Cloudera_Manager_API_dev

Cloudera Manager API：http://cloudera.github.io/cm_api/docs/python-client/

1、cm_monitor：基于Cloudera Manager API对CDH集群的资源使用情况进行统计记录并作可视化分析。

    集群环境：CDH 5.7.3  API：cm-api
    #install the Python API client
    $ git clone git://github.com/cloudera/cm_api.git
    $ cd cm_api/python
    $ sudo python setup.py install
    
    利用api的时间序列查询query_timeseries()函数记录整个集群的CPU、内存、存储及YARN资源池的CPU、内存在过去12个小时的使用情况，通过定时任务执行，实现集群资源使用情况的全记录，数据粒度为10分钟取一个点；利用matplotlib对统计的结果进行可视化展示。
    
    通过可视化展示，能够直观地发现集群资源的使用异常点，进而发现集群运行过程中异常状况，实现故障跟踪及故障排查；此外，通过跟踪监控集群资源使用情况可为资源扩容、采购，提供数据支撑。
