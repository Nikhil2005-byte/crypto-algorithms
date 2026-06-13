from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    return get_random_bytes(32)           # 256-bit key

def encrypt(plaintext: str, key: bytes) -> str:
    cipher = AES.new(key, AES.MODE_CBC)   # CBC mode adds an IV
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    # Store IV + ciphertext together (you need IV to decrypt)
    result = base64.b64encode(cipher.iv + ct_bytes).decode()
    return result

def decrypt(ciphertext_b64: str, key: bytes) -> str:
    raw = base64.b64decode(ciphertext_b64)
    iv = raw[:16]                          # First 16 bytes = IV
    ct = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()
if __name__ == "__main__":
    print("=== AES-256 Encryption Demo ===")
    
    key = generate_key()
    print(f"Generated Key (base64): {key.hex()}")
    
    message = "Hello, this is a secret message!"
    print(f"Original Text: {message}")
    
    encrypted = encrypt(message, key)
    print(f"Encrypted: {encrypted}")
    
    decrypted = decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")
    
    print("\n✅ AES encryption/decryption successful!" if message == decrypted else "❌ Something went wrong")
