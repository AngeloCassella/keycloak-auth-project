import requests
from keycloak import KeycloakOpenID

# ====== CONFIG ======
KEYCLOAK_SERVER_URL = "http://localhost:8080"
REALM_NAME = "tesi"
CLIENT_ID = "python-client"
USERNAME = "studente"
PASSWORD = "1234"

API_LIBERA_URL = "http://127.0.0.1:5001/api/libera"      # porta 5001
API_PROTETTA_URL = "http://127.0.0.1:5002/api/protetta"  # porta 5002 (coerente con api.py nuovo)

# ====== TOKEN ======
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=CLIENT_ID,
    realm_name=REALM_NAME
)

token = keycloak_openid.token(USERNAME, PASSWORD)
access_token = token["access_token"].strip()

print("\n🔑 TOKEN JWT OTTENUTO:\n")
print(access_token)
print("\n----------------------------------------\n")

# ====== 1) API LIBERA ======
print("📡 Chiamata alla API Libera (senza autenticazione):")
try:
    r = requests.get(API_LIBERA_URL, timeout=5)
    print(f"Status Code: {r.status_code}")
    try:
        print(f"Risposta: {r.json()}")
    except Exception:
        print(f"Risposta: {r.text}")
except Exception as e:
    print("ERRORE:", e)
print("\n----------------------------------------\n")

# ====== 2) API PROTETTA - SENZA TOKEN ======
print("📡 Chiamata alla API Protetta (senza token):")
try:
    r = requests.get(API_PROTETTA_URL, timeout=5)
    print(f"Status Code: {r.status_code}")
    try:
        print(f"Risposta: {r.json()}")
    except Exception:
        print(f"Risposta: {r.text if r.text else 'Nessun contenuto restituito'}")
except Exception as e:
    print("ERRORE:", e)
print("\n----------------------------------------\n")

# ====== 3) API PROTETTA - CON TOKEN ======
print("📡 Chiamata alla API Protetta (con token):")
headers = {"Authorization": f"Bearer {access_token}"}
try:
    r = requests.get(API_PROTETTA_URL, headers=headers, timeout=5)
    print(f"Status Code: {r.status_code}")
    try:
        print(f"Risposta: {r.json()}")
    except Exception:
        print(f"Risposta: {r.text if r.text else 'Nessun contenuto restituito'}")
except Exception as e:
    print("ERRORE:", e)
print("\n----------------------------------------\n")
