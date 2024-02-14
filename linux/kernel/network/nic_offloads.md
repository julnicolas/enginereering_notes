# NIC Offloads
source: red hat
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/performance_tuning_guide/network-nic-offloads

The default Ethernet maximum transfer unit (MTU) is 1500 bytes, 
which is the largest frame size that can usually be transmitted. 
This can cause system resources to be underutilized, for example, 
if there are 3200 bytes of data for transmission, it would 
mean the generation of three smaller packets. There are several options, 
called offloads, which allow the relevant protocol stack to transmit 
packets that are larger than the normal MTU. Packets as large 
as the maximum allowable 64KiB can be created, with options for 
both transmitting (Tx) and receiving (Rx). When sending or receiving 
large amounts of data this can mean handling one large packet as opposed 
to multiple smaller ones for every 64KiB of data sent or received. This 
means there are fewer interrupt requests generated, less processing overhead 
is spent on splitting or combining traffic, and more opportunities for 
transmission, leading to an overall increase in throughput. 

## Offload Types
### TCP Segmentation Offload (TSO)
Uses the TCP protocol to send large packets. Uses the NIC 
to handle segmentation, and then adds the TCP, IP and 
data link layer protocol headers to each segment

### UDP Fragmentation Offload (UFO)
Uses the UDP protocol to send large packets. Uses the NIC 
to handle IP fragmentation into MTU sized packets for large UDP 
datagrams. 

### Generic Segmentation Offload (GSO)
Uses the TCP or UDP protocol to send large packets. If 
the NIC cannot handle segmentation/fragmentation, GSO performs the same 
operations, bypassing the NIC hardware. This is achieved by delaying 
segmentation until as late as possible, for example, when the 
packet is processed by the device driver. 

### Large Receive Offload (LRO)
Uses the TCP protocol. All incoming packets are re-segmented 
as they are received, reducing the number of segments the system 
has to process. They can be merged either in the driver 
or using the NIC. A problem with LRO is that it 
tends to resegment all incoming packets, often ignoring differences in 
headers and other information which can cause errors. It is generally not 
possible to use LRO when IP forwarding is enabled. LRO in 
combination with IP forwarding can lead to checksum errors. Forwarding is 
enabled if /proc/sys/net/ipv4/ip_forward 
is set to 1. 

### Generic Receive Offload (GRO)
Uses either the TCP or UDP protocols. GRO is more rigorous 
than LRO when resegmenting packets. For example it checks the MAC 
headers of each packet, which must match, only a limited 
number of TCP or IP headers can be different, and the 
TCP timestamps must match. Resegmenting can be handled by either the 
NIC or the GSO code. 

## Using NIC Offloads
Offloads should be used on high speed systems that transmit or receive 
large amounts of data and favor throughput over latency. Because using 
offloads greatly increases the capacity of the driver queue, latency can 
become an issue. An example of this would be a system 
transferring large amounts of data using large packet sizes, but is 
also running lots of interactive applications. Because interactive 
applications send small packets at timed intervals there is a very real 
risk that those packets may become 'trapped' in the buffer while larger 
packets in front of them are processed, causing unacceptable latency.
To check current offload settings use the ethtool command. Some device 
settings may be listed as fixed, meaning they cannot be changed.
Command syntax: ethtool -k ethernet_device_name 

