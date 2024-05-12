# Install collections from requirements file
Install several collections from ansible galaxy.
The perks of using this is that collection versions are
explicetely stored in the requirements file.

``` sh
ansible-galaxy collection install -r requirements.yml
```

Note - collections are downloaded in order to:
- ~/.ansible/collections
- /etc/ansible/collections
- /usr/share/ansible/collections
-> They will be downloaded in only one of these destinations.

