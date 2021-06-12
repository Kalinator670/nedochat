import socket
import time
import threading
def kek(ip,port):
    global serv
    global clients
    clients=[]
    #прослушка соединений
    #1.socket.AF_INET 2.socket.SOCK_STREAM - 1.ipv4 2.TCP соединение соответственно
    serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #начало прослушивания по ip и порту
    serv.bind((ip,port))
    #сколько клиентов может слушать сервер (0- все клиенты)
    serv.listen(0)
    #отслеживание новых соединений
    threading.Thread(target=ch).start()
    print("Go")
def ch():
    while True:
        global client
        #прием подключений (принимается клиентский сокет-с и его адрес-а)
        c,a=serv.accept()
        client=c.recv(1024).decode()
        print(client, 'подцепился')
        if c not in clients:
            clients.append(c)
            #поток ниже используется для обработки сообщений (передается клиентский сокет и запускается поток)
            threading.Thread(target=mh,args=(c,)).start()
#обработка отправляемого текста
def mh(cs):
    while True:
        #прием данных от клиента
        b,a=cs.recvfrom(1024)
        print(a,'>',b)
        if b=='' or b==b'':
            break
        #удаление подключения, если клиент вышел (удаление сокета)
        if b=="exit":
            clients.remove(cs)
            break
        #для того, чтобы не отправить сообщение самому себе
        for c in clients:
            if c!=clients:
                c.send(b)
kek("127.0.0.1", 5050)
