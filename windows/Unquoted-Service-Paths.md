```bash
wmic service get name,displayname,pathname,startmode |findstr /i "Auto" |findstr /i /v "C:\Windows\\" |findstr /i /v """
```


```sh
wmic service get name,pathname |  findstr /i /v "C:\Windows\\" | findstr /i /v """
```
