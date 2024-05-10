# Ansible hangs on enable
To avoid the problem, tell the kernel to not drop
active ssh connections. Ansible seems to hang because
no feedback occurs on the connection until it expires.

```yml
- name: Allow SSH - port 22    
  ufw:
    rule: allow                
    port: 22
  
# Rate limiting: 6 connections per IP per 30s
- community.general.ufw:       
    rule: limit
    port: 22
    proto: tcp
  
- name: Allow TLS - port 443   
  ufw:
    rule: allow                
    port: 443
  
- name: Configure the kernel to keep connections alive when enabling the firewall
  sysctl:
    name: net.netfilter.nf_conntrack_tcp_be_liberal
    value: 1
    state: present
    sysctl_set: yes
    reload: yes

- name: Enable ufw
  ufw:
    state: enabled
```
