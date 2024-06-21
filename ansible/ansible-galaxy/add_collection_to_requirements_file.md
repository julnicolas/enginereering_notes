# How to add/install a collection to the requirements file
Note - the same applies for installing roles

## Install the collection
``` sh
ansible-galaxy collection <collection name>
```

## Get the collection version
``` sh
ansible-galaxy collection list | grep '<collection name>'
```
Retrieve the version number from here.

## Edit the requirements file by adding the collection
``` yml
collections:
  - name: "collection name (fqdn)"
    version: ">=8.6.0,<9.0.0"
  - name: ...
```

