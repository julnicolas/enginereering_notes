# Close Best Practice
Channels are not like files so they do not need
to be closed to free system resources.

A channel does not leak resources when going out of
scope and being destroyed by the garbage collector.

## When to manually close a channel?
Close a channel only when certain communication is
over. The closing action must be done from the sender
end.

### Why? 
Reading from a closed channel has no dramatic impact -
it returns the channel type's null value. So no crash
is to expect by reading a close channel (at least 
immediatly).

Writing to a closed channel causes a panic. So it's better
not to let that scenario being possible.

Finally, from a subscriber/publisher point of view, when publishing
is over (i.e. channel is closed), subsrciber can unsubscribe from said
feed. This is a commong scenario that developers are used too.

