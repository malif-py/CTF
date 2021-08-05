#!/usr/bin/env python2
import sys
import os

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
    print "hi!, what's your name?"
    try:
        name = str(input("your name: "))
        print "hi {}! nice to meet you!".format(name)
    except:
        print "your name is bad :("

if __name__ == '__main__':
    main()