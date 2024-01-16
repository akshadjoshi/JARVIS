ldapsearh (find user principal name and service name) --> valid users via kerbrute / or nmap (for keberoasting and asrep roasting)

kerberoasting 

if roasting fails: vaild users via kerbrute ---> crackmapexec smb, ldap, winrm, msql

if ldapsearh fails you can use kerbrute to find user

## to get dc name 

```sh
ldapsearch -x -H ldap://10.10.11.158 -s base namingcontexts
```



## null session

```sh
ldapsearch -x -H ldap://<IP> -D '' -w '' -b "DC=htb,DC=local" > output.txt
```


```sh
ldapsearch -x -H ldap://10.10.10.161 -D '' -w '' -b "DC=htb,DC=local" | grep userPrincipalName | cut -f 2 -d " "
```
