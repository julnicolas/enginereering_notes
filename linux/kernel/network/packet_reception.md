# Overview of Packet Reception
source: redhat

To better analyze network bottlenecks and performance issues, you 
need to understand how packet reception works. Packet reception 
is important in network performance tuning because the receive path 
is where frames are often lost. Lost frames in the receive path 
can cause a significant penalty to network performance. 

```
 NIC ----> hard IRQ --> soft IRQ --> app socket queue ---> app
- NIC--|------------------ CPU --------------------------------
       |------------- Kernel ---------------|--- User Space ---
```
Figure 8.1. Network receive path diagram

The Linux kernel receives each frame and subjects it to 
a four-step process:
- Hardware Reception: the network interface card 
(NIC) receives the frame on the wire. Depending 
on its driver configuration, the NIC transfers the 
frame either to an internal hardware buffer memory or 
to a specified ring buffer.
- Hard IRQ: the NIC asserts the presence of a net frame 
by interrupting the CPU. This causes the NIC driver to 
acknowledge the interrupt and schedule the soft IRQ operation.
- Soft IRQ: this stage implements the actual frame-receiving 
process, and is run in softirq context. This means that the 
stage pre-empts all applications running on the specified CPU,
 but still allows hard IRQs to be asserted.
- In this context (running on the same CPU as hard IRQ, thereby 
minimizing locking overhead), the kernel actually removes the frame 
from the NIC hardware buffers and processes it through the network 
stack. From there, the frame is either forwarded, discarded, or passed 
to a target listening socket.
- When passed to a socket, the frame is appended to the 
application that owns the socket. This process is done iteratively until the 
NIC hardware buffer runs out of frames, or until the device weight 
(dev_weight). For more information about device weight, refer to Section 
- 8.4.1, “NIC Hardware Buffer” Application receive: the application 
receives the frame and dequeues it from any owned sockets 
via the standard POSIX calls (read, recv, recvfrom). At this point, 
data received over the network no longer exists on the network stack. 

The Red Hat Enterprise Linux Network Performance Tuning Guide available on the Red 
Hat Customer Portal contains information on packet reception in the Linux kernel, 
and covers the following areas of NIC tuning: SoftIRQ misses (netdev budget), tuned 
tuning daemon, numad NUMA daemon, CPU power states, interrupt balancing, pause frames,
 interrupt coalescence, adapter queue (netdev backlog), adapter RX and TX buffers, 
adapter TX queue, module parameters, adapter offloading, Jumbo Frames, TCP and UDP 
protocol tuning, and NUMA locality.
 
## CPU/cache affinity
To maintain high throughput on the receive path, it is recommended that 
you keep the L2 cache hot. As described earlier, network buffers 
are received on the same CPU as the IRQ that signaled their presence. 
This means that buffer data will be on the L2 cache of that receiving CPU.
To take advantage of this, place process affinity on applications expected to receive the most data on the NIC that shares the same core as the L2 cache. This will maximize the chances of a cache hit, and thereby improve performance. 
