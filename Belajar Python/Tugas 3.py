print('NAMA \t: JONATHAN KWAN')
print('NIM \t: H071221067')
print('=======================')
print('KONVERSI ANGKA KE HURUF')
print('=======================')

Angka = input('Masukkan Angka :')
Angka = eval(Angka)

if Angka == 0 :
    Huruf = "Nol"
elif Angka == 1 :
    Huruf = "Satu"
elif Angka == 2 :
    Huruf = "Dua"
elif Angka == 3 :
    Huruf = "Tiga"
elif Angka == 4 :
    Huruf = "Empat"
elif Angka == 5 :
    Huruf = "Lima"
elif Angka == 6 :
    Huruf = "Enam"
elif Angka == 7 :
    Huruf = "Tujuh"
elif Angka == 8 :
    Huruf = "Delapan"
elif Angka == 9 :
    Huruf = "Sembilan"
else :
    Angka >= 9
    Huruf = 'ERROR'
    
print('Huruf = ', Huruf)