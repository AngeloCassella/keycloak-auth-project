from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError
import json

keycloak_openid = KeycloakOpenID(
    server_url="http://localhost:8080/",
    client_id="python-client",
    realm_name="tesi"
)

username = "studente"
password = "1234"

try:
    token = keycloak_openid.token(username, password)
    print("\n=== ACCESS TOKEN ===")
    print(token['access_token'])

except KeycloakAuthenticationError as err:
    print("\n ERRORE DI AUTENTICAZIONE")
    print("Status code:", err.response_code)
    print("Dettagli:", err.error_message)
    print("Risposta completa:")
    print(err.response_body.decode())
