import inquirer

# Buat pertanyaan dengan pilihan yang bisa dipilih pakai panah
pertanyaan = [
    inquirer.List(
        'bahasa',
        message="Pilih bahasa pemrograman favoritmu:",
        choices=['Python', 'JavaScript', 'Java', 'C++', 'Go']
    )
]

# Jalankan pertanyaan
jawaban = inquirer.prompt(pertanyaan)

# Tampilkan hasil
print(f"\nKamu memilih: {jawaban['bahasa']} ✨")
