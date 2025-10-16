# 🔐 Keycloak Auth Project

Progetto realizzato come parte della **Tesi di Laurea in Reti di Calcolatori** presso l’Università Giustino Fortunato.

L’obiettivo è lo **studio e l’implementazione di un sistema di autenticazione e autorizzazione** basato su **OAuth 2.0 e Keycloak**, utilizzando **Flask** e **Docker**.

## ⚙️ Architettura
- **Keycloak (Authorization Server)**: gestisce utenti, ruoli e token JWT.
- **API Flask (Resource Server)**: espone endpoint liberi e protetti.
- **Client Python**: si autentica presso Keycloak e accede alle API.

## 🚀 Esecuzione del progetto

Avviare il sistema
aprire Docker e premere play o lanciare il comando docker-compose up
verificare se apre l'ambiente http://localhost:8080

Aprire la cartella del progetto tramite 
Visual studio facendo:
code ./

Aprire 4 terminali diversi: 
Lanciare su ogni terminale comando: 
source venv/bin/activate

Sul 1° terminale lanciare:
python3 client.py

Sul 2° terminale lanciare:
python3 api_libera.py

Sul 3° terminale lanciare 
python3 api.py

Sul 4° terminale lanciare 
python3 call_api.py

in modo da fare la chiamata 