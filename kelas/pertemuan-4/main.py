# ulangi = 10
# for i in range (ulangi):
#     print(f'Perulangan ke {i}')


# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(1, 4):
#     for j in range(1, 5):
#         print(f'{i} x {j} = {i * j}')
#         print('') 


# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
# print(f"Total perulangan: {hitung}")


# angka = [2, 5, 8, 12, 15, 7, 20]
# print("Mencari angka pertama yang lebih besar dari 10...")
# for n in angka:
#     print(f"Sekarang memeriksa angka: {n}")
#     if n > 10:
#         print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")


# for i in range(1,10):
#     print('#'* i)
# for i in range(10, 0, -1):
#     print('#' * i)

# for i in range(1, 11):
#     if i % 2 != 0: #if i % 2 == 0:
#         continue
#     print(f"Angka genap ditemukan: {i}")
# print("\nProgram selesai.")

h = 10

for i in range(1, 10):
    kiri = '#' * i
    tengaah = ' '*((h-i)*2)
    kanan = '#' * i
    print(kiri+tengaah+kanan)
