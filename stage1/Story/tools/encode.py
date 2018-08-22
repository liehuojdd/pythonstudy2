'''
Python 3.6.3
pip3 install -i https://pypi.douban.com/simple pycryptodomex
'''
from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex

AES_LENGTH = 16

class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_ECB
        self.cryptor = AES.new(self.pad_key(self.key).encode(), self.mode)

    # if text len not 16, add space to 16
    def pad(self,text):
        while len(text) % AES_LENGTH != 0:
            text += ' '
        return text

    # if pad key len not 16, add to 16
    def pad_key(self,key):
        while len(key) % AES_LENGTH != 0:
            key += ' '
        return key

    def encrypt(self, text):

        # change encode str to byte
        # print(self.pad(text))
        self.ciphertext = self.cryptor.encrypt(self.pad(text).encode())
        # change decode str to 16 band
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        plain_text = self.cryptor.decrypt(a2b_hex(text)).decode()
        return plain_text.rstrip(' ')