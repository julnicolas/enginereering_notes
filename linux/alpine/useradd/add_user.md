# Add User
adduser <user name> -G <group name>

The group must be created beforehand.

- `-H` to not create a home dir
- `-D` to not set a password
- `-S` to create a system user (UID and GUID in the 100s, no password, SYS_UID_MIN-SYS_UID_MAX range, defined in /etc/login.defs)

