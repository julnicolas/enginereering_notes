# Show reverse dependencies
Two commands can be used, they return different values.

## Online database query
``` sh
pacman -Sii <package name>
```
This query is accurate, listing required and optional reverse deps.

## Local database query
``` sh
pacman -Qii <package name>
```
This query was not showing certain reverse dependencies even though I
may have had them present on my system.

