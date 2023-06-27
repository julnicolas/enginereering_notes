# Change boot options
This article shows how to add or remove boot parameters used to start the kernel.

## Change parameters in the default config
As root edit `vim /etc/default/grub` and change the parameter list in `GRUB_CMDLINE_LINUX_DEFAULT`.

Example:
``` sh
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

## Generate a new config file
By default the config is generated on stdout as follows:
``` sh
grub-mkconfig
```

To make it *persistent* type:
``` sh
grub-mkconfig -o /boot/grub/grub.cfg
```

## Reboot the machine so that new parameters can be applied
``` sh
shutdown -r now
```
