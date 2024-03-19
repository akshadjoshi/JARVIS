## nmap
```bash
nmap -v -Pn -n -sT -sCV -p 139,445 --script=smb* <IP> -oN nmap/smb
```


## smbclient 

**imp**

```sh
smbclient -L //IP -U dcname//username%password
```


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

**for domain join pc**
```
smbmap -H <ip> -d <domain-name> -u <username> -p <password>
```



## SMB Anonymous

**to list the contents**
```sh
smbmap -H 10.10.10.100 -r <sharedir> --depth 10 --no-banner -q
```
**eg**
```bash
smbmap -H 10.10.10.100 -r Replication --depth 10 --no-banner -q
```
#### Download files

```sh
smbclient //10.10.10.100/Replication/ -c "recurse ON; prompt OFF; cd active.htb; mget *"
```
