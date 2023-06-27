# Nowatchdog
Watchdogs are hardware or software implemented timers used by servers or embeeded devices to recover from certain
machine states. The watchdog daemon (`[watchdogd]`) is a kernel process, as such it is able to periodically collect
kernel information and react upon established state.

Watchdogs are useful  for machines without human supervision (such as servers and embeeded devices) but not necessary
for desktops or laptops (as supervised by humans). Disabling them can speed up  boot and shutdown steps.

To disable the use of software and hardware watchdogs, provide the following CLI boot parameter to your `boot loader`
(i.e. grub):
``` sh
nowatchdog
```

*IMPORTANT:* Some hardware implement additional watchdogs. If some additional piece of hardware does so,
their watchdog must be individually disabled using constructors' configuration (or disabling some constructor-related
kernel modules). Known manufacturers are `ATI` who implement them for their GPU.
