from cryptography.fernet import Fernet
import base64
import hashlib

# Function to derive a key from the passkey
def get_key_from_passkey(passkey):
    # Use SHA-256 to create a consistent key from the passkey
    key = hashlib.sha256(passkey.encode()).digest()
    # Convert to a valid Fernet key (32 bytes base64-encoded)
    return base64.urlsafe_b64encode(key[:32])

# Function to encrypt resume data
def encrypt_resume(resume_data, passkey):
    try:
        key = get_key_from_passkey(passkey)
        cipher = Fernet(key)
        encrypted_data = cipher.encrypt(resume_data.encode())
        encoded_data = base64.b64encode(encrypted_data).decode()
        return encoded_data
    except Exception as e:
        print(f"Encryption error: {e}")
        return None

# Function to decrypt resume data
def decrypt_resume(encoded_data, passkey):
    try:
        key = get_key_from_passkey(passkey)
        cipher = Fernet(key)
        encrypted_data = base64.b64decode(encoded_data.encode())
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        return None
