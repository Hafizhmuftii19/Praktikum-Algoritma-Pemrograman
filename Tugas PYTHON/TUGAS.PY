total = 0
barang = []
harga = []

while True:

    print("======= TOKO VAPERS HAFIZH =======\n")
    print("========== JL SWAKARSA 1 PONDOK KELAPA JAKTIM ============\n")

    print("""Daftar menu LIQUID\n
    1. ES TEH MANIS 60ML \t 80000
    2. ES TEH LECI 60ML \t 80000
    3. LUNAR HEXOM 60ML \t 130000
    4. NIKMAT 60L       \t 135000
    5. MANGO KHALIFAH 60ML \t 100000
    """ )


    Nama = input("Masukkan nama anda :")
    Alamat = input("Masukkan alamat anda :")
    Telepon = input("Masukkan telepon anda :")
    Tanggal = input("Masukkan tanggal pembelian :")
    kode = int(input("pilih menu : "))


    if kode == 1:
        barang.append('ES TEH MANIS 60L')
        harga.append('80000')
        total += 80000
    elif kode == 2:
        barang.append('ES TEH LECI 60L')
        harga.append('80000')
        total += 80000
    elif kode == 3:
        barang.append('LUNAR HEXOM 60ML')
        harga.append('130000')
        total += 130000
    elif kode == 4:
        barang.append('NIKMAT 60ML')
        harga.append('135000')
        total += 135000
    elif kode == 5:
        barang.append('MANGGO KHALIFAH 60ML')
        harga.append('100000')
        total += 100000
    else:
        print('kode tidak valid')

    lanjut = input('lanjut belanja (y/t) : ')
    if lanjut == 't' :
        print("")
        print('Nama :', Nama)
        print('Alamat :', Alamat)
        print('Telepon :', Telepon)
        print('Tanggal :', Tanggal)
        print('Barang yang dibeli : ', barang)
        print('Total yang harus dibayar : ', total, '\n')
        uang = int(input('Masukkan uang pembayaran : '))
        if uang > total:
            print('Kembaliannya : ', uang - total)
        elif uang == total:
            print('Uang pas')
        else:
            print('Uangnya kurang', uang - total)
        break 
    print('Harga barangnya : ', harga)