# Show all available packages
This command shows all available packages (installed or not) with their
description:
``` sh
pacman -Ss
```

To just show package names add the `q` (for quiet) option:
``` sh
pacman -Ssq
```

The above command can be filtered out using a fuzzy finder such
as `fzf`.

