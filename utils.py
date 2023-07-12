from cryptography.fernet import Fernet
import config

def decrypt_api_keys(msg):
  # Load secret from config, encode it to bytes
  key = config.fernet_key.encode('ascii')
  # Generate the actual key from the secret
  f = Fernet(key)

  decrypted = f.decrypt(msg)
  return decrypted.decode('ascii')