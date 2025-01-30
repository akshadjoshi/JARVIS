wsl python server access to public network

### Allow Traffic Through Windows Firewall

Open Windows Defender Firewall
Click Advanced Settings
Go to Inbound Rules → Click New Rule
Select Port → Next
Choose TCP and enter 80 as the port → Next
Select Allow the connection → Next
Apply to Private/Public networks → Next
Name it Allow WSL HTTP → Finish

### Enable Port Forwarding (run below cmd as administrator)

```sh
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=80 connectaddress=<wslIP> connectport=80
```
```sh
netsh interface portproxy show all
```
```sh
python3 -m http.server 80 --bind 0.0.0.0
```

now hit the windows host IP on another laptop to access the dir

### Disable Port Forwarding

```sh
netsh interface portproxy delete v4tov4 listenport=80 listenaddress=0.0.0.0
```
### Delete the Firewall Rule and run the below cmd
```sh
netstat -ano | findstr :80
```
