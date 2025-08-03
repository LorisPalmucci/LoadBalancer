import socket
from threading import Thread, ThreadError
import logconfig

HOST = ''
PORT = 50007

def new_thread(conn, addr):
    print ("connesso da ", addr)
    print (conn)   

def start_server():
    #crea la socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logconfig.LOGGER.info("Avvio del server")
        #assegna la socket ad una tupla IP:PORT e resta in ascolto
        s.bind((HOST,PORT))
        s.listen(5)
        logconfig.LOGGER.info("Server in ascolto")
        #attende una connessione e genera un thread quando arriva
        while True:
            conn, addr = s.accept()
            t = Thread(target=new_thread, args=(conn,addr))
            t.start()
        
if __name__ == "__main__":
    #LOGGER = logconfig.logging.getLogger
    start_server()