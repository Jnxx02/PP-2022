FateSF = [
{
    'Key': '001',
    'Judul Buku': 'Fate/Strange Fake',
    'Author': 'Ryohgo Narita',
}]

YourN = [
{
    'Key': '002',
    'Judul Buku': 'Your Name',
    'Author': 'Makoto Shinkai',
}]

BlueBP = [
{
    'Key': '003',
    'Judul Buku': 'Blue, Painful, and Brittle',
    'Author': 'Sumino Yoru',
}]
kata = ['Menu', 'Thank You', 'Sukses', 'Data tidak Valid']
pinjaman = []
username = input('Username      : ')
password = input('Password      : ')

if username == 'jnxx' and password == '002':
    True
    def menu():
        print()
        print(53*"=")
        print(kata[0].center(53))
        print(53*"-")
        print('0]. Exit')
        print('1]. Pinjam Buku')
        print('2]. Kembalikan Buku')
        print('3]. Daftar Buku')
        print(53*"=")
        print(53*"-")
        pilihan = int(input('> Pilih : '))

        return pilihan

    def pinjam_buku():
        print(53*"-")
        key = input('Key: ')
        print(53*"-")
        if key == '001':
            print(f"Key         : {FateSF[0]['Key']}")
            print(f"Judul Buku  : {FateSF[0]['Judul Buku']}")
            print(f"Author      : {FateSF[0]['Author']}")
            waktupinjaman = input('Lama waktupinjaman : ')
            print(53*"-")
            print(kata[2].center(53))
            print(53*"-")
            pinjaman.append(key)
            print(pinjaman)
        elif key == '002':
            print(f"Key         : {YourN[0]['Key']}")
            print(f"Judul Buku  : {YourN[0]['Judul Buku']}")
            print(f"Author      : {YourN[0]['Author']}")
            waktupinjaman = input('Lama Peminjaman : ')
            print(53*"-")
            print(kata[2].center(53))
            print(53*"-")
            pinjaman.append(key)
            print(pinjaman)
        elif key == '003':
            print(f"Key         : {BlueBP[0]['Key']}")
            print(f"Judul Buku  : {BlueBP[0]['Judul Buku']}")
            print(f"Author      : {BlueBP[0]['Author']}")
            waktupinjaman = input('Lama waktupinjaman : ')
            print(53*"-")
            print(kata[2].center(53))
            print(53*"-")
            pinjaman.append(key)
            print(pinjaman)
        else:
            print(53*"-")
            print(kata[3].center(53))
            print(53*"-")

    def kembalikan_buku():
        print(53*"-")
        print(pinjaman)
        print(53*"-")
        key = input('Key: ')
        print(53*"-")
        if key == '001':
            pinjaman.remove('001')
            print(kata[2].center(53))
            print(53*"-")
        elif key == '002':
            pinjaman.remove('002')
            print(kata[2].center(53))
            print(53*"-")
        elif key == '003':
            pinjaman.remove('003')
            print(kata[2].center(53))
            print(53*"-")

    def daftar_buku():
        print(53*"-")
        print(f"FateSF : {FateSF[0]['Judul Buku']}")
        print(f"YourN  : {YourN[0]['Judul Buku']}")
        print(f"BlueBP : {BlueBP[0]['Judul Buku']}")
        print(53*"-")

    while True:
        pilihan = menu()

        if pilihan == 0:
            print(53*"-")
            print(kata[1].center(53))
            print(53*"-")
            break
        elif pilihan == 1:
            jalankan = pinjam_buku()
        elif pilihan == 2:
            jalankan = kembalikan_buku()
        elif pilihan == 3:
            jalanlan = daftar_buku()
        else:
            continue
else:
    False
    print('Username atau password salah')
