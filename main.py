import os
os.system("cls")


def tarik():
     saldoUser = saldo[rekening]
     print(f"Saldo anda = {saldoUser}")
     seratus = 100000
     duaratus = 200000
     limaratus =500000
     print(f"1 Rp,{seratus}\n2. Rp{duaratus}\n3. Rp{limaratus}")
     tarik = int(input("Masukkan jumlah yang ingin anda tarik\t: "))  
     if saldoUser < seratus or saldoUser < duaratus or saldoUser < limaratus:
          print("saldo anda tidak cukup")
     elif tarik == 1:
          sisaSaldo = saldoUser - seratus
          print("anda berhasil menarik sebanyak 100k")
          print(f"sisa saldo {sisaSaldo}")
     elif tarik == 2:
          sisaSaldo = saldoUser - duaratus
          print("anda berhasil menarik sebanyak 200k")
          print(f"sisa saldo {sisaSaldo}")
     elif tarik == 3:
          sisaSaldo = saldoUser - limaratus
          print("anda berhasil menarik sebanyak 500k")
          print(f"sisa saldo {sisaSaldo}")

def tambahTabungan():
     print(f"Saldo anda = {saldoUser}") 
     seratus = 100000
     duaratus = 200000
     limaratus =500000
     print(f"1 Rp,{seratus}\n2. Rp{duaratus}\n3. Rp{limaratus}")
     menabung = int(input("Masukkan jumlah yang ingin anda tabung\t: "))
     if menabung == 1:
          sisaSaldo = saldoUser + seratus
          print("anda berhasil menabung 100k")
          print(f"sisa saldo {sisaSaldo}")
     elif menabung == 2:
          sisaSaldo = saldoUser + duaratus
          print("anda berhasil menabung 200k")
          print(f"sisa saldo {sisaSaldo}")
     elif menabung == 3:
          sisaSaldo = saldoUser + limaratus
          print("anda berhasil menabung 500k")
          print(f"sisa saldo {sisaSaldo}")

def transfer():
     print(f"Saldo anda = {saldoUser}") 
     seratus = 100000
     duaratus = 200000
     limaratus =500000
     print(f"1 Rp,{seratus}\n2. Rp{duaratus}\n3. Rp{limaratus}")
     jumlah = int(input("Masukkan jumlah yang ingin anda transfer\t: "))
     no_rek = int(input("Masukkan nomor rekening tujuan\t: "))
     transfer = saldo[no_rek]
     if no_rek in saldo:
          if jumlah == 1:
               kirim = transfer + seratus
               transferNow = kirim
               sisaSaldo = saldoUser - seratus
               print(f"anda berhasil transfer 100k ke {no_rek}")
               print(f"sisa saldo anda : {sisaSaldo}")
               # print(f"Saldo yang anda kirimkan {transferNow}")
          elif jumlah == 2:
               kirim = transfer + duaratus
               transferNow = kirim
               sisaSaldo = saldoUser - duaratus
               print(f"anda berhasil transfer 200k ke {no_rek}")
               print(f"sisa saldo {sisaSaldo}")
               # print(f"Saldo yang anda kirimkan {transferNow}")
          elif jumlah == 3:
               kirim = transfer + limaratus
               transferNow = kirim
               sisaSaldo = saldoUser - limaratus
               print(f"anda berhasil transfer 500k ke {no_rek}")
               print(f"sisa saldo {sisaSaldo}")
               # print(f"Saldo yang anda kirimkan {transferNow}")
     else:
          print("Rekening tidak ada silahkan coba lagi")



saldo = {
     1234 : 1200000,
     4321 : 500000,
     9898 : 250000,
     2323 : 10000
}

print("Selamat datang di Bank GTG")
rekening = int(input("Masukkan no rekening anda\t: "))
if rekening in saldo:
     saldoUser = saldo[rekening]
     def task():
          if rekening in saldo:
               print("1.Tarik uang")
               print("2.Menabung")
               print("3.Transfer")
               user = int(input("Apa yang ingin anda lakukan\t: "))
               if user == 1:
                    tarik()
               elif user == 2:
                    tambahTabungan()
               elif user == 3:
                    transfer()
               else:
                    print("Masukkan sesuai yang tertera!")
               # print(f"Saldo anda = {saldo[rekening]}")
          else:
               print("rekening tidak ada silahkan ulangi lagi")

     task()
     while True:
          lanjut = int(input("Mau melanjutkan transaksi?\n1. Ya\n2.Tidak\n: "))
          if lanjut == 1:
               task()
          else:
               print("Terimakasih")
               break
else:
     print("Rekeing tidak ada!")