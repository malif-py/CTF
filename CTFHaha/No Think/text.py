#!/usr/bin/python3
from sys import modules
from Crypto.Util.number import *
import base64
from pwn import *

def intToB64(n): 
    return base64.b64encode(long_to_bytes(n)).decode('utf-8')

def b64ToInt(n):
    return bytes_to_long(base64.b64decode(n.encode('utf-8')))

def ctoken(mainm):
    # Create Token
    global r
    r.sendline(b'1')
    r.sendline(mainm.encode('utf-8'))
    data = r.recvline()
    r.recvlines(7)
    return str(data)[55:-3]

def points():
    global r
    r.sendline(b'3')
    data = r.recvline()
    r.recvlines(7)
    return int(str(data)[30:-17])

def nflag(n):
    global flag
    global mod
    enc_n = b64ToInt(ctoken(intToB64(n)))
    enc_f = b64ToInt(flag)
    return intToB64((enc_n * enc_f) % mod)

def redeem_diff(msg):
    global r
    global rdm
    r.sendline(b'2')
    r.sendline(msg.encode('utf-8'))
    r.recvlines(7)
    v_now = points()
    diff = rdm - v_now
    rdm = v_now
    return diff
def main_p():
    # Inisialisasi
    r = remote('18.142.96.226', 10021)
    data = r.recvline()
    flag = str(data)[18:-3]
    r.recvlines(7)

    # Penentuan N
    e = 0x10001
    enc_2 = b64ToInt(ctoken(intToB64(2)))
    enc_3 = b64ToInt(ctoken(intToB64(3)))
    mod = GCD(2 ** e - enc_2, 3 ** e - enc_3)
    assert pow(2, e, mod) == enc_2


    b_bw = 0
    b_at = mod
    diff = b_at - b_bw
    rdm = points()
    i = 2
    while diff:
        p = redeem_diff(nflag(i)) % 2
        mid = (b_at + b_bw) // 2
        if p == 1:
            b_at = mid + 1
        else:
            b_bw = mid - 1
        i *= 2
        diff = b_at - b_bw
        print(b_bw, b_at)

# Dapet kurang lebih
# 39348467541832741319092410534207421021526001337537380274808822150137286382903789092057105225020955683455353059664