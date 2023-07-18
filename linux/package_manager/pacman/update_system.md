# Update whole system
The following commands update the whole system on distributions using
`pacman` as package manager (such as arch linux).

To update the system, please check first that the key ring is still up-to-date
by typing the following:
``` sh
pacman -Sy archlinux-keyring
```

Then update all packages:
``` sh
pacman -Syu
```

This is not considered as beeing a partial update because the keyring is needed to install any other packages.

