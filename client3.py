import socket
import threading as th
ip=input('Enter ip server :')
port=input('\nEnter port server :')

isshell=0

def recive():
    global isshell
    while 1:
       res=s.recv(1024).decode("utf-8")
       if res.lower()=="shell":
            isshell=1
       if res.lower()=="exit":
            isshell==0   
            
       print(res)
          
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
try: 
    s.connect((ip, int(port)))
    t=th.Thread(target=recive)
    t.start()
    while True:
        if isshell==0:
           message=input("your message: ")+" "
        else:
           message=input("Command : ") 
             
        s.send(message.encode('utf-8'))
except socket.error as e:
        print(e)

  




            