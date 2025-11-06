import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# plt.figure(figsize=(12, 6))
# plt.xlabel('kasih nama Sumbu X')
# plt.ylabel('kasih nama Sumbu Y')
# plt.title("Ini judul loh")

# x = [1, 2, 3, 4, 5]
# y = [10, 35, 20, 70, 60]

# plt.figure(figsize=(8, 4))
# # plt.plot()
# plt.plot(x, y)
# # Detail element
# plt.title("Contoh Grafik")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(12, 6))
# plt.xlabel('kasih nama Sumbu X')
# plt.ylabel('kasih nama Sumbu Y')
# plt.title("Ini judul loh")

# x = [1, 2, 3, 4, 5]
# y = [10, 35, 20, 70, 60]

# plt.figure(figsize=(8, 4))
# # plt.plot()
# plt.plot(x, y)
# # Detail element
# plt.title("Contoh Grafik")
# plt.xlabel("Sumbu X")
# plt.ylabel("Sumbu Y")
# plt.grid(True)
# plt.show()

x = [1, 2, 3, 4, 5]
y = [10, 35, 20, 70, 60]
y2 = [12, 43, 56, 23, 67]
plt.figure(figsize=(8, 4))
# plt.plot() untuk masing-masing garis
plt.plot(x, y, marker="o", color="blue", label="Matematika")
plt.plot(x, y2, color="red", marker="h", linestyle="--", label="Fisika")
# Detail elemen untuk memambahkan teks
plt.title("Contoh Grafik")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.grid(True)
# Nambahin keterangan, tapi jangan lupa tambahkan label
plt.legend()
plt.show()
plt.savefig("Real Penggunaan") #Menyimpan Gambar

# kategori = ['Python', 'Assembly', 'Java', 'C++']
# jumlah_pengguna = [100, 10, 50, 70]
# plt.figure(figsize=(8, 5))
# # plt.bar() untuk menampilkan bar ke atas
# plt.bar(kategori, jumlah_pengguna)
# plt.xlabel("Nama Bahasa Pemrograman")
# plt.ylabel("Banyak Pengguna")
# plt.title("Perbandingan popularitas Bahasa Pemrograman")
# # axis = y --- untuk mengubur garis vertikal;
# # alpha --- untuk mengatur opacity garis
# plt.grid(axis="y", alpha=0.5, linestyle="--")

# plt.show()

# # Data dua kelompok
# fisika_kelompok1 = [85, 88, 90, 92, 87]
# matematika_kelompok1 = [60, 58, 55, 62, 59]
# fisika_kelompok2 = [65, 68, 70, 72, 69]
# matematika_kelompok2 = [80, 85, 82, 88, 84]
# plt.figure(figsize=(8, 5))
# plt.scatter(fisika_kelompok1, matematika_kelompok1, marker="o", label="Kelompok1")
# plt.scatter(fisika_kelompok2, matematika_kelompok2, marker="*", label="Kelompok2")
# plt.title("Perbandingan Nilai Fisika dan Matematika")
# plt.xlabel("Nilai Fisika")
# plt.ylabel("Nilai Matematika")
# plt.legend(loc="lower left")
# plt.grid(True, alpha=0.5)
# plt.show()

# views = [320, 450, 400, 390, 410, 470, 500, 490, 480, 510,
# 530, 600, 620, 590, 550, 570, 610, 640, 700, 5000, 1000, 2000, 800,
# 700, 750]

# plt.figure(figsize=(7, 4))
# plt.boxplot(views, vert=False)
# plt.xlabel('Number of Views')
# plt.ylabel('Instagram')
# plt.ylabel('Number of Costumers')
# plt.grid(axis='y', alpha=0.5)
# plt.show()

# # Data
# views = [320, 450, 400, 390, 410, 470, 500, 490, 480, 510,
#         530, 600, 620, 590, 550, 570, 610, 640, 700, 5000,
#         1000, 2000, 800, 700, 750]

# # Convert to Series and clean outliers
# views_series = pd.Series(views)
# views_clean = views_series[views_series < 1000]  # remove outliers

# # Plot
# plt.figure(figsize=(7, 4))
# plt.boxplot(views_clean, vert=False)
# plt.ylabel('Number of Costumers')
# plt.grid(axis='y', alpha=0.5)
# plt.show()


    # # Mengambil dataset iris dari seaborn
    # iris = sns.load_dataset("iris")

    # plt.figure(figsize=(8, 5))
    # # Membuat histogram untuk kolom sepal_length
    # plt.hist(iris["sepal_length"], bins=15, color="skyblue", edgecolor="black",
    # alpha=0.7)
    # plt.title("Distribusi Panjang Sepal (sepal_length)")
    # plt.xlabel("Sepal Length")
    # plt.ylabel("Frekuensi")
    # plt.grid(axis='y', alpha=0.5)
    # plt.show()