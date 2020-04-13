# Tugas 7

## Performance Test

[Server yang ditest](../tugas6/server_thread_http.py)

### Keluaran Hasil

| No test | Concurrency level | Time taken for test (seconds) | Complete request | Failed request | Total transferred (bytes) | Request per second | Time per request (ms) | Transfer rate (Kbytes/sec) |
|:-------:|:-----------------:|:-----------------------------:|:----------------:|:--------------:|:-------------------------:|:------------------:|:---------------------:|:--------------------------:|
|    1    |         1         |             1.426             |        10        |        0       |            1360           |       7.01       |         142.578         |            0.93           |
|    2    |         1         |             13.850             |        50        |        0       |            6800           |        3.61       |         277.005        |            0.48            |
|    3    |         1         |             158.380             |        100       |        0       |           13600           |        0.63       |         1583.795        |            0.08            |

### Screenshot

- `ab -n 10 -c 1,5,10 http://127.0.0.1:10001/`  
![1](foto/1.png)
- `ab -n 50 -c 1,10,30,50 http://127.0.0.1:10001/`  
![2](foto/2.png)
- `ab -n 100 -c 1,10,50,100 http://127.0.0.1:10001/`  
![3](foto/3.png)
