# List Disk Partitions
``` sh
fdisk -l
```

*Important:* `fdisk` generally requires high priviledges, `lsblk` retrieves less information
but is less likely to require root access (this is the case with a default arch install).

