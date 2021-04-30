import os
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import utils.mylogger as log
import utils.getconfig as cfg
import utils.Exceptions as exc

class Safe_Transfer:
    def __init__(self,fops):
        self._storage=fops
    
    def _encrypt_aes(self,data):
        session_key=get_random_bytes(16)
        cipher_aes=AES.new(session_key,AES.MODE_EAX)
        nonce=cipher_aes.nonce
        ciphedata,tag=cipher_aes.encrypt_and_digest(data)
        return cipherdata,session_key,nonce,tag
    
    def _decrypt_aes(self,data,session_key,nonce,tag):
        cipher_aes=AES.new(session_key,AES.MODE_EAX,nonce=nonce)
        plaindata=cipher_aes.decrypt(data)
        try:
            cipher_aes.verify(tag)
        except ValueError:
            log.raiserror(f"Broken crypto file: {sys.exc_info()[1].args[0]}")
            plaindata=None
            raise
        return plaindata
    
    def _encrypt_rsa(self,data):
        try:
            rsakey=RSA.import_key(open(self._storage.getparams().keypath))
            cipher_rsa=PKCS1_OAEP.new(rsakey)
            data_enc=cipher_rsa.encrypt(data)
        except Exception:
            log.raiserror(f"RSA encrypt error: {sys.exc_info()[1].args[0]}")
            data_enc=None
            raise
        return data_enc
    
    def _decrypt_rsa(self,data):
        try:
            rsakey=RSA.import_key(open(self._storage.getparams().keypath))
            cipher_rsa=PKCS1_OAEP.new(rsakey)
            data_dec=cipher_rsa.decrypt(data)
        except Exception:
            log.raiserror(f"RSA decrypt error: {sys.exc_info()[1].args[0]}")
            data_dec=None
            raise
        return data_dec
    
    def create(self):
        try:
        
        
        
    