# pertemuan 5
# list and tuple

# praktikum =['apd',['orsikom', 'jarkom'],['rpl','basis data', 'struktur data']]
# print(praktikum[1][1])

# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# print(praktikum)
# print(praktikum[1])
# print(praktikum[4][0])
# for i in praktikum :
#     print(i)

# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)
# studyclub.append("Web")
# print(studyclub)
# studyclub.insert(2,"Web")
# print(studyclub)
# studyclub[2] = "AI"
# print(studyclub)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# del matakuliah[2]
# print(matakuliah)

# pop disimpan remove tidak
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# matakuliah.remove('Kalkulus')
# print(matakuliah) 

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# print(matakuliah)
# ambil_matkul = matakuliah.pop(2)
# print(matakuliah)
# print(ambil_matkul)

# Slicing
# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
# 'Orsikom','Basis Data']
# print(matakuliah[1:6:2])

# angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(angka[0:10:2]) #start stop step

# a = [1, 2, 3]
# b = [4, 5, 6]
# # menggabungkan kedua list
# c = a + b
# print(c)

# a = ["teknik", "informatika"]
# # mengulang isi list 3 kali
# c = a*3
# print(c)

# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]

# for i in mahasiswa: # 0,1
#     for j in i : # 0,2
#         print (j)

# tuple = ('kata')
# print(type(tuple))
# tuple = ('kata',)
# print(type(tuple))

# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota)


# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota[1])
# print(anggota[-1])
# print(anggota[5][0])

tugas = ('rangkuman', 'arduino','scrapping')
(PTI, orsikom, basisdata) = tugas # key
print(PTI)
print(orsikom)
print(basisdata)

barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
(segitiga, *bulat, kotak) = barang
print(segitiga)
print(bulat)
print(kotak)