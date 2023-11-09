# Difference between FAT32 and FAT32 LBA
The difference between FAT32 (hex code b in fdisk) and FAT32 (LBA) (hex code c in fdisk).

FAT 32 is for Win95 OSR2 Fat32 with a partition up to 2047Mb and Type c is for LBA-mapped capable of 2Tb size. The type b is for the early Win95 system and type c is for later Win95 and all Win98.

So if someone wants to use FAT32 for an usb.stick, which still makes sense when you want to exchange data with Macs, use hex code c in fdisk, and not b.

source - linuxquestions.com
