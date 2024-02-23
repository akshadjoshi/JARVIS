
look for **service** you have the **power to restart**

```bash
wmic service where startmode="Auto" get name, displayname, state, startmode
```

```sh
wmic service where startmode="Auto" get name, displayname, state, startmode,pathname
```
