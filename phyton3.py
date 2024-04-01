absen=int(input("Masukan nilai Absen= "))
uts=int(input("Masukan nilai UTS= "))
uas=int(input("Masukan nilai UAS= "))
standar=50
jumlah=absen+uts+uas
rata_rata= jumlah/3
print('Nilai yang diperoleh oleh :')
print(' ')
print('Jumlah nilai yang didapatkan adalah = ', jumlah)
print('Nilai rata-rata yang didapatkan adalah = ', rata_rata)


if rata_rata >= 90:
    predikat = 'A'
elif rata_rata >= 80:
    predikat = 'B+'
elif rata_rata >= 70:
    predikat = 'B'
elif rata_rata >= 60:
    predikat = 'C+'
elif rata_rata >=50:
    predikat = 'C'
else :
    predikat = 'D'
print('Predikat : ',predikat)



if rata_rata>=standar:
    print('"SELAMAT ANDA DINYATAKAN LULUS "')
else:
    print('"ANDA DINYATAKAN TIDAK LULUS, NT BRO NT"')