# # # # # pertemuan 6
# # # # # set dan dictionary

# # # # # Membuat set
# # # # buah = {"apel", "jeruk", "mangga", "apel"}
# # # # print(buah)

# # # # angka_ganjil = {1, 3, 5, 7, 9}
# # # # for angka in angka_ganjil:
# # # #     print (angka)


# # # # Daftar_buku = {
# # # # "novel" : "Bumi Manusia",
# # # # "Buku2" : "Laut Bercerita"
# # # # }

# # # # print(Daftar_buku["Buku1"])
# # # # print(Daftar_buku)

# # # # List_game = dict(GTA 5 : "Open World", Valorant : "FPS", Honkai Star Rail :
# # # # "RPG")

# # # #key:value

# # # # Biodata = {
# # # #     "Nama" : "Ananda Daffa Harahap",
# # # #     "NIM" : 2409106050,
# # # #     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# # # #     "Mahasiswa_Aktif" : True,
# # # #     "Social Media" : {
# # # #         "Instagram" : "daffahrhap"
# # # #     }
# # # # }

# # # # # print(Biodata)

# # # # # hanya print key saja
# # # # # ,items() -> untuk mengambil key dan value
# # # # # for i in Biodata:
# # # # #     print(i)

# # # # # # print key dan value
# # # # # for i, j in Biodata.items():
# # # # #     print(i, j)
    
# # # # print(f"nama saya adalah {Biodata['nama']}")
# # # # print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# # # # print(f"nama saya adalah {Biodata.get('Nama')}")
# # # # print(Biodata.get("Nama"))

# # # # print(Biodata.get("Nama"))
# # # # print(Biodata.get("Alamat"))
# # # # print(Biodata.get("Alamat", "Key tersebut tidak ada"))

# # # # Nilai = {
# # # #     "Matematika": 80,
# # # #     "Bahasa Indonesia": 90,
# # # #     "B. Inggris": 81,
# # # #     "Kimia": 78,
# # # #     "Fisika": 80
# # # # }
# # # # # Tanpa menggunakan items()
# # # # for i in Nilai:
# # # #     print(i)
# # # # print("") # pemisah
# # # # # Menggunakan items()
# # # # for i, j in Nilai.items():
# # # #     print(f"Nilai {i} anda adalah {j}")

# # # # Film = {
# # # # "Avenger Endgame" : "Action",
# # # # "Sherlock Holmes" : "Mystery",
# # # # "The Conjuring" : "Horror"
# # # # }

# # # # print(Film)
# # # # Film.update({"amibarata" : "Detective"})
# # # # Film["The Conjuring"] = "Comedy"
# # # # Film.update({"Avenger Endgame" : "Thriller"})
# # # # print(Film)

# # # data = {
# # # "Nama" : "Daffa",
# # # "Umur" : 19,
# # # "Jurusan" : "Informatika"
# # # }
# # # #SebeLum Dihapus
# # # print(data)

# # # # del data["Nama"]
# # # cache = data.pop("Nama")


# # # #Setelah diuhah
# # # print(data)

# # # #memanggil data yang telah dihapus
# # # print(data.get("Nama"))


# # # print(cache)


# # Musik = {
# #     "The Chainsmoker": ["All we Know", "The Paris"],
# #     "Alan Walker": ["Alone", "Lily"],
# #     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
# #     'Paramore' : ["Misery Business", "Ain't It Fun", ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# # }

# # print(Musik['Paramore'][2][1][1])
# # print(Musik['The Chainsmoker'][0])
# # print(Musik['Neffex'][1][1])



# # angka ={11,10,12}
# # b = {12,13,14}
# # # union
# # c = angka | b
# # # AND
# # D = angka & b
# # # OR
# # E = angka ^ b
# # print(c)
# # print(D)
# # print(E)


# # print(type(angka))

# # #set kosong
# # angka = set()
# # print(type(angka))


# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
# print(f"Musik milik {i} adalah : ")
# for song in j:
# print(song)
# print("")


# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }

# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
#     print("")



Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Fisika" : 80
}
#menggunakan keys
for i in Nilai.keys():
    print(i)
print("") #pemisah

for i in Nilai.values():
    print(i)

print(Nilai)
print("") #pemisah

print("Nilai :", Nilai.setdefault("Kimia",70))
print("")
print(Nilai)