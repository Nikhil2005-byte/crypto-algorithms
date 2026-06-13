from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt(message: str, public_key_bytes: bytes) -> bytes:
    pub_key = RSA.import_key(public_key_bytes)
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message.encode())

def decrypt(ciphertext: bytes, private_key_bytes: bytes) -> str:
    priv_key = RSA.import_key(private_key_bytes)
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext).decode()
if __name__ == "__main__":
    print("=== RSA-2048 Encryption Demo ===")
    
    print("Generating RSA key pair...")
    private_key, public_key = generate_keypair()
    print("✅ Keys generated!")
    print(f"Public Key (first 60 chars): {public_key[:60]}...")
    
    message = "RSA secret message"
    print(f"\nOriginal Text: {message}")
    
    encrypted = encrypt(message, public_key)
    print(f"Encrypted (bytes): {encrypted[:30]}...")
    
    decrypted = decrypt(encrypted, private_key)
    print(f"Decrypted: {decrypted}")
    
    print("\n✅ RSA encryption/decryption successful!" if message == decrypted else "❌ Something went wrong")
