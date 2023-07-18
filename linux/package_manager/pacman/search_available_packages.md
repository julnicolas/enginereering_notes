# Search available packages
To search available packages (whether installed or not) by name or description
type the following:
``` sh
pacman -Ss <name pattern>
```

To perform the same search but only display package names type:
``` sh
pacman -Ssq <name pattern>
```

Then to further filter either use `grep` or a fuzzy searcher such as `fzf`.

