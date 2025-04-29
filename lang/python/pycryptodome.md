### pycryptodome

- 安装: pip install pycryptodome

- 对称加密
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# AES encryption function
def aes_encrypt(plain_text, key):
    # Create an AES encryption object using the CBC (Cipher Block Chaining) mode, which can enhance the security of encryption
    cipher = AES.new(key, AES.MODE_CBC)
    # Initialization Vector (IV), used to increase the randomness of encryption
    iv = cipher.iv
    # Pad the plaintext to make its length an integer multiple of AES.block_size
    padded_plain_text = pad(plain_text.encode(), AES.block_size)
    # Encrypt the padded plaintext
    cipher_text = cipher.encrypt(padded_plain_text)
    # Return the initialization vector and the encrypted ciphertext, because the initialization vector is required for decryption
    return iv + cipher_text

# AES decryption function
def aes_decrypt(cipher_text, key):
    # Extract the initialization vector
    iv = cipher_text[:AES.block_size]
    # Create an AES decryption object using the extracted initialization vector and the key
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the ciphertext and remove the padding part
    plain_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    # Convert the decrypted byte data into a string and return it
    return plain_text.decode()

# Generate a 128-bit key (16 bytes)
key = os.urandom(16)
plain_text = "Hello, World!"
cipher_text = aes_encrypt(plain_text, key)
decrypted_text = aes_decrypt(cipher_text, key)

print("Before AES encryption:", plain_text)
print("After AES encryption:", cipher_text.hex())
print("After AES decryption:", decrypted_text)
```

- 非对称加密
```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Function to generate RSA key pair
def generate_rsa_keys():
    # Generate a 2048-bit RSA key pair. The longer the key length, the higher the security
    key = RSA.generate(2048)
    # Export the private key
    private_key = key.export_key()
    # Export the public key
    public_key = key.publickey().export_key()
    # Save the private key to a file
    with open("private.pem", "wb") as f:
        f.write(private_key)
    # Save the public key to a file
    with open("public.pem", "wb") as f:
        f.write(public_key)

# RSA encryption function
def rsa_encrypt(plain_text, public_key_path):
    # Read the public key file
    with open(public_key_path, "rb") as f:
        public_key = RSA.import_key(f.read())
    # Create a PKCS1_OAEP encryption object using the public key
    cipher = PKCS1_OAEP.new(public_key)
    # Encrypt the plaintext
    cipher_text = cipher.encrypt(plain_text.encode())
    return cipher_text

# RSA decryption function
def rsa_decrypt(cipher_text, private_key_path):
    # Read the private key file
    with open(private_key_path, "rb") as f:
        private_key = RSA.import_key(f.read())
    # Create a PKCS1_OAEP decryption object using the private key
    cipher = PKCS1_OAEP.new(private_key)
    # Decrypt the ciphertext
    plain_text = cipher.decrypt(cipher_text)
    return plain_text.decode()

# Generate RSA key pair when running for the first time
# generate_rsa_keys()
public_key_path = "public.pem"
private_key_path = "private.pem"
plain_text = "Hello, RSA!"
cipher_text = rsa_encrypt(plain_text, public_key_path)
decrypted_text = rsa_decrypt(cipher_text, private_key_path)

print("Before RSA encryption:", plain_text)
print("After RSA encryption:", cipher_text.hex())
print("After RSA decryption:", decrypted_text)
```
- hash + slat
```python
import hashlib
import os

# Salted hashing function
def salted_hash(password, salt=None):
    if salt is None:
        # Generate a 16-byte salt value (32-bit hexadecimal string)
        salt = os.urandom(16).hex()
    # Concatenate the password and the salt value
    combined = password + salt
    # Use the SHA - 256 hash algorithm to calculate the hash value of the concatenated string
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    return salt, hashed

# Password verification function
def verify_password(password, salt, hashed_password):
    # Concatenate the input password and the salt value obtained from the database
    combined = password + salt
    # Calculate the hash value of the concatenated string
    new_hash = hashlib.sha256(combined.encode()).hexdigest()
    # Compare whether the calculated hash value is the same as the hash value stored in the database
    return new_hash == hashed_password

# Process the password during registration
password = "user_password"
salt, hashed_password = salted_hash(password)
print("Salt value:", salt)
print("Salted hash value:", hashed_password)

# Verify the password during login
input_password = "user_password"
is_valid = verify_password(input_password, salt, hashed_password)
print("Password verification result:", is_valid)
```