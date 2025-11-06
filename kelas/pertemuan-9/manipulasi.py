# import numpy as np
# import pandas as pd

# # # arr = np.array([1,2,3,4,5])
# # # print(arr)
# # # print(type(arr))

# # # arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# # # print(arr2d)

# # # arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# # # print('elemen ke dua dari row 1\n', arr[0, 1])

# # # # Array berisi angka 1 (satu)
# # # ones = np.ones((3, 2)) # Membuat matriks 3x2 berisi 1
# # # print(f"\nArray satu ukuran 3x2: \n{ones}")

# # # # np.arange(start, stop, step)
# # # rentang = np.arange(0, 10, 2) # Angka 0 sampai 9, lompat 2
# # # print(f"\nArray Arange: \n{rentang}")

# # # matrik_a = np.array([
# # #     [1, 2, 3],
# # #     [4, 5, 6],
# # #     [7, 8, 9]])

# # # matrik_b = np.array([
# # #     [3, 2, 1],
# # #     [6, 5, 4],
# # #     [9, 8, 7]])

# # # hasil = matrik_a + matrik_b
# # # print(hasil)

# # # #tanpa numpy
# # # matrik_a = [
# # #     [1, 2, 3],
# # #     [4, 5, 6],
# # #     [7, 8, 9]]

# # # matrik_b = [
# # #     [3, 2, 1],
# # #     [6, 5, 4],
# # #     [9, 8, 7]]

# # # hasil = []
# # # for i in range(len(matrik_a)):
# # #     baris_hasil = []
# # #     for j in range(len(matrik_a[0])):
# # #         jumlah_elemen = matrik_a[i][j] + matrik_b[i][j]
# # #         baris_hasil.append(jumlah_elemen)
# # #     hasil.append(baris_hasil)

# # # print(hasil)

# # # data awal string
# # data_awal = """NIM,Nama,Angkatan
# # 23001,Budi Santoso,2023
# # 23002,Ani Wijaya,2023
# # 23003,Citra Lestari,2023
# # 23004,Doni Firmansyah,2023
# # """

# # try:
# #     with open("mahasiswa.csv", "w") as f:
# #         f.write(data_awal) #khusus string
# #     print("File 'mahasiswa.csv' berhasil dibuat!")
# # except Exception as e:
# #     print(f"Gagal membuat file: {e}")

# # df = pd.read_csv("mahasiswa.csv")
# # # print(df)



# # # dataAwal = {
# # #     'NIM': [2409106046],
# # #     'Nama': ['st'],
# # #     'Angkatan': ['2024']
# # # }

# # # try:
# # #     df = pd.DataFrame(dataAwal) #ubah dictionary menjadi dataframe
    
# # #     df.to_csv("mahasiswa2.csv", index=True)# index=False penting agar nomor index (0) tidak ikut disimpan
# # #     print("File 'mahasiswa2.csv' berhasil dibuat dengan data!")

# # # except Exception as e:
# # #     print(f"Gagal membuat file: {e}")

# # # df1 = pd.read_csv("mahasiswa2.csv")
# # # print(df1)


# # # print(df.head()) #menampilkan 5 teratas, jika menulis df.head(3) berarti menampilkan 3 teratas
# # # print(df.tail())

# # # print(df.info()) #buat ngeliat informasi ringkas

# # # # Data Sebelum di update
# # # print("Data Sebelum di Update")
# # # print(df.head())

# # # # mengubah pada index 1 di kolom "nama"
# # # df.loc[1, 'Nama'] = 'Maria'

# # # # Tampilkan data setelah diubah
# # # print("\nData Setelah di Update")
# # # print(df.head())

# # # carIndex = df[df['Nama'] == "Citra Lestari"].index
# # # df.loc[carIndex, 'Angkatan']  = 2019
# # # print(df)


# # # dataDF = pd.read_csv('mahasiswa.csv')

# # # nim = int(input('NIM yang ingin di input'))
# # # nama = input('Nama yang ingin di input')
# # # angkatan = int(input('Angkatan yang ingin di input'))

# # # dataBaru = pd.DataFrame({'NIM': [nim], 'Nama': [nama], 'Angkatan': [angkatan]})
# # # dataDF = pd.concat([dataDF, dataBaru], ignore_index=True)
# # # print(dataDF)
# # # dataDF.to_csv('mahasiswa.csv', index=False)


# # dataBaru = {
# # 'NIM': [23005],
# # 'Nama': ['budi Putra'],
# # 'Angkatan': [2023]
# # }

# # # ubah dictionary ke dataframe
# # df_baru = pd.DataFrame(dataBaru)

# # # 3.gabung dataframe lama dengan dataframe baru
# # df = pd.concat([df, df_baru], ignore_index=True)

# # print("\nData setelah ditambah Eka Putra:")
# # print(df)
# # df.to_csv('mahasiswa.csv', index=False)

# # df['Asal'] = 'Samarinda'

# # print("Data setelah ditambah kolom 'Asal':")
# # print(df)

# # # Menghapus baris berdasarkan index-nya
# # # inplace=True berarti kita memodifikasi df secara langsung
# # print(df)
# # df.drop(index=1, inplace=True) #cara 1
# # df = df.drop(index=1) #cara 2

# # print("\nData setelah menghapus Citra (index 2):")
# # print(df)

# # # Menghapus kolom 'Asal'
# # # axis=1 memberitahu pandas bahwa kita mau menghapus KOLOM
# # print(df)
# # df.drop('Asal', axis=1, inplace=True)

# # print("\nData setelah menghapus kolom 'Asal':")
# # print(df)

# # kondisi = df['Nama'] != 'Ekas Putra'
# # dfBaru = df[kondisi]
# # print(dfBaru)


# # data = {'NIM': [19001, 23001], 'Nama': ['Citra', 'Budi'], 'Angkatan': [2019, 2023]}
# # df_benar = pd.DataFrame(data)
# # print("--- Data Awal ---")
# # print(df_benar)

# # for index, row in df_benar.iterrows():
# #     if row['Angkatan'] < 2020:
# #         # Gunakan .loc[index, 'NamaKolomBaru'] untuk mengubah DataFrame ASLI
# #         df_benar.loc[index, 'Status'] = 'Alumni'
# #     else:
# #         df_benar.loc[index, 'Status'] = 'Mahasiswa Aktif'

# # print("\n--- Hasil yang Benar (Data Berubah) ---")
# # print(df_benar)


# url = 'https://raw.githubusercontent.com/orkvacy/dummy-data/refs/heads/main/dummyData.csv'
# df = pd.read_csv(url)

# print(df.head(5))

# # df.isna().sum()

# # df['tingkat_pendidikan'].value_counts()

# # df['tingkat_pendidikan'] = df['tingkat_pendidikan'].fillna("Tidak Diketahui")

# # df = df.dropna()

# # df.isna().sum()

# # df[df.duplicated()]