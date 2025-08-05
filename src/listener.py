import socket
import logconfig
from threading import Thread

HOST = ''
PORT = 50007

#funzione per testare la velocità di esecuzione
def new_thread(conn, addr):
    logconfig.LOGGER.info(f"Avvio del calcolo per il thread {addr}")
    with conn: #fa si che una volta finita l'esecuzione inizi la chiusura della connessione inviando un FIN al client (pacchetto di 0 byte) necessario anche per rilasciare la connessione anche in presenza di errori
        for i in range(50):
            i+=i
    logconfig.LOGGER.info(f"Avvio chiusura del thread {addr}")


def start_server():
    #crea la socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        logconfig.LOGGER.info(f"Avvio del server")
        #assegna la socket ad una tupla IP:PORT e resta in ascolto
        s.bind((HOST,PORT))
        s.listen(5)
        logconfig.LOGGER.info(f"Server in ascolto su port : {PORT}")
        #attende una connessione e genera un thread quando arriva
        while True:
            conn, addr = s.accept()
            logconfig.LOGGER.info(f"Connessione accettata da: {addr}")
            t = Thread(target=new_thread, args=(conn, addr)) #i parametri da passare deve essere per forza una tupla altrimenti da errore TypeError: __main__.new_thread() argument after * must be an iterable, not socket
            logconfig.LOGGER.info(f"Creato nuovo thread: {t}")
            t.start()
            logconfig.LOGGER.info(f"Thread avviato su {t.native_id}")
        
if __name__ == "__main__":
    #LOGGER = logconfig.logging.getLogger
    start_server()