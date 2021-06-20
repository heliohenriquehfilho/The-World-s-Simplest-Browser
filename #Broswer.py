#Broswer

import socket

mysock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) #Estabelece um meio de se comunicar
mysock.connect(('data.pr4e.org', 80)) #Começa a comunicação 
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() #Cria uma string com o comando que irá ser mandado
mysock.send(cmd) #Envia o comando

#Esse loop coleta o 'Data' do documento que pedimos
while True:
    data=mysock.recv(512)
    if len(data) <1:
        break
    print(data.decode(), end=' ')

mysock.close() #Fecha a comunicação 
