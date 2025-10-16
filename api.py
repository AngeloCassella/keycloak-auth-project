from flask import Flask, request, jsonify
import jwt
from jwt import PyJWKClient

app = Flask(__name__)

# Configurazione Keycloak
REALM = "tesi"
ISSUER = f"http://localhost:8080/realms/{REALM}"
JWKS_URL = f"{ISSUER}/protocol/openid-connect/certs"

@app.route('/api/protetta', methods=['GET'])
def api_protetta():
    # Log nel terminale per debugging
    print("== RICHIESTA SU /api/protetta ==")
    print("Authorization header:", request.headers.get('Authorization'))

    auth_header = request.headers.get('Authorization', '')
    parts = auth_header.split()

    # Caso 2: senza token -> 403
    if len(parts) != 2 or parts[0].lower() != 'bearer':
        return jsonify({"error": "Accesso vietato: token mancante"}), 403

    token = parts[1].strip()

    try:
        # Recupero chiave pubblica corretta dal kid del token
        jwk_client = PyJWKClient(JWKS_URL)
        signing_key = jwk_client.get_signing_key_from_jwt(token).key

        # Decodifica e validazione del token
        payload = jwt.decode(
            token,
            signing_key,
            algorithms=["RS256"],
            issuer=ISSUER,
            options={"verify_aud": False},  # disattivo controllo audience
            leeway=10
        )

        # Caso 3: token valido
        return jsonify({
            "message": "✅ Accesso consentito con token valido",
            "subject": payload.get("sub"),
            "issued_at": payload.get("iat"),
            "expires_at": payload.get("exp")
        }), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token scaduto"}), 401
    except jwt.InvalidIssuerError:
        return jsonify({"error": "Issuer non valido"}), 401
    except Exception as e:
        return jsonify({"error": "Token non valido", "detail": str(e)}), 401


if __name__ == '__main__':
    print("== API PROTETTA (nuova) in ascolto su :5002 ==")
    app.run(host="127.0.0.1", port=5002)
