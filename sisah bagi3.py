'''Buatlah program yang dapat menerima inputan berupa angka 
dengan ketentuan sebagai berikut:
1. Angka yang dimasukkan melalui input adalah batas atas 
angka
2. Program menampilkan jumlah angka yang habis dibagi 3
Contoh angka yang diinput adalah 10, maka jawabannya 
adalah 3, karena ada 3 angka yang habis dibagi 3 yaitu 3, 6 
dan 9 '''

angka = int(input("angka : " ))

for i in range (3,angka+1,3):
	print(i)
