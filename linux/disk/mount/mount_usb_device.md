# Mount USB Device
## Find the usb storage's bus and port
First identify the device using:
``` sh
lsusb --tree
```
Somewhere `Mass Storage` or `Storage` will be mentionned

Note - if `lsusb` is not available, please read the next section. An alternative is mentionned.

Several information must be noted here:
- the `bus` number
- the `port number`
- any other `subport`

An excerpt of the generated output is as followed:
``` sh
Bus 03.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/12p, 480M
    |__ Port 1: Dev 2, If 0, Class=Wireless, Driver=btusb, 12M
    |__ Port 1: Dev 2, If 1, Class=Wireless, Driver=btusb, 12M
    |__ Port 3: Dev 3, If 0, Class=Video, Driver=uvcvideo, 480M
    |__ Port 3: Dev 3, If 1, Class=Video, Driver=uvcvideo, 480M
    |__ Port 4: Dev 14, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 1: Dev 15, If 0, Class=Mass Storage, Driver=usb-storage, 480M
        |__ Port 4: Dev 16, If 0, Class=Human Interface Device, Driver=usbhid, 12M
```
What matters to identify the usb storage unit here is:
- bus == 3
- port == 4
- subport == 1

Note - If it is hard to identify which device is which, unplug the device, run `lsusb` then plug
it and run `lsusb`. Do the diff.

## List connected usb storage (block) devices
``` sh
ls -l /sys/dev/block | grep usb
```

A list such as the following will be printed:
```
->  ls -l /sys/dev/block | grep usb
lrwxrwxrwx 1 root root 0 Oct  2 15:40 8:0 -> ../../devices/pci0000:00/0000:00:14.0/usb3/3-4/3-4.1/3-4.1:1.0/host0/target0:0:0/0:0:0:0/block/sda
lrwxrwxrwx 1 root root 0 Oct  2 15:40 8:1 -> ../../devices/pci0000:00/0000:00:14.0/usb3/3-4/3-4.1/3-4.1:1.0/host0/target0:0:0/0:0:0:0/block/sda/sda1
```
What's important to notice here is twofold:
- usb3/3-4/3-4.1 stands for `usb3 standard`, on `bus 3`, `port 4`, `port 1` (because device is a hub here)
- corresponding block device in `/dev` is `sda1`

This is the same information found with `lsusb` therefore `sda1` corresponds to the connected usb device that is looked for.

Note - if `lsusb` is not available, the device name can be found in `3-4.1/manufacturer` and `3-4.1/product`.

## Mount the device
``` sh
sudo mount /dev/sda1 /mnt
```
Note - /mnt must exist to do so.


