#!/usr/bin/env python
from os import name
import sys

class RC4:

    def __init__( self, key):
        self.key = key
        self.init()

    def init(self):
        self.S = self.KSA()
        self._keystream = self.PRGA(self.S)


    def KSA(self):
        key = self.key
        keylength = len(key)

        S = [i for i in range(256)]

        j = 0

        for i in range(256):
            j = (( j ) + S[i] + int( key[i % keylength] )) % 256
            S[i], S[j] = S[j], S[i]  # swap

        return S


    def PRGA(self,S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256

            S[i], S[j] = S[j], S[i]  # swap

            K = S[(S[i] + S[j]) % 256]

            yield K

    def keystream(self):
        self.init()
        return self._keystream


    def getKeystream(self,n):
        self.init()
        res=""
        for i in range(0,n):
            res += format(next( self._keystream ), '#04x')[2:]
        return res

def change_to_be_hex(s):
    return int(s,base=16)

if __name__ == "__main__":
    a = RC4('124412412413')
    stream = a.keystream()
    for i, char in enumerate( "aabcdabcdabcdabcdabcdabcdabcdabcdbcd" ):
        a = change_to_be_hex(char)
        b = next( stream )
        print(hex( a ^ b ), end='')

    # print(change_to_be_hex( a.getKeystream(1) ));
    # print(next(stream))
    # print(next(stream))
    # print(next(stream))
    # print(next(stream))
