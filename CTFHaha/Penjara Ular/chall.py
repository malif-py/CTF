#!/usr/bin/env python2
import sys
import os
import random
from secret import flag

class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def main():
    secret = random.randint(1, 10000)
    try:
        n = int(input("Masukkan integer: "))
        if(n==secret):
            print flag
        else:
            print "Coba lagi ya" 
    except:
        print "Anda tidak memasukkan integer."

if __name__ == '__main__':
    main()