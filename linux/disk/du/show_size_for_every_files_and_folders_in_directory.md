# Show Size Of All Files And Folders In Directory
``` sh
du -h --max-depth=1 <path, default is current dir> | sort -h --reverse
```
The result is sorted from the highest size to the lowest.

