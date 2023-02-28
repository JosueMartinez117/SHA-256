import hashlib

print("---SHA-1 Implementation started---")
sha_1_message = hashlib.sha1(b'Test message to encrypt')
str_hex = sha_1_message.hexdigest()
print("Hash: ")
print(str_hex)

print("---SHA-256 Implementation started---")
sha_256_message = hashlib.sha256(b'Test message to encrypt')
str_hex = sha_256_message.hexdigest()
print("Hash: ")
print(str_hex)

print("---SHA-512 Implementation started---")
sha_512_message = hashlib.sha512(b'Test message to encrypt')
str_hex = sha_512_message.hexdigest()
print("Hash: ")
print(str_hex)