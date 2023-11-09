# Create a FAT32 File System On A Partition
First download the right package. Shown example is for arch linux.
``` sh
pacman -S dosfstools
```

Then create the file system on the partition with:
``` sh
mkfs.fat -F 32 <path to partition>
```

