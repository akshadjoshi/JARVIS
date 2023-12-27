## nmap
```bash
nmap -v -Pn -n -sT -sCV -p 139,445 --script=smb* <IP> -oN nmap/smb
```


## smbclient 

**list the content**
```bash
smbclient -L //<IP>
```

```bash
smbclient -L \\<IP>
```

```sh
smbclient -L ////<IP>
```

```sh
smbclient -L \\\<IP>
```

```sh
smbclient -L \\\\<IP>
```


 **null session**
```sh
smbclient -L //10.10.11.174/ -U "" 
Password for [WORKGROUP\]:
```
```sh
smbclient  //10.10.11.174/support-tools -U ""
Password for [WORKGROUP\]:

```


**annon login**

```sh
smbclient -N //10.10.11.174/support-tools -U  
```

```sh
smbclient -N //10.10.11.174/support-tools -U "joshi"
```


## smbmap

```sh
smbmap -H 10.10.11.174
```
**pass the hash**

```sh
smbmap -H 192.168.1.100 -u administrator -p 'NTLM:LM'
```


