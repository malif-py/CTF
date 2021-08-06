# Shop
Diberikan `nc mercury.picoctf.net 37799` . Saat dibuka, merupakan aplikasi shop dengan item kedua `Fruitful Flag` seharga 100 koin sedangkan kita hanya diberikan 40 koin. Setelah testing lebih lanjut, ternyata program menerima angka negatif sebagai jumlah barang, sehingga dapat menambah jumlah koin.

```
Welcome to the market!
=====================
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-6

You have 100 coins
	Item		Price	Count
(0) Quiet Quiches	10	18
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 53 57 49 97 56 57 53 97 125]
```

Diberikan sebuah flag yang jika diconvert dari decimal, didapatkan flag `picoCTF{b4d_brogrammer_591a895a}`.
