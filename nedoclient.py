import socket
import time
import threading
import hashlib
ss=socket.socket()
p=5050
sh=socket.gethostname()
ip=socket.gethostbyname(sh)
sh=input("ip server > ")
name=input("Tvoe name > ")
ss.connect((sh,p))
ss.send(name.encode())
def hash(mess):
    m=hashlib.sha1(mess.encode())
    m1=m.hexdigest()
    return m1
def priem():
    while True:
        d,a=ss.recvfrom(1024)
        print(a,'>',d.decode())
        time.sleep(0.2)
priv = threading.Thread(target = priem)
priv.start()
while True:
    mess=input("Me > ")
    mess1=hash(mess)
    ss.send(mess1.encode())
    ss.send(mess.encode())
ss.close()
