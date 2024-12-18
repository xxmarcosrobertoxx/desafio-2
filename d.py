from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# Configuração do AES
BLOCK_SIZE = 16
KEY_SIZE = 32  # tamanho da chave AES (32 bytes para AES-256)
KEY = get_random_bytes(KEY_SIZE)  # gera uma chave aleatória

def encrypt_file(file_path, key):
    # Leitura do arquivo
    with open(file_path, 'rb') as f:
        data = f.read()

    # Criação do objeto de criptografia AES
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data, BLOCK_SIZE))
    
    # Gravação do arquivo criptografado
    with open(file_path + '.enc', 'wb') as f:
        f.write(cipher.iv)  # escreve o vetor de inicialização (IV)
        f.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    # Leitura do arquivo criptografado
    with open(encrypted_file_path, 'rb') as f:
        iv = f.read(BLOCK_SIZE)  # lê o vetor de inicialização (IV)
        encrypted_data = f.read()
    
    # Criação do objeto de decriptografia AES
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), BLOCK_SIZE)
    
    # Gravação do arquivo descriptografado
    decrypted_file_path = encrypted_file_path.replace('.enc', '')
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

# Exemplo de uso
file_path = 'arquivo.txt'
encrypt_file(file_path, KEY)  # Criptografa o arquivo
decrypt_file(file_path + '.enc', KEY)  # Decriptografa o arquivo
