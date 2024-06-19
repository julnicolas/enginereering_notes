# Decrypt a file
This command decrypts a file using ansible vault. It is
a symetric encryption method (probably using AES). It
needs a password file to encrypt the files.

``` sh
ansible-vault decrypt \
    --vault-password-file ../../../vault_password.txt \
    --output foo \
    foo.enc
```
Note - use `-` as value for `--output` to print file to
`stdout`.

