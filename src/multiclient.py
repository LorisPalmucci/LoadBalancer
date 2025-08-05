import socket
import time
import logconfig

HOST = '127.0.0.1'
PORT = 50007

sockets = []
for i in range(5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    logconfig.LOGGER.info(f"Connessione {i+1} stabilita su {s}")
    #print(len(sockets))
    sockets.append(s)

logconfig.LOGGER.info(f"{len(sockets)} connections are active")

# Quando un socket chiude una connessione TCP, spesso il lato che ha effettuato la chiusura entra in stato TIME_WAIT.
# Questo stato dura un certo intervallo di tempo (tipicamente fino a 2 volte il massimo tempo di vita di un pacchetto in rete, MSL) ed è utile a garantire che eventuali pacchetti duplicati o ritardati vengano scartati e che la chiusura sia definitiva.
# Durante TIME_WAIT la connessione è tecnicamente chiusa ma il sistema tiene aperta la risorsa in attesa di questi timeout, impedendo anche di riutilizzare gli stessi indirizzi IP/porta subito.
while sockets:
    for sock in sockets:
        data = sock.recv(1024)
        if data == b'':
            sockets.remove(sock)
            logconfig.LOGGER.info(f"connessione {sock} chiusa")

#
# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     logconfig.LOGGER.info(f"Chiusura connessione...")
#     for s in sockets:
#         s.close()
#     logconfig.LOGGER.info(f"Connessione chiusa")
