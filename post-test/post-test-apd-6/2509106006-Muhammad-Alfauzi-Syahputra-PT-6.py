import os
from prettytable import PrettyTable
from colorama import Fore, Style, init
from data import data_pertandingan, data_user
from menu import menu_utama, menu_admin, menu_user
init(autoreset=True)

while True:
    os.system('cls || clear')
    print(f'PENCATATAN HASIL PERTANDINGAN CATUR'.center(50))
    print(Fore.YELLOW + str(menu_utama))
    pilihan_awal = input('Masukkan pilihan Anda: ')
    login_berhasil = False

    if pilihan_awal == '1':
        os.system('cls || clear')
        print(Fore.YELLOW + (f'{'='*18}{'HALAMAN LOGIN'}{'='*18}'))

        input_username = ""
        while not input_username.strip():
            input_username = input('Masukkan Username: ')
            if not input_username.strip():
                print(Fore.RED + "Username tidak boleh kosong.")

        input_password = ''
        while not input_password.strip():
            input_password = input('Masukkan Password: ')
            if not input_password.strip():
                print(Fore.RED + "Password tidak boleh kosong.")

        if input_username in data_user and data_user[input_username]['password'] == input_password:
            peran_user = data_user[input_username]['role']
            login_berhasil = True

        if login_berhasil == True:
            print(Fore.GREEN + (f'\n{'-'*17}{'Login berhasil'}{'-'*18}'))
            input(Fore.CYAN + 'Tekan Enter untuk melanjutkan...' + Style.RESET_ALL)
            
            while True:
                os.system('cls || clear')
                
                if peran_user == 'admin':
                    print(f'Selamat Datang, {input_username}'.center(50))
                    print(f'MENU ADMIN'.center(50))
                    print(Fore.YELLOW + str(menu_admin))

                    pilihan_menu = ''
                    while not pilihan_menu.strip():
                        pilihan_menu = input('Pilih menu: ')
                        if not pilihan_menu.strip():
                            print(Fore.RED + "Pilihan tidak boleh kosong. Silakan coba lagi.")
                    
                    if pilihan_menu == '1':
                        os.system('cls || clear')
                        print(Fore.YELLOW + 'DATA HASIL PERTANDINGAN'.center(77))

                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Pemenang']
                        if data_pertandingan:
                            for id_match, details in data_pertandingan.items():
                                tabel.add_row([
                                    id_match,
                                    details['pemain_putih'],
                                    details['pemain_hitam'],
                                    details['jumlah_langkah'],
                                    details['pemenang']
                                ])
                            print(tabel)
                        else:
                            print(Fore.RED + '\nBelum ada data pertandingan.')
                        input(Fore.CYAN + '\nTekan Enter untuk kembali...' + Style.RESET_ALL)
                    
                    elif pilihan_menu == '2':
                        while True:
                            os.system('cls || clear')
                            print(Fore.YELLOW + (f'\n{'='*10}{'TAMBAH DATA PERTANDINGAN'}{'='*10}'))

                            input_id_str = ''
                            while not input_id_str.strip():
                                input_id_str = input('Masukkan ID Pertandingan (atau ketik "X" untuk kembali): ')
                                if not input_id_str.strip():
                                    print(Fore.RED + "ID tidak boleh kosong. Silakan coba lagi.")
                            if input_id_str == 'x':
                                break
                            elif not input_id_str.isdigit():
                                print(Fore.RED + '\nID harus berupa angka!')
                                input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)
                                continue
                            
                            input_id = int(input_id_str)

                            if input_id not in data_pertandingan:
                                nama_putih = ""
                                while not nama_putih.strip():
                                    nama_putih = input('Nama Pemain Putih: ')
                                    if not nama_putih.strip(): 
                                        print(Fore.RED + "Nama tidak boleh kosong.")
                                        
                                nama_hitam = ''
                                while not nama_hitam.strip():
                                    nama_hitam = input('Nama Pemain Hitam: ')
                                    if not nama_hitam.strip():
                                        print(Fore.RED + "Nama tidak boleh kosong.")

                                while True:
                                    jumlah_langkah_str = input('Jumlah Langkah Total: ')
                                    if not jumlah_langkah_str.strip():
                                        print(Fore.RED + "Jumlah langkah tidak boleh kosong.")
                                    elif not jumlah_langkah_str.isdigit():
                                        print(Fore.RED + 'Jumlah langkah harus berupa angka!')
                                    else:
                                        jumlah_langkah = int(jumlah_langkah_str)
                                        break
                                while True:
                                    print('\nPilihan Hasil: 1. Putih Menang, 2. Hitam Menang, 3. Seri')
                                    pilihan_hasil = ''
                                    while not pilihan_hasil.strip():
                                        pilihan_hasil = input('Pilihan (1/2/3): ')
                                        if not pilihan_hasil.strip():
                                            print(Fore.RED + "Pilihan hasil tidak boleh kosong.")
                                    if pilihan_hasil in ['1', '2', '3']:
                                        hasil = 'Putih Menang' if pilihan_hasil == '1' else 'Hitam Menang' if pilihan_hasil == '2' else 'Seri'
                                        break
                                    else:
                                        print(Fore.RED + 'Pilihan tidak valid.')

                                data_pertandingan[input_id] = {
                                    'pemain_putih': nama_putih,
                                    'pemain_hitam': nama_hitam,
                                    'jumlah_langkah': jumlah_langkah,
                                    'pemenang': hasil
                                }

                                print(Fore.GREEN + '\nData berhasil ditambahkan!')
                                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                                break
                            else:
                                print(Fore.RED + f'\nID {input_id} sudah digunakan.')
                                input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)

                    elif pilihan_menu == '3':
                        os.system('cls || clear')
                        print(Fore.YELLOW + 'UBAH DATA PERTANDINGAN'.center(77))
                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Hasil']
                        if not data_pertandingan:
                            print(Fore.RED + '\nBelum ada data pertandingan untuk diubah.')
                            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                            continue
                        if data_pertandingan:
                            for id_match, details in data_pertandingan.items():
                                tabel.add_row([
                                    id_match,
                                    details['pemain_putih'],
                                    details['pemain_hitam'],
                                    details['jumlah_langkah'],
                                    details['pemenang']
                                ])
                            print(tabel)

                        while True:
                            input_id_str = ''
                            while not input_id_str.strip():
                                input_id_str = input('\nMasukkan ID yang ingin diubah (atau ketik "x" untuk kembali): ')
                                if not input_id_str.strip():
                                    print(Fore.RED + 'ID tidak boleh kosong. Silakan coba lagi.')
                            if input_id_str == 'x':
                                break
                            elif not input_id_str.isdigit():
                                print(Fore.RED + 'Input tidak valid. ID harus berupa angka.')
                                continue

                            input_id = int(input_id_str)
                            
                            if input_id in data_pertandingan:
                                print(Fore.CYAN + f'\nMengubah data untuk ID {input_id}')
                                nama_putih_baru = ''
                                while not nama_putih_baru.strip():
                                    nama_putih_baru = input('Nama Pemain Putih Baru: ')
                                    if not nama_putih_baru.strip():
                                        print(Fore.RED + "Nama Pemain Putih tidak boleh kosong.")
                                        
                                nama_hitam_baru = ''
                                while not nama_hitam_baru.strip():
                                    nama_hitam_baru = input('Nama Pemain Hitam Baru: ')
                                    if not nama_hitam_baru.strip():
                                        print(Fore.RED + "Nama Pemain Hitam tidak boleh kosong.")
                                
                                while True:
                                    jumlah_langkah_baru_str = ''
                                    while not jumlah_langkah_baru_str.strip():
                                        jumlah_langkah_baru_str = input('Jumlah Langkah Baru: ')
                                        if not jumlah_langkah_baru_str.strip():
                                            print(Fore.RED + "Jumlah Langkah tidak boleh kosong.")
                                    if jumlah_langkah_baru_str.isdigit():
                                        jumlah_langkah_baru = int(jumlah_langkah_baru_str)
                                        break
                                    else:
                                        print(Fore.RED + 'Input tidak valid, jumlah langkah harus angka!')
                                
                                while True:
                                    print('\nPilihan Hasil Baru: 1. Putih Menang, 2. Hitam Menang, 3. Seri')
                                    pilihan_hasil_baru = ''
                                    while not pilihan_hasil_baru.strip():
                                        pilihan_hasil_baru = input('Pilihan (1/2/3): ')
                                        if not pilihan_hasil_baru.strip():
                                            print(Fore.RED + "Pilihan hasil tidak boleh kosong.")
                                    if pilihan_hasil_baru in ['1', '2', '3']:
                                        if pilihan_hasil_baru == '1': hasil_baru = 'Putih Menang'
                                        elif pilihan_hasil_baru == '2': hasil_baru = 'Hitam Menang'
                                        else: hasil_baru = 'Seri'
                                        break
                                    else:
                                        print(Fore.RED + 'Pilihan tidak valid.')
                            
                                data_pertandingan[input_id] = {
                                    'pemain_putih': nama_putih_baru,
                                    'pemain_hitam': nama_hitam_baru,
                                    'jumlah_langkah': jumlah_langkah_baru,
                                    'pemenang': hasil_baru
                                }

                                print(Fore.GREEN + '\nData berhasil diubah!')
                                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                                break
                            else:
                                print(Fore.RED + f'ID {input_id} tidak ditemukan. Silakan coba lagi.')

                    elif pilihan_menu == '4':
                        os.system('cls || clear')
                        print(Fore.YELLOW + 'HAPUS DATA PERTANDINGAN'.center(77))
                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Hasil']
                        if not data_pertandingan:
                            print(Fore.RED + '\nBelum ada data pertandingan untuk diubah.')
                            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                            continue
                        if data_pertandingan:
                            for id_match, details in data_pertandingan.items():
                                tabel.add_row([
                                    id_match,
                                    details['pemain_putih'],
                                    details['pemain_hitam'],
                                    details['jumlah_langkah'],
                                    details['pemenang']
                                ])
                            print(tabel)
                        
                        while True:
                            input_id_str = ''
                            while not input_id_str.strip():
                                input_id_str = input('\nMasukkan ID yang mau dihapus (atau ketik "X" untuk kembali): ')
                                if not input_id_str.strip():
                                    print(Fore.RED + "ID tidak boleh kosong. Silakan coba lagi.")
                            if input_id_str == 'x':
                                break
                            elif not input_id_str.isdigit():
                                print(Fore.RED + '\nID harus berupa angka!')
                                continue
                            
                            input_id = int(input_id_str)

                            if input_id in data_pertandingan:
                                del data_pertandingan[input_id]
                                print(Fore.GREEN + f'\nData ID {input_id} berhasil dihapus!')
                                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                                break
                            else:
                                print(Fore.RED + '\nID tidak ditemukan.')
                        
                    elif pilihan_menu == '0':
                        print(Fore.YELLOW + 'Anda telah logout.')
                        input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                        break
                    
                    else:
                        print(Fore.RED + 'Pilihan tidak valid.')
                        input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)

                else:
                    print(f'Selamat Datang, {input_username}'.center(50))
                    print(f'MENU USER'.center(50))
                    print(Fore.YELLOW + str(menu_user))
                    pilihan_menu = ''
                    while not pilihan_menu.strip():
                        pilihan_menu = input('Pilih menu: ')
                        if not pilihan_menu.strip():
                            print(Fore.RED + "Pilihan tidak boleh kosong. Silakan coba lagi.")
                    
                    if pilihan_menu == '1':
                        os.system('cls || clear')
                        print(Fore.YELLOW + 'DATA HASIL PERTANDINGAN'.center(77))
                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Pemenang']
                        if data_pertandingan:
                            for id_match, details in data_pertandingan.items():
                                tabel.add_row([
                                    id_match,
                                    details['pemain_putih'],
                                    details['pemain_hitam'],
                                    details['jumlah_langkah'],
                                    details['pemenang']
                                ])
                            print(tabel)
                        else:
                            print(Fore.RED + '\nBelum ada data pertandingan.')
                        input(Fore.CYAN + '\nTekan Enter untuk kembali...' + Style.RESET_ALL)

                    elif pilihan_menu == '0':
                        print(Fore.YELLOW + 'Anda telah logout.')
                        input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL) 
                        break
                    else:
                        print(Fore.RED + 'Pilihan tidak valid.')
                        input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)
        else:
            print(Fore.RED + (f'\n{'-'*19}{'Login gagal'}{'-'*19}'))
            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)

    elif pilihan_awal == '2':
        while True:
            os.system('cls || clear')
            print(Fore.YELLOW + f'\n{'='*18}{'MENU REGISTER'}{'='*18}')
            username_baru = ''
            while not username_baru.strip():
                username_baru = input('Masukkan Username Baru (atau ketik "X" untuk kembali): ')
                if not username_baru.strip():
                    print(Fore.RED + 'Username tidak boleh kosong.')

            if username_baru == 'x':
                break

            if username_baru in data_user:
                print(Fore.RED + '\nUsername sudah digunakan.')
                input(Fore.CYAN + 'Tekan Enter untuk cobal lagi...' + Style.RESET_ALL)
            else:
                password_baru = ''
                while not password_baru.strip():
                    password_baru = input('Masukkan Password Baru: ')
                    if not password_baru.strip():
                        print(Fore.RED + 'Password tidak boleh kosong.')
                data_user[username_baru] = {'password': password_baru, 'role': 'user'}
                print(Fore.GREEN + '\nRegistrasi berhasil! Silakan login.')
                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                break
    
    elif pilihan_awal == '0':
        print(Fore.GREEN + '\nTerima kasih telah menggunakan program kami!')
        break
        
    else:
        print(Fore.RED + 'Pilihan tidak valid, silakan pilih 1, 2, atau 0.')
        input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)