# v0.3.2更新

## 对股票分时成交数据获取模块的重构

之前采取的方案是在存储过程中通过传入表名参数选择对应表进行存储，其实这样的业务逻辑不应该写在数据库部分，而应该写在我们的应用程序里面，所以我们对此进行重构，同时采用批量存储来实现加速。

针对同时爬取300支股票数据

修改前

```
[INFO] [2024-05-09 10:57:23,477] [20240509105713404842-2913da0e-ce3c-4671-a0d7-421702fe5d1b] [30008:39048] - [job_executor.run_a_job] [line:36]: Job success finished: Job(job_id=20240509105713404842-2913da0e-ce3c-4671-a0d7-421702fe5d1b)
[INFO] [2024-05-09 10:57:23,477] [20240509105713404842-2913da0e-ce3c-4671-a0d7-421702fe5d1b] [30008:39048] - [job_executor.run_a_job] [line:41]: Thread id 39048 end to run job: Job(job_id=20240509105713404842-2913da0e-ce3c-4671-a0d7-421702fe5d1b)
[INFO] [2024-05-09 10:57:23,477] [server] [30008:39048] - [job_executor.run] [line:58]: JobExecutor 0:39048 finished a job: Job(job_id=20240509105713404842-2913da0e-ce3c-4671-a0d7-421702fe5d1b), time cost: 10.070843499999999
```


修改后

```
[INFO] [2024-05-09 15:33:00,316] [server] [42540:40276] - [job_executor.run] [line:72]: JobExecutor 1:40276 finished a job: Job(job_id=20240509153256520531-42d5ff85-cde1-432e-b475-d5c556e5c115), time cost: 3.7919138000000014
```

## logger模块bug修复

修复了logger handlers 不能正确删除的问题

