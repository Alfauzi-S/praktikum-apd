# def perkenalan():
#     print("Halo, aku Nabil")

# perkenalan()

# def salam():
#     print("Halo, Ridho")

# def kali():
#     x = 5 * 5
#     print(x)

# salam()
# salam()
# salam()
# kali()
# kali()
# kali()

# def nama_fungsi(parameter):
#     print(parameter)

# nama_fungsi("Halo, ali")


# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print('Luas persegi panjang adalah:', luas)

# luas_persegi_panjang(4, 5)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# print ("Luas persegi :", luas_persegi(8))

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     print ("Luas Persegi = ", luas)
#     return luas

# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)

# luas_persegi(4)
# volume_persegi(8)

# Nama = "Hambali"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar" 

# def info():
#     Nama = "Informatika"
#     Mata_Kuliah = "Logika Informatika"
#     print("Prodi (dalam info):", Nama)
#     print("Mata Kuliah (dalam info):", Mata_Kuliah)

# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)

# info()

# fungsi memanggil dirinya sendiri sampai kondisi tertentu
# def faktorial(n):
#     if n == 1 or n == 0:
#         print(n)
#         return 1
#     else:
#         print(n)
#         return n * faktorial(n - 1)
    
# hasil = faktorial(7)
# print(f"Hasil dari 7! adalah: {hasil}")

# film = []

# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#     for indeks in range(len(film)):
#         print(indeks, "|", film[indeks])

# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")

# def show_menu():
#     while True:
#         print ("\n")
#         print ("----------- MENU---------- ")
#         print ("[1] Show Data")
#         print ("[2] Insert Data")
#         print ("[3] Edit Data")
#         print ("[4] Delete Data")
#         print ("[5] Exit")
#         menu = input("PILIH MENU> ")
#         print ("\n")
#         if menu == "1":
#             show_data()
#         elif menu == "2":
#             insert_data()
#         elif menu == "3":
#             edit_data()
#         elif menu == "4":
#             delete_data()
#         elif menu == "5":
#             exit()
#         else:
#             print ("Salah pilih!")

# show_menu()

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# # Fungsi untuk menampilkan semua data
# film = []
# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#     for indeks in range(len(film)):
#         print(indeks, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")

#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     else:
#         print('Tidak ada di menu')


# while True():
#     show_menu()

# angka = int(input('Masukkan Angka : '))
# print(angka) #input 'Hai'

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(angka)

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')
# finally :
#     print('Blok Try Selesai')

# try:
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as e:
#     print(e)
# else :
#     print(f'Username yang kamu buat : {usn}')
# finally :
#     print('Proses Pembuatan Username Selesai')

# Buatlah Error Handling untuk melakukan input nama dengan kriteria tidak boleh kosong atau hanya berisi spasi saja.

# try:
#     nama = input('Masukkan Nama : ')
#     if nama.strip() == '':
#         raise ValueError('Nama tidak boleh kosong atau hanya berisi spasi saja')
# except ValueError as e:
#     print(e)
# else :
#     print(f'Nama yang kamu input : {nama}')

# Buatlah Error Handling untuk melakukan input password dengan kriteria password minimal memiliki panjang 8 karakter dan wajib ada angka. Berikan keterangan juga kriteria mana yang tidak terpenuhi.

try: 
    password = input('Masukkan Password : ')
    if len(password) < 8:
        raise ValueError('Password minimal memiliki panjang 8 karakter')
    if not any(char.isdigit() for char in password): # mengecek apakah ada angka di dalam password
        raise ValueError('Password wajib mengandung minimal satu angka')
except ValueError as e:
    print(e)
else :
    print(f'Password berhasil dibuat {password}')

# Buatlah Error Handling jika key tidak dapat ditemukan pada dictionary dan berikan
# pesan “Kode barang tidak ditemukan

# data_barang = {
#     '0' : 'Pensil',
#     '1' : 'Buku Tulis',
#     '2' : 'Penghapus'
# }

# try:
#     kode = input('Masukkan Kode Barang : ')
#     print(f'Barang dengan kode {kode} adalah {data_barang[kode]}')
# except KeyError:
#     print('Kode barang tidak ditemukan')    
