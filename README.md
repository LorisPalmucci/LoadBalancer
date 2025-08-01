# Progetto Load Balancer in Python

Questo repository contiene un semplice progetto di Load Balancer realizzato in Python. L'obiettivo è illustrare i concetti fondamentali di un load balancer, tra cui:

*   **Ascolto delle connessioni in entrata:** Un socket principale accetta le connessioni dei client.
*   **Gestione Concorrente:** Ogni connessione viene gestita in un thread separato per non bloccare il server.
*   **Pool di Server Backend:** Il load balancer distribuisce il traffico tra un insieme di server di destinazione.
*   **Strategia di Bilanciamento:** In questa prima fase, verrà implementata una strategia Round Robin.

## Componenti

*   `load_balancer.py`: Lo script principale che funge da load balancer.
*   `server1.py`: Un semplice server di test in ascolto sulla porta 9001.
*   `server2.py`: Un altro server di test in ascolto sulla porta 9002.
