# Exception Safety Properties

## Exception safety
Three levels are defined describing objects's state after an exception has been raised.

### Weak/basic exception safety guarantee
If an exception is thrown (by a function or method), no resources are 
leaked, involved objects are destructible and still usable. Though current state may not 
be predictable.

### Strong exception safety guarantee
- weak guarantee
- objects' state are left unchanged in case an exception occurs. State is 
therefore predictable. This property is generally implemented using some kind of roll back 
technique.

### No throw guarantee
No exceptions are thrown to callers even if exceptions are raised while method is executed.

Basic and strong exception safety are guaranteed. 
