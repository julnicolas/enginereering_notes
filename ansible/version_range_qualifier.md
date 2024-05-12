# Version Range Qualifier
At the moment, it is only supported for collections
in requirement files.

``` sh
ansible-galaxy collection install 'my_namespace.my_collection:>=1.0.0,<2.0.0'
```
Note - in a `requirement file`, write the requirement expression in the
`version` field. The requirement expression being: `>=1.0.0,<2.0.0`.

Ansible will always install the most recent version that meets the range 
identifiers you specify. You can use the following range identifiers:

- `*`: The most recent version. This is the default.
- `!=`: Not equal to the version specified.
-`==`: Exactly the version specified.
- `>=`: Greater than or equal to the version specified.
- `>`: Greater than the version specified.
- `<=`: Less than or equal to the version specified.
- `<`: Less than the version specified.

