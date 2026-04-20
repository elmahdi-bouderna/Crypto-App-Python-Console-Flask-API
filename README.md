# 🔐 Crypto App (Python) — Console + Flask API

This project is a Python implementation of the given exercises, replacing:

* Java → Python
* Spring Boot → Flask

It includes:

* A console-based application
* A web API using Flask

---

# 📌 Features

## 🖥️ Console Application

Menu-driven program with the following options:

1. Encrypt a text
2. Decrypt a text
3. Compute SHA-256 hash
4. Compare two hashes (detect modification)

---

## 🌐 Web Application (Flask API)

Available endpoints:

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| POST   | `/crypt`          | Encrypt a text        |
| GET    | `/decrypt`        | Decrypt a text        |
| POST   | `/hash`           | Generate SHA-256 hash |
| POST   | `/compare-hashes` | Compare two hashes    |

---

# 🛠️ Technologies Used

* Python 3
* Flask
* Cryptography (Fernet)
* hashlib (SHA-256)

---

# 📂 Project Structure

```
project/
│
├── console_app.py
├── app.py
├── secret.key
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/crypto-app.git
cd crypto-app
```

## 2. Install dependencies

```bash
pip install flask cryptography
```

---

# ▶️ Usage

## 🖥️ Run Console Application

```bash
python console_app.py
```

---

## 🌐 Run Flask Application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

# 🧪 Postman Testing (Step-by-Step)

## 🔐 1. Encrypt Text

**Method:** POST
**URL:** http://127.0.0.1:5000/crypt

**Body → raw → JSON:**

```json
{
  "text": "Hello World"
}
```

**Response:**

```json
{
  "original_text": "Hello World",
  "encrypted_text": "gAAAAABl..."
}
```

---

## 🔓 2. Decrypt Text

**Method:** GET
**URL:**

```
http://127.0.0.1:5000/decrypt?text=gAAAAABl...
```

**Response:**

```json
{
  "encrypted_text": "gAAAAABl...",
  "decrypted_text": "Hello World"
}
```

---

## 🔑 3. SHA-256 Hash

**Method:** POST
**URL:** http://127.0.0.1:5000/hash

**Body → raw → JSON:**

```json
{
  "text": "Hello World"
}
```

**Response:**

```json
{
  "text": "Hello World",
  "sha256": "a591a6d40bf420404a011733cfb7b190..."
}
```

---

## 🔍 4. Compare Hashes

**Method:** POST
**URL:** http://127.0.0.1:5000/compare-hashes

**Body → raw → JSON:**

```json
{
  "hash1": "abc123",
  "hash2": "abc123"
}
```

**Response:**

```json
{
  "same": true,
  "message": "Aucune modification détectée."
}
```

---

# 💻 Curl Commands (Alternative)

## Encrypt

```bash
curl -X POST http://127.0.0.1:5000/crypt \
-H "Content-Type: application/json" \
-d "{\"text\":\"Hello\"}"
```

## Decrypt

```bash
curl "http://127.0.0.1:5000/decrypt?text=ENCRYPTED_TEXT"
```

## Hash

```bash
curl -X POST http://127.0.0.1:5000/hash \
-H "Content-Type: application/json" \
-d "{\"text\":\"Hello\"}"
```

## Compare

```bash
curl -X POST http://127.0.0.1:5000/compare-hashes \
-H "Content-Type: application/json" \
-d "{\"hash1\":\"abc\",\"hash2\":\"abc\"}"
```

---

# ⚠️ Important Notes

* Encryption uses **Fernet (symmetric encryption)**
* SHA-256 is a **one-way hash function (not reversible)**
* `secret.key` is automatically generated

---

# 🎯 Exercises Mapping

## Exercise 1

✔ Console application
✔ Encryption / Decryption
✔ SHA-256 hashing
✔ Hash comparison

## Exercise 2

✔ Web application (Flask)
✔ REST API endpoints
✔ HTTP methods (GET / POST)

---

# 👨‍💻 Author

**EL MAHDI BOUDERNA**

---

# ⭐ Possible Improvements

* Add a frontend (React / HTML)
* Add database storage
* Add authentication (JWT)
* Dockerize the project
