import argparse
import aes_cipher, rsa_cipher, sha_hash

def handle_aes(args):
    if args.aes_command == "encrypt":
        key = aes_cipher.generate_key()
        encrypted = aes_cipher.encrypt(args.text, key)
        print(f"\n✅ AES Encryption Successful!")
        print(f"🔑 Key (save this!): {key.hex()}")
        print(f"🔒 Encrypted Text:   {encrypted}")

    elif args.aes_command == "decrypt":
        key = bytes.fromhex(args.key)
        decrypted = aes_cipher.decrypt(args.text, key)
        print(f"\n✅ AES Decryption Successful!")
        print(f"🔓 Decrypted Text: {decrypted}")

def handle_rsa(args):
    if args.rsa_command == "generate-keys":
        private_key, public_key = rsa_cipher.generate_keypair()
        # Save keys to files
        with open("private_key.pem", "wb") as f:
            f.write(private_key)
        with open("public_key.pem", "wb") as f:
            f.write(public_key)
        print(f"\n✅ RSA-2048 Key Pair Generated!")
        print(f"📄 Private key saved to: private_key.pem")
        print(f"📄 Public key saved to:  public_key.pem")

    elif args.rsa_command == "encrypt":
        with open("public_key.pem", "rb") as f:
            public_key = f.read()
        encrypted = rsa_cipher.encrypt(args.text, public_key)
        with open("rsa_encrypted.bin", "wb") as f:
            f.write(encrypted)
        print(f"\n✅ RSA Encryption Successful!")
        print(f"🔒 Encrypted data saved to: rsa_encrypted.bin")

    elif args.rsa_command == "decrypt":
        with open("private_key.pem", "rb") as f:
            private_key = f.read()
        with open("rsa_encrypted.bin", "rb") as f:
            encrypted = f.read()
        decrypted = rsa_cipher.decrypt(encrypted, private_key)
        print(f"\n✅ RSA Decryption Successful!")
        print(f"🔓 Decrypted Text: {decrypted}")

def handle_sha(args):
    if args.sha_command == "hash":
        result256 = sha_hash.hash_text(args.text, "sha256")
        result512 = sha_hash.hash_text(args.text, "sha512")
        print(f"\n✅ SHA Hashing Successful!")
        print(f"📝 Input Text:   {args.text}")
        print(f"🔷 SHA-256 Hash: {result256}")
        print(f"🔶 SHA-512 Hash: {result512}")

    elif args.sha_command == "hash-file":
        result = sha_hash.hash_file(args.file)
        print(f"\n✅ File Hashing Successful!")
        print(f"📁 File:         {args.file}")
        print(f"🔷 SHA-256 Hash: {result}")

    elif args.sha_command == "verify":
        match = sha_hash.verify_file(args.file, args.hash)
        print(f"\n{'✅ File is INTACT — hash matches!' if match else '❌ File is TAMPERED — hash mismatch!'}")

def main():
    parser = argparse.ArgumentParser(
        prog="CryptoTool",
        description="🔐 Cryptography CLI Tool — AES, RSA, SHA implemented in Python"
    )
    subparsers = parser.add_subparsers(dest="command", help="Choose algorithm")
    subparsers.required = True

    # --- AES subcommand ---
    aes_parser = subparsers.add_parser("aes", help="AES-256 symmetric encryption")
    aes_sub = aes_parser.add_subparsers(dest="aes_command")
    aes_sub.required = True

    aes_enc = aes_sub.add_parser("encrypt", help="Encrypt text with AES")
    aes_enc.add_argument("--text", required=True, help="Text to encrypt")

    aes_dec = aes_sub.add_parser("decrypt", help="Decrypt AES ciphertext")
    aes_dec.add_argument("--text", required=True, help="Encrypted base64 text")
    aes_dec.add_argument("--key",  required=True, help="Hex key used during encryption")

    # --- RSA subcommand ---
    rsa_parser = subparsers.add_parser("rsa", help="RSA-2048 asymmetric encryption")
    rsa_sub = rsa_parser.add_subparsers(dest="rsa_command")
    rsa_sub.required = True

    rsa_sub.add_parser("generate-keys", help="Generate RSA public/private key pair")
    rsa_enc = rsa_sub.add_parser("encrypt", help="Encrypt text using public key")
    rsa_enc.add_argument("--text", required=True, help="Text to encrypt")
    rsa_sub.add_parser("decrypt", help="Decrypt using private key")

    # --- SHA subcommand ---
    sha_parser = subparsers.add_parser("sha", help="SHA-256/512 hashing")
    sha_sub = sha_parser.add_subparsers(dest="sha_command")
    sha_sub.required = True

    sha_hash_p = sha_sub.add_parser("hash", help="Hash a text string")
    sha_hash_p.add_argument("--text", required=True, help="Text to hash")

    sha_file_p = sha_sub.add_parser("hash-file", help="Hash a file")
    sha_file_p.add_argument("--file", required=True, help="Path to file")

    sha_ver_p = sha_sub.add_parser("verify", help="Verify file integrity")
    sha_ver_p.add_argument("--file", required=True, help="Path to file")
    sha_ver_p.add_argument("--hash", required=True, help="Known hash to compare")

    # Parse and dispatch
    args = parser.parse_args()
    if args.command == "aes":
        handle_aes(args)
    elif args.command == "rsa":
        handle_rsa(args)
    elif args.command == "sha":
        handle_sha(args)

if __name__ == "__main__":
    main()
