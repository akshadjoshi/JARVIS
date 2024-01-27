## on my kali linux

```
sudo ip tuntap add user [your_username] mode tun ligolo

sudo ip tuntap add user akshad mode tun ligolo
```

```
sudo ip link set ligolo up
```

```
lin-proxy -selfcert -laddr 0.0.0.0:443
```


## on windows box

```bash
 ./agent.exe -connect <kali-ip>:443 -ignore-cert
```


# in the ligolo-ng prompt of kali type

```
session

ifconfig

start
```


# add the interface

```
sudo ip route add 172.16.219.0/24 dev ligolo

```
