from keycloak import KeycloakOpenID
import requests

# Configurazione Keycloak
keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/",
    client_id="python-client",         # nome del client inserito in Keycloak
    realm_name="tesi",                 # Nome del realm
)

# Credenziali dell'utente
username = "studente"
password = "1234"

# Richiedi il token
token = keycloak_openid.token(username, password)

print("\n=== ACCESS TOKEN ===")
print(token["access_token"])


from keycloak import KeycloakOpenID

