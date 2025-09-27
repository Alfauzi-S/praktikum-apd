# nilai = 75
# if nilai = 70:
#     print("Anda Lulus!") # Blok if dijalankan karena kondisi True
# else:
#     print("Anda Belum Lulus.")

# umur = (input("masukkan umur anda: "))

# if umur < 13:
#     katagori = "anak-anak"
# elif umur < 18:
#     katagori = "remaja"
# elif umur < 65:
#     katagori = "dewasa"
# else:
#     katagori = "lansia"

# print(katagori)

# nilai = 70
# status = "Lulus" if nilai >= 70 else "Tidak Lulus"
# print(status)

# tinggi = int(input("Masukkan tinggi badan Anda (cm): "))

# if tinggi >= 145:
#     print("Anda boleh menaiki wahana Roller Coaster Tornado Dufan.")
# else:
#     print("Maaf, Anda tidak boleh menaiki wahana tersebut.")

# harga = int(input("Masukkan harga barang: "))

# if harga >= 100000:
#     diskon = 0.20 * harga
# elif harga >= 50000:
#     diskon = 0.10 * harga
# else:
#     print("tidak ada diskon")

# print(harga - diskon)


print("kalkulator bangun ruang")
print("1. kubus")
print("2. balok")
print("3. tabung")

pilihan = int(input("masukkan pilihan anda: "))

if pilihan == 1:
    sisi = float(input("masukkan sisi: "))
    volume = sisi * sisi * sisi
    print("volume kubus adalah: ", volume)

elif pilihan == 2:
    panjang = float(input("masukkan panjang: "))
    lebar = float(input("masukkan lebar: "))
    tinggi = float(input("masukkan tinggi: "))
    volume = panjang * lebar * tinggi
    print("volume balok adalah: ", volume)

elif pilihan == 3:
    jari_jari = float(input("masukkan jari-jari: "))
    tinggi = float(input("masukkan tinggi: "))
    volume = 3.14 * jari_jari * jari_jari * tinggi
    print("volume tabung adalah: ", volume)