# Encrypt a file
This command encrypts a file using ansible vault. It is
a symetric encryption method (probably using AES). It
needs a password file to encrypt the files.

``` sh
ansible-vault encrypt \
    --vault-password-file ../../../vault_password.txt \
    --output foo.enc \
    foo
```
Note - use `-` as value for `--output` to print file to
`stdout`.

