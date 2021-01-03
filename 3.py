import datetime
f = open("c:/Users/Fikri/Documents/pro11.2.txt", "r")
data  = []
data2 = []
data3 = []
data4 = []
data5 = []

for line in f:
    spl = line.split("|")
    data.append(spl[0])
    data2.append(spl[1])
    data3.append(spl[2])
    data4.append(spl[3])
    data5.append(spl[4].strip())

pil = str(input("Masukkan kode member yang mau dicari : "))
if pil in data:
    ketemu = True
    a = data.index(pil)
    NOW = datetime.datetime.now()
    x = data5[a]
    from datetime import datetime
    x = datetime.strptime(x, "%Y-%m-%d")
    rumus = x - NOW
    from datetime import *
    pengembalian = datetime.date(NOW)
    maksimal = datetime.date(x)
else:
    print("data tidak ditemukan")
    exit()
if ketemu == True:
    rumus = datetime.date(NOW) - maksimal
    rumus = int(rumus.days)
    bayardenda = 0
    if rumus >= 0:
        bayardenda = 2000 *(rumus)
        rumus = abs(rumus)
    elif rumus <= 0:
        rumus = 0

    print("\nData Peminjaman Buku\n"
         "\nKode Member                    : ",data[a],
         "\nNama Member                    : ",data2[a],
         "\nJudul Buku                     : ",data3[a],
         "\nTanggal Mulai Peminjaman       : ",data4[a],
         "\nTanggal Maks Peminjaman        : ",data5[a],
         "\nTanggal Pengembalian           : ",pengembalian,
         "\ntelat                          : ", rumus,"Hari"
         "\nTotal denda                    :  Rp.",bayardenda)

else:
    print("data tidak ditemukan")
