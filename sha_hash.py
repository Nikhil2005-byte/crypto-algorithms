import hashlib

def hash_text(text: str, algorithm: str = "sha256") -> str:
    h = hashlib.new(algorithm)
    h.update(text.encode())
    return h.hexdigest()

def hash_file(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_file(filepath: str, known_hash: str) -> bool:
    return hash_file(filepath) == known_hash
if __name__ == "__main__":
    print("=== SHA Hashing Demo ===")
    
    text = "password123"
    print(f"Original Text: {text}")
    
    hash256 = hash_text(text, "sha256")
    print(f"SHA-256 Hash: {hash256}")
    
    hash512 = hash_text(text, "sha512")
    print(f"SHA-512 Hash: {hash512}")
    
    # Show that same input ALWAYS gives same hash
    print(f"\nSame input again: {hash_text(text, 'sha256')}")
    print("✅ Hashes match!" if hash256 == hash_text(text, "sha256") else "❌ Mismatch")
    
    # Show that different input gives completely different hash
    different = hash_text("password124", "sha256")
    print(f"\nSlightly different input hash: {different}")
    print("✅ Hashes are different (avalanche effect demonstrated!)")
