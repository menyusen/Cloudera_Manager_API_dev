# Get a handle to the API client
from cm_api.api_client import ApiResource
import time
from datetime import datetime, timedelta

cm_host = "x.x.x.x"
api = ApiResource(cm_host, username="admin", password="xxxxxx")

# Basic Usage
#Get a list of all clusters
cdh = None
for c in api.get_all_clusters():
  print c.name

#Getting Metrics
#Timeseries information
#print time.time()
from_time = datetime.fromtimestamp(time.time() - 3600*12)
to_time = datetime.fromtimestamp(time.time())
print datetime.now()

#total_physical_memory_used monitoring data
f_memory = open("./data/total_physical_memory_used.out", 'a+w') 
query_memory = "SELECT total_physical_memory_used_across_hosts WHERE entityName = \"1\" AND category = CLUSTER"
result1 = api.query_timeseries(query_memory, from_time, to_time)
ts_list1 = result1[0]
for ts1 in ts_list1.timeSeries:
  print "--- %s: %s ---" % (ts1.metadata.entityName, ts1.metadata.metricName)
  for point1 in ts1.data:
    dt1 = point1.timestamp + timedelta(hours=8)
    print >> f_memory,"%s\t%s" % (dt1, point1.value/1024/1024/1024/1024)
f_memory.close()
print "Memory monitoring data in the last 12 hours written"

#cpu_percent_used monitoring data
f_cpu = open("./data/cpu_percent_used.out", 'a+w')
query_cpu = "select cpu_percent_across_hosts where category = CLUSTER"
result2 = api.query_timeseries(query_cpu, from_time, to_time)
ts_list2 = result2[0]
for ts2 in ts_list2.timeSeries:
  print "--- %s: %s ---" % (ts2.metadata.entityName, ts2.metadata.metricName)
  for point2 in ts2.data:
    dt2 = point2.timestamp + timedelta(hours=8)
    print >> f_cpu,"%s\t%s" % (dt2, point2.value)
f_cpu.close()
print "CPU monitoring data in the last 12 hours written"

#capacity_used monitoring data
f_capacity = open("./data/capacity_used.out", 'a+w')
query_capacity = "select dfs_capacity_used + dfs_capacity_used_non_hdfs where entityName=hdfs:nameservice1"
result3 = api.query_timeseries(query_capacity, from_time, to_time)
ts_list3 = result3[0]
for ts3 in ts_list3.timeSeries:
  print "--- %s: %s ---" % (ts3.metadata.entityName, ts3.metadata.metricName)
  for point3 in ts3.data:
    dt3 = point3.timestamp + timedelta(hours=8)
    print >> f_capacity,"%s\t%s" % (dt3, point3.value/1024/1024/1024/1024/1024)
f_capacity.close()
print "Capacity monitoring data in the last 12 hours written"

#Memory Usage of YARN_POOL monitoring data
f_memory = open("./data/yarn_memory_used.out", 'a+w')
query_memory = "SELECT allocated_memory_mb_cumulative where category=YARN_POOL and serviceName=yarn and queueName=root"
result1 = api.query_timeseries(query_memory, from_time, to_time)
ts_list1 = result1[0]
for ts1 in ts_list1.timeSeries:
  print "--- %s: %s ---" % (ts1.metadata.entityName, ts1.metadata.metricName)
  for point1 in ts1.data:
    dt1 = point1.timestamp + timedelta(hours=8)
    print >> f_memory,"%s\t%s" % (dt1, point1.value/1024/1024)
f_memory.close()
print "YARN memory monitoring data in the last 12 hours written"


#YARN cpu_used monitoring data
f_cpu = open("./data/yarn_cpu_used.out", 'a+w')
query_cpu = "SELECT allocated_vcores_cumulative where category=YARN_POOL and serviceName=yarn and queueName=root"
result2 = api.query_timeseries(query_cpu, from_time, to_time)
ts_list2 = result2[0]
for ts2 in ts_list2.timeSeries:
  print "--- %s: %s ---" % (ts2.metadata.entityName, ts2.metadata.metricName)
  for point2 in ts2.data:
    dt2 = point2.timestamp + timedelta(hours=8)
    print >> f_cpu,"%s\t%s" % (dt2, point2.value)
f_cpu.close()
print "YARN CPU monitoring data in the last 12 hours written"
