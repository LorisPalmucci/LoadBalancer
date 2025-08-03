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
    sockets.append(s)

print("\n5 connections are active. Press Ctrl+C to close them.")

# try:
#     while True:
#         time.sleep(1)
# except KeyboardInterrupt:
#     logconfig.LOGGER.info(f"Chiusura connessione...")
#     for s in sockets:
#         s.close()
#     logconfig.LOGGER.info(f"Connessione chiusa")
