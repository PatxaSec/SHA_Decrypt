#!/bin/python3
#Author: PatxaSec

import hashlib
import base64
import os, sys
from tqdm import tqdm

class PasswordEncryptor:

    def __init__(self, hash_type="SHA", pbkdf2_iterations=10000):
        self.hash_type = hash_type
        self.pbkdf2_iterations = pbkdf2_iterations

    def crypt_bytes(self, salt, value):
        if not salt:
          salt = base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8')
        hash_obj = hashlib.new(self.hash_type)
        hash_obj.update(salt.encode('utf-8'))
        hash_obj.update(value)
        hashed_bytes = hash_obj.digest()
        result = f"${self.hash_type}${salt}${base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')}"
        return result

    def get_crypted_bytes(self, salt, value):
      try:
        hash_obj = hashlib.new(self.hash_type)
        hash_obj.update(salt.encode('utf-8'))
        hash_obj.update(value)
        hashed_bytes = hash_obj.digest()
        return base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')
      except hashlib.NoSuchAlgorithmException as e:
          raise Exception(f"Error while computing hash of type {self.hash_type}: {e}")
if len(sys.argv) != 4:
    print("Usage: python3 sha_dec.py <salt> <hash> <wordlist>")
    sys.exit(1)

hash_type = "SHA1"
salt = sys.argv[1]
search = sys.argv[2]
wordlist = sys.argv[3]

encryptor = PasswordEncryptor(hash_type)
total_lines = sum(1 for _ in open(wordlist, 'r', encoding='latin-1'))
with open(wordlist, 'r', encoding='latin-1') as password_list:
    for password in tqdm(password_list, total=total_lines, desc="Processing"):
        value = password.strip()
        hashed_password = encryptor.crypt_bytes(salt, value.encode('utf-8'))
        if hashed_password == search:
            print(f'Found Password:{value}, hash:{hashed_password}')
            break