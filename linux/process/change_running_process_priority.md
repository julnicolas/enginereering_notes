# Change Running Process Priority

This commands change the priority of a running process using a set of integers.
Range goes to -20 (most favorable to the process) to 19 (least favorable).
Default value is 10.

``` sh
renice -n 15 -p $SOME_PID
```
