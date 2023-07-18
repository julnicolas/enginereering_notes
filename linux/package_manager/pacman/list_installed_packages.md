# List installed packages
This shows a list of all installed packages:
``` sh
pacman -Q
```

To show up package description alongside package names:
``` sh
pacman -Qs
```

Then it is possible to filter by name patterns on package name *AND* description
by providing a pattern to the `s` option such as:
``` sh
pacman -Qs go
```

It is then possible to show package names only (with a search on name *and* description still):
``` sh
pacman -Qsq <package name, i.e. qt>
```

