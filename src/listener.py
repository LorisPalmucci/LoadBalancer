import socket
from threading import Thread, ThreadError

HOST = ''
PORT = 50007

def new_thread(conn, addr):
    print ("connesso da ", addr)
    print (conn)   

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    #crea la socket
        s.bind((HOST,PORT))                                         #assegna la socket ad una tupla IP:PORT e resta in ascolto
        s.listen(5)
        while True:                                                 #attende una connessione e genera un thread quando arriva
            conn, addr = s.accept()
            t = Thread(target=new_thread, args=(conn,addr))
            t.start()
        
if __name__ == "__main__":
    start_server()