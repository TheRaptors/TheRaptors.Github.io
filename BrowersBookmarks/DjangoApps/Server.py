#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n".encode())
    client.send("Content-Type:text/html\r\n\r\n".encode())
    #</br>:换行
    client.send("Hello World!</br>".encode())
    #如果此处不加"http://"，则打开"http://domain:port/www.baidu.com"
    client.send("<a href='www.baidu.com'>Hello World!</a></br>".encode())
    #跳转到"http://www.baidu.com"
    client.send("<a href='http://www.baidu.com'>Hello World!</a>".encode())
    

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(5)
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()
if __name__ == '__main__':
    main()
