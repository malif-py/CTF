# MacroHard WeakEdge
Diberikan sebuah file `.pptm`. Jika dibuka, hanya berisi presentasi biasa. Pencarian menggunakan tools seperti `file`, `cat`, dan `binwalk` tidak membuahkan hasil. Setelah dicari lebih lanjut, file `.pptm` menggunakan `.zip` dan `.xml` lalu dikompres menjadi satu. Jika kita ekstrak, akan didapatkan beberapa file.

```
└─$ ls -la
total 132
drwxr-xr-x 5 alif alif   4096 Aug  6 16:24  .
drwxr-xr-x 3 alif alif   4096 Aug  6 16:24  ..
-rw-r--r-- 1 alif alif 100093 Aug  6 16:24  0.zip
-rw-r--r-- 1 alif alif  10660 Aug  6 16:24 '[Content_Types].xml'
drwxr-xr-x 2 alif alif   4096 Aug  6 16:24  docProps
drwxr-xr-x 7 alif alif   4096 Aug  6 16:24  ppt
drwxr-xr-x 2 alif alif   4096 Aug  6 16:24  _rels

```

Setelah melihat-lihat isi file, didapatkan sebuah file dalam `./ppt/slideMasters` yang bernama `hidden`. Di dalam file itu, terdapat sebuah text yang unik.

```
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```

Dengan mengonversi teks ini dari `Base64` akan menghasilkan

```
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```

flag : `picoCTF{D1d_u_kn0w_ppts_r_z1p5}`.
