# from cryptography.fernet import Fernet


# key = Fernet.generate_key()

# with open('secret.key', 'wb') as key_file:
#     key_file.write(key)



# def load_key():
#     return open('secret.key', 'rb').read()

# key = load_key()

# f = Fernet(key)
# message = 'This is a secret message.'.encode()
# encrypted_message = f.encrypt(message)
# print(f'Encrypted message here: {encrypted_message}')


# decrypt_message = f.decrypt(encrypted_message).decode()
# print(f'Decrypted message here: {decrypt_message}')


# import hashlib

# m = hashlib.sha256()
# m.update(b'Nobody inspect')
# m.update(b'The spamish repitition')
# print(m.digest())
# print(m.hexdigest())
