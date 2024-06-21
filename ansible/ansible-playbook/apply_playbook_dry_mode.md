# Dry mode execution
Changes are simulated but not executed on hosts.

``` sh
ansible-playbook -i inventory.ini site.yml --check [--diff]
```

The `--diff` option shows a diff of changes between before
applying the playbook and after.
*WARNING* - sensitive file information can be displayed using
the copy module.

