# Trap a signal

Trapping a signal means catch it then call a handler to do some action.

Here is an example to trap `SIGUSR1`:
``` sh
hello() {
    echo "hello"
}
trap hello SIGUSR1
```

Now check this all work:
``` sh
# Sends SIGUSR1 to kill's parent which is the shell
kill -SIGUSR1 $$
```
