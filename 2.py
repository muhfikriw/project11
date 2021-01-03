import datetime
while True:
    kode = input("Masukkan Kode Member  = ")
    nama = input("Masukkan Nama Member	= ")
    judul = input("Masukkan Judul Buku   = ")

    print("\n")
    pil = input("Ulangi lagi (y/n) = ")
    print("\n")

    if pil == "n":
        sekarang = datetime.date.today()
        batas = datetime.timedelta(days=7)
        pinjam = str(sekarang + batas)
        hariini = str(sekarang)
        data = open("c:/Users/Fikri/Documents/pro11.2.txt", "a+")
        data.write(kode + "|" + nama + "|" + judul + "|" + hariini + "|" + pinjam + "\n")
        data.close
        data = open("c:/Users/Fikri/Documents/pro11.2.txt", "r")
        print("data peminjam :")
        print(data.read())
        data.close()
        break
    elif pil == "y":
        sekarang = datetime.date.today()
        batas = datetime.timedelta(days=7)
        pinjam = str(sekarang + batas)
        hariini = str(sekarang)
        data = open("c:/Users/Fikri/Documents/pro11.2.txt", "a+")
        data.write(kode + "|" + nama + "|" + judul + "|" + hariini + "|" + pinjam + "\n")
        data.close
        continue
    else:
        print("input anda salah")
        exit()