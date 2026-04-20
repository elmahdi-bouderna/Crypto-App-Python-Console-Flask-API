import hashlib
import os
from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

KEY_FILE = "secret.key"


def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key


key = load_or_create_key()
cipher = Fernet(key)


def encrypt_text(text: str) -> str:
    return cipher.encrypt(text.encode()).decode()


def decrypt_text(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()


def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


@app.route("/")
def home():
    return jsonify({
        "message": "API Flask active",
        "routes": {
            "POST /crypt": {"body": {"text": "bonjour"}},
            "GET /decrypt?text=<encrypted_text>": {},
            "POST /hash": {"body": {"text": "bonjour"}},
            "POST /compare-hashes": {"body": {"hash1": "...", "hash2": "..."}}
        }
    })


@app.route("/crypt", methods=["POST"])
def crypt():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Le champ 'text' est obligatoire."}), 400

    encrypted = encrypt_text(data["text"])
    return jsonify({
        "original_text": data["text"],
        "encrypted_text": encrypted
    })


@app.route("/decrypt", methods=["GET"])
def decrypt():
    encrypted_text = request.args.get("text")
    if not encrypted_text:
        return jsonify({"error": "Le paramètre 'text' est obligatoire."}), 400

    try:
        decrypted = decrypt_text(encrypted_text)
        return jsonify({
            "encrypted_text": encrypted_text,
            "decrypted_text": decrypted
        })
    except Exception:
        return jsonify({"error": "Texte chiffré invalide ou clé incorrecte."}), 400


@app.route("/hash", methods=["POST"])
def hash_text():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Le champ 'text' est obligatoire."}), 400

    hashed = sha256_hash(data["text"])
    return jsonify({
        "text": data["text"],
        "sha256": hashed
    })


@app.route("/compare-hashes", methods=["POST"])
def compare_hashes():
    data = request.get_json()
    if not data or "hash1" not in data or "hash2" not in data:
        return jsonify({"error": "Les champs 'hash1' et 'hash2' sont obligatoires."}), 400

    same = data["hash1"] == data["hash2"]
    return jsonify({
        "hash1": data["hash1"],
        "hash2": data["hash2"],
        "same": same,
        "message": "Aucune modification détectée." if same else "Modification détectée."
    })


if __name__ == "__main__":
    app.run(debug=True)