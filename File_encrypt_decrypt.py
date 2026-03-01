from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

    print("✅ File Encrypted Successfully!")

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    decrypted = f.decrypt(data)

    original_name = filename.replace(".enc", ".dec.txt")
    with open(original_name, "wb") as file:
        file.write(decrypted)

    print("✅ File Decrypted Successfully!")

def main():
    if not os.path.exists(KEY_FILE):
        generate_key()

    print("\n--- File Encryption System ---")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Enter choice (1/2): ")

    file_name = input("Enter file name: ")

    if choice == "1":
        encrypt_file(file_name)
    elif choice == "2":
        decrypt_file(file_name)
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()