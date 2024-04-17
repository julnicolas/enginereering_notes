# Group Ranges
## 0-99
The group ID ranging from `0` to `99` are reserved 
for system accounts, and they are statically assigned. 

## 100-499 or 100-999
Then, the group ID from `100` to `999` is dynamically assigned
for application groups.

## 500-... or 1000-...
Finally, we've seen that for regular group 
accounts, the group ID, by convention, starts from `1000`

## Final note
For system administration purposes, given that 1000 > 500,
it is safer to assign a gid > 1000 rather than > 500 as the
first solution works for both conventions.

