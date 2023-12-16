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
