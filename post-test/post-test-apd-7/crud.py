from prettytable import PrettyTable
from colorama import Fore, Style
from data import matches
from tools import get_input, get_number, clear

# READ
# fungsi tanpa parameter
def get_data_for_read():
    clear()
    print(Fore.YELLOW + 'DATA HASIL PERTANDINGAN'.center(70))
    if not matches:
        return None
    tabel = PrettyTable(['ID', 'Pemain Putih', 'Pemain Hitam', 'Langkah', 'Pemenang'])
    for id, detail in matches.items():
        tabel.add_row([id, detail['putih'], detail['hitam'], detail['langkah'], detail['pemenang']])
    return tabel

# CREATE
# fungsi tanpa parameter
def get_data_for_create():
    while True:
        try:
            clear()
            print(Fore.YELLOW + (f'\n{'='*10}{'TAMBAH DATA PERTANDINGAN'}{'='*10}'))
            id_str = get_input('ID pertandingan (ketik "x" untuk kembali): ')
            if id_str.lower() == 'x': return None, None

            id = int(id_str)
            if id in matches:
                print(Fore.RED + f'\nID {id} sudah digunakan.')
                input(Fore.CYAN + 'Tekan Enter...')
            else:
                putih = get_input('Nama Pemain Putih: ')
                hitam = get_input('Nama Pemain Hitam: ')
                langkah = get_number('Jumlah Langkah: ')
                while True:
                    print('\nPilihan Hasil: 1. Putih Menang, 2. Hitam Menang, 3. Seri')
                    pilih_hasil = get_number('Pilihan (1/2/3): ')
                    if pilih_hasil in [1, 2, 3]:
                        hasil = 'Putih Menang' if pilih_hasil == 1 else 'Hitam Menang' if pilih_hasil == 2 else 'Seri'
                        break
                    else: print(Fore.RED + 'Pilihan tidak valid.')
                
                data_baru = {'putih': putih, 'hitam': hitam, 'langkah': langkah, 'pemenang': hasil}
                return id, data_baru
        except ValueError:
            print(Fore.RED + '\nID harus berupa angka!')
            input(Fore.CYAN + 'Tekan Enter...')

# UPDATE
# fungsi tanpa parameter
def get_data_for_update():
    read_table = get_data_for_read()
    if read_table:
        clear()
        print(Fore.YELLOW + 'UBAH DATA PERTANDINGAN'.center(70))
        print(read_table)
    else:
        print(Fore.RED + '\nBelum ada data pertandingan.')
        return None, None
    
    while True:
        try:
            id_str = get_input('\nID pertandingan yang akan diubah (ketik "x" untuk kembali): ')
            if id_str.lower() == 'x': return None, None

            id_laga = int(id_str)
            if id_laga in matches:
                print(Fore.CYAN + f'\nMengubah data ID {id_laga}')
                putih = get_input('Nama Pemain Putih Baru: ')
                hitam = get_input('Nama Pemain Hitam Baru: ')
                langkah = get_number('Jumlah Langkah Baru: ')
                while True:
                    print('\nPilihan Hasil Baru: 1. Putih Menang, 2. Hitam Menang, 3. Seri')
                    pilih_hasil = get_number('Pilihan (1/2/3): ')
                    if pilih_hasil in [1, 2, 3]:
                        hasil = 'Putih Menang' if pilih_hasil == '1' else 'Hitam Menang' if pilih_hasil == '2' else 'Seri'
                        break
                    else: print(Fore.RED + 'Pilihan tidak valid.')

                data_update = {'putih': putih, 'hitam': hitam, 'langkah': langkah, 'pemenang': hasil}
                return id_laga, data_update
            else:
                print(Fore.RED + f'\nID {id_laga} tidak ditemukan.')
        except ValueError:
            print(Fore.RED + 'ID harus berupa angka!')

# DELETE
# fungsi tanpa parameter
def get_id_for_delete():
    read_table = get_data_for_read()
    if read_table:
        clear()
        print(Fore.YELLOW + 'HAPUS DATA PERTANDINGAN'.center(70))
        print(read_table)
    else:
        print(Fore.RED + '\nBelum ada data pertandingan.')
        input(Fore.CYAN + '\nTekan Enter untuk kembali...' + Style.RESET_ALL)
        return None
    
    while True:
        try:
            id_str = get_input('\nID pertandingan yang akan dihapus (ketik "x" untuk kembali): ')
            if id_str.lower() == 'x': return None

            id = int(id_str)
            if id in matches:
                return id
            else:
                print(Fore.RED + 'ID tidak ditemukan.')
        except ValueError:
            print(Fore.RED + 'ID harus berupa angka!')