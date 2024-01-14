# Filter Out System Calls
``` sh
strace -p $SOME_PID -e 'trace=!full_syscall_name'
```

Example of system calls:
- `clock_nanosleep`

as in:
```clock_nanosleep(CLOCK_REALTIME, 0, {tv_sec=0, tv_nsec=50000000}, 0x7ffe4d69cf80) = 0
```

