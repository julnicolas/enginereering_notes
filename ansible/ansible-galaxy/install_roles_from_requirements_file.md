# Install roles from requirements file
Install several roles from ansible galaxy.
The perks of using this is that role versions are
explicetely stored in the requirements file.

``` sh
ansible-galaxy role install -r requirements.yml
```

Note - roles are downloaded in order to:
- ~/.ansible/roles
- /etc/ansible/roles
- /usr/share/ansible/roles
-> They will be downloaded in only one of these destinations.

