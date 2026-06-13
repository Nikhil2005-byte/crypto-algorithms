---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Nikhil2005-byte/crypto-algorithms.git
cd crypto-algorithms

# Install dependency
pip3 install pycryptodome --break-system-packages
```

---

## 🚀 Usage

### 🔷 SHA Hashing
```bash
# Hash a text string (SHA-256 + SHA-512)
python3 main.py sha hash --text "password123"

# Hash a file
python3 main.py sha hash-file --file myfile.txt

# Verify file integrity
python3 main.py sha verify --file myfile.txt --hash <known_hash>
```

### 🔒 AES-256 Encryption
```bash
# Encrypt text (generates a random key automatically)
python3 main.py aes encrypt --text "Hello World"

# Decrypt text (use the key printed during encryption)
python3 main.py aes decrypt --text "<encrypted_text>" --key "<hex_key>"
```

### 🔑 RSA-2048 Encryption
```bash
# Step 1 — Generate public/private key pair
python3 main.py rsa generate-keys

# Step 2 — Encrypt a message using public key
python3 main.py rsa encrypt --text "Top secret message"

# Step 3 — Decrypt using private key
python3 main.py rsa decrypt
```

### ❓ Help Menu
```bash
python3 main.py --help
python3 main.py aes --help
python3 main.py rsa --help
python3 main.py sha --help
```

---

## 💡 Key Concepts Learned

- **AES CBC Mode** — An IV (Initialization Vector) ensures identical plaintexts produce different ciphertexts every time
- **RSA OAEP Padding** — Prevents pattern-based attacks on raw RSA encryption
- **Symmetric vs Asymmetric** — AES is fast but needs a shared key; RSA solves key distribution using a key pair
- **SHA is one-way** — Hashes cannot be reversed, making them ideal for password storage and file integrity checks
- **Avalanche Effect** — A single character change in input produces a completely different hash output

---

## 🛡️ Security Notes

- Private keys and encrypted files are excluded from this repo via `.gitignore`
- AES keys are randomly generated per session using `get_random_bytes(32)`
- RSA-2048 with OAEP padding is the current industry standard
- Never hardcode cryptographic keys in source code

---

## 📸 Screenshots

*Coming soon — terminal demo screenshots*

---

## 📚 Dependencies

| Package | Purpose |
|---------|---------|
| `pycryptodome` | AES and RSA cryptographic operations |
| `hashlib` | SHA hashing (Python standard library) |
| `argparse` | CLI interface (Python standard library) |
