# List packages which install binary
This command query the database to check if file belongs
to any package managed by pacman.

It checks against the database. Therefore it cannot tell
if the package was installed manually or from which package
it was installed from.

To be extra clear, it doesn't check how was pointed file
installed.

Here's an example with gcc.
``` sh
pacman -F $(which gcc)
```

## Note on how to handle dependencies
Leaving `/bin` directories (`/bin`, /usr/bin) managed 
by pacman avoid conflict problems.
-> pacman do not install if it finds that a package
would install a file that is already present.

If binaries are installed in `/bin` dirs without
pacman then it is hard to tell from which package
manager they come from or if they were installed
manually. It makes it harder to manage software
version that way.

This is why it is better to install aur binaries
or manually compiled tools in local user bin dirs
not managed by pacman such as `~/bin`.

