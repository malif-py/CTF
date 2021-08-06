# New Caesar
Dari soal, kita mendapatkan teks tereknripsi

```
ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih
```

Proses enkripsi terdiri dari dua tahap, `encode` dan `shift`. Proses `encode` menghasilkan dua karakter dari satu karakter text berdasarkan karakter text tersebut. Proses `shift` memiliki dua input, `c` dan `k` dengan `c` merupakan sebuah karakter yang telah di-`encode` dan `k` merupakan karakter konstan yang berasal dari alphabet A-P.

Proses dekripsi akan terdiri dari dua tahap, `decode` dan `unshift`. Proses `decode` merupakan inverse dari proses `encode` dan proses `unshift` merupakan inverse dari proses `shift`. Berikut implementasi Python dari kedua fungsi tersebut:

```
def unshift(alp, key):
    num = ord(alp) - LOWERCASE_OFFSET
    t2  = ord(key) - LOWERCASE_OFFSET
    return ALPHABET[(num - t2) % 16]
```

```
def b16_decode(msg):
    text = ''
    for i in range(0, len(msg), 2):
        bin1 = "{0:08b}".format(ord(msg[i]) - LOWERCASE_OFFSET)[4:]
        bin2 = "{0:08b}".format(ord(msg[i + 1]) - LOWERCASE_OFFSET)[4:]
        text += chr(int(bin1 + bin2, 2))
    return text
```

Lalu dengan mem-brute-force key-nya, kita dapatkan flag `picoCTF{et_tu?_0797f143e2da9dd3e7555d7372ee1bbe}`.
