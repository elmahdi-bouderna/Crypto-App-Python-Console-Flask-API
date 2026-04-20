import hashlib
import os
from cryptography.fernet import Fernet


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


def compare_hashes(hash1: str, hash2: str) -> bool:
    return hash1 == hash2


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Saisir un texte puis le chiffrer")
        print("2. Déchiffrer le texte")
        print("3. Calculer le SHA-256 d'un texte")
        print("4. Comparer deux hashes")
        print("5. Quitter")

        choice = input("Choisir une option: ")

        if choice == "1":
            text = input("Entrer le texte à chiffrer: ")
            encrypted = encrypt_text(text)
            print("Texte chiffré :", encrypted)

        elif choice == "2":
            encrypted_text = input("Entrer le texte chiffré: ")
            try:
                decrypted = decrypt_text(encrypted_text)
                print("Texte déchiffré :", decrypted)
            except Exception:
                print("Erreur : texte chiffré invalide ou clé incorrecte.")

        elif choice == "3":
            text = input("Entrer le texte à hasher: ")
            print("SHA-256 :", sha256_hash(text))

        elif choice == "4":
            hash1 = input("Entrer le premier hash: ")
            hash2 = input("Entrer le deuxième hash: ")
            if compare_hashes(hash1, hash2):
                print("Les deux hashes sont identiques.")
            else:
                print("Les deux hashes sont différents : modification détectée.")

        elif choice == "5":
            print("Au revoir.")
            break

        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == "__main__":
    menu()