# Tugas 7

## Performance Test

[Server yang ditest](../tugas6/server_thread_http.py)

### Keluaran Hasil

| No test | Concurrency level | Time taken for test (seconds) | Complete request | Failed request | Total transferred (bytes) | Request per second | Time per request (ms) | Transfer rate (Kbytes/sec) |
|:-------:|:-----------------:|:-----------------------------:|:----------------:|:--------------:|:-------------------------:|:------------------:|:---------------------:|:--------------------------:|
|    1    |         1         |             0.196             |        10        |        0       |            1360           |       51.06       |         19.584         |            6.78           |
|    2    |         5         |             0.191             |        10        |        0       |            1360           |        52.32       |         95.558        |            6.95            |
|    3    |         10         |             0.742             |        10       |        0       |           1360           |        13.47       |         742.357        |            1.79            |
|    4    |         1         |             24.119             |        50       |        0       |           6800           |        2.07       |         482.371        |            0.28            |
|    5    |         10         |             0             |        50       |        0       |           0           |        0       |         0        |            0            |
|    6    |         30         |             0             |        50       |        0       |           0           |        0       |         0        |            0            |
|    7    |         50         |             0             |        50       |        0       |           0           |        0       |         0        |            0            |
|    8    |         1         |             36.121             |        100       |        0       |           13600           |        2.77       |         361.208        |            0.37            |
|    9    |         10         |             0             |        100       |        0       |           0           |        0       |         0        |            0            |
|    10    |         50         |             0             |        100       |        0       |           0           |        0       |         0        |            0            |
|    11    |         100         |             0             |        100       |        0       |           0           |        0       |         0        |            0            |

### Screenshot

- `ab -n 10 -c 1 http://127.0.0.1:10001/`  
![1](foto/1.png)
- `ab -n 10 -c 5 http://127.0.0.1:10001/`  
![2](foto/2.png)
- `ab -n 10 -c 10 http://127.0.0.1:10001/`  
![3](foto/3.png)
- `ab -n 50 -c 1 http://127.0.0.1:10001/`  
![4](foto/4.png)
- `ab -n 50 -c 10 http://127.0.0.1:10001/`
![5](foto/error.png)
- `ab -n 50 -c 30 http://127.0.0.1:10001/`
![6](foto/error.png)
- `ab -n 50 -c 50 http://127.0.0.1:10001/`
![7](foto/error.png)
- `ab -n 100 -c 1 http://127.0.0.1:10001/`
![8](foto/8.png)
- `ab -n 100 -c 10 http://127.0.0.1:10001/`
![9](foto/error.png)
- `ab -n 100 -c 50 http://127.0.0.1:10001/`
![10](foto/error.png)
- `ab -n 100 -c 100 http://127.0.0.1:10001/`
![11](foto/error.png)
