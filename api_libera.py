from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/libera', methods=['GET'])
def api_libera():
    return jsonify({"message": "Connessione riuscita alla API libera (senza autenticazione)"}), 200

if __name__ == '__main__':
    app.run(port=5001)
