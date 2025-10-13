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
        print(Fore.YELLOW + (f'\n{'='*18}{'HALAMAN LOGIN'}{'='*18}'))
        input_username = input('Masukkan Username: ')
        input_password = input('Masukkan Password: ')
        for user in data_user:
            if user[0] == input_username and user[1] == input_password:
                peran_user = user[2]
                login_berhasil = True
                break

        if login_berhasil:
            print(Fore.GREEN + (f'\n{'-'*17}{'Login berhasil'}{'-'*18}'))
            input(Fore.CYAN + 'Tekan Enter untuk melanjutkan...' + Style.RESET_ALL)
            
            while True:
                os.system('cls || clear')
                
                if peran_user == 'admin':
                    print(f'Selamat Datang, {input_username}'.center(50))
                    print(f'MENU ADMIN'.center(50))
                    print(Fore.YELLOW + str(menu_admin))
                    pilihan_menu = input('Pilih menu: ')
                    
                    if pilihan_menu == '1':
                        os.system('cls || clear')
                        print(Fore.YELLOW + 'DATA HASIL PERTANDINGAN'.center(77))
                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Pemenang']
                        if data_pertandingan:
                            for pertandingan in data_pertandingan:
                                tabel.add_row(pertandingan)
                            print(tabel)
                        else:
                            print(Fore.RED + '\nBelum ada data pertandingan.')
                        input(Fore.CYAN + '\nTekan Enter untuk kembali...' + Style.RESET_ALL)
                    
                    elif pilihan_menu == '2':
                        while True:
                            os.system('cls || clear')
                            print(Fore.YELLOW + (f'\n{'='*10}{'TAMBAH DATA PERTANDINGAN'}{'='*10}'))
                            input_id_str = input('Masukkan ID Pertandingan (atau ketik "X" untuk kembali): ')
                            if input_id_str == 'x':
                                break
                            elif not input_id_str.isdigit():
                                print(Fore.RED + '\nID harus berupa angka!')
                                input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)
                                continue
                            
                            input_id = int(input_id_str)
                            id_sudah_ada = False
                            for i in data_pertandingan:
                                if i[0] == input_id:
                                    id_sudah_ada = True
                                    break
                            
                            if id_sudah_ada == True:
                                print(Fore.RED + '\nID sudah digunakan!')
                                input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)
                            else:
                                nama_putih = input('Nama Pemain Putih: ')
                                nama_hitam = input('Nama Pemain Hitam: ')
                                while True:
                                    jumlah_langkah_str = input('Jumlah Langkah Total: ')
                                    if jumlah_langkah_str.isdigit():
                                        jumlah_langkah = int(jumlah_langkah_str)
                                        break
                                    else:
                                        print(Fore.RED + 'Jumlah langkah harus berupa angka!')
                                while True:
                                    print('\nPilihan Hasil: 1. Putih Menang, 2. Hitam Menang, 3. Seri')
                                    pilihan_hasil = input('Pilihan (1/2/3): ')
                                    if pilihan_hasil in ['1', '2', '3']:
                                        if pilihan_hasil == '1': hasil = 'Putih Menang'
                                        elif pilihan_hasil == '2': hasil = 'Hitam Menang'
                                        else: hasil = 'Seri'
                                        break
                                    else:
                                        print(Fore.RED + 'Pilihan tidak valid.')
                                
                                data_pertandingan.append([input_id, nama_putih, nama_hitam, jumlah_langkah, hasil])
                                print(Fore.GREEN + '\nData berhasil ditambahkan!')
                                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                                break

                    elif pilihan_menu == '3':
                        os.system('cls || clear')
                        print(Fore.YELLOW + 'UBAH DATA PERTANDINGAN'.center(77))
                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Hasil']
                        if not data_pertandingan:
                            print(Fore.RED + '\nBelum ada data pertandingan untuk diubah.')
                            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                            continue
                        for pertandingan in data_pertandingan:
                            tabel.add_row(pertandingan)
                        print(tabel)

                        while True:
                            input_id_str = input('\nMasukkan ID yang ingin diubah (atau ketik "x" untuk kembali): ')
                            if input_id_str == 'x':
                                break
                            elif not input_id_str.isdigit():
                                print(Fore.RED + 'Input tidak valid. ID harus berupa angka.')
                                continue

                            input_id = int(input_id_str)
                            data_ditemukan = False
                            indeks_data = -1

                            for i in range(len(data_pertandingan)):
                                if data_pertandingan[i][0] == input_id:
                                    data_ditemukan = True
                                    indeks_data = i
                                    break
                            
                            if data_ditemukan:
                                print(Fore.CYAN + f'\nMengubah data untuk ID {input_id}: {data_pertandingan[indeks_data]}')
                                nama_putih_baru = input('Nama Pemain Putih Baru: ')
                                nama_hitam_baru = input('Nama Pemain Hitam Baru: ')
                                
                                while True:
                                    jumlah_langkah_baru_str = input('Jumlah Langkah Baru: ')
                                    if jumlah_langkah_baru_str.isdigit():
                                        jumlah_langkah_baru = int(jumlah_langkah_baru_str)
                                        break
                                    else:
                                        print(Fore.RED + 'Input tidak valid, jumlah langkah harus angka!')
                                
                                while True:
                                    print('\nPilihan Hasil Baru: 1. Putih Menang, 2. Hitam Menang, 3. Seri')
                                    pilihan_hasil_baru = input('Pilihan (1/2/3): ')
                                    if pilihan_hasil_baru in ['1', '2', '3']:
                                        if pilihan_hasil_baru == '1': hasil_baru = 'Putih Menang'
                                        elif pilihan_hasil_baru == '2': hasil_baru = 'Hitam Menang'
                                        else: hasil_baru = 'Seri'
                                        break
                                    else:
                                        print(Fore.RED + 'Pilihan tidak valid.')
                                
                                data_pertandingan[indeks_data] = [input_id, nama_putih_baru, nama_hitam_baru, jumlah_langkah_baru, hasil_baru]
                                print(Fore.GREEN + '\nData berhasil diubah!')
                                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                                break
                            else:
                                print(Fore.RED + f'ID {input_id} tidak ditemukan. Silakan coba lagi.')

                    elif pilihan_menu == '4':
                        os.system('cls || clear')
                        print(Fore.YELLOW + '--- HAPUS DATA PERTANDINGAN ---')
                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Hasil']
                        if not data_pertandingan:
                            print(Fore.RED + '\nBelum ada data pertandingan untuk diubah.')
                            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                            continue
                        for pertandingan in data_pertandingan:
                            tabel.add_row(pertandingan)
                        print(tabel)
                        
                        while True:
                            input_id_str = input('Masukkan ID yang mau di hapus (atau ketik "X" untuk kembali): ')
                            if input_id_str == 'x':
                                break
                            elif not input_id_str.isdigit():
                                print(Fore.RED + '\nID harus berupa angka!')
                                input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)
                                continue
                            else:
                                input_id = int(input_id_str)
                                data_ditemukan = False
                                indeks_data = -1
                                for i in range(len(data_pertandingan)):
                                    if data_pertandingan[i][0] == input_id:
                                        data_ditemukan = True
                                        indeks_data = i
                                        break
                                if data_ditemukan:
                                    data_pertandingan.pop(indeks_data)
                                    print(Fore.GREEN + f'\nData ID {input_id} berhasil dihapus!')
                                else:
                                    print(Fore.RED + '\nID tidak ditemukan.')
                            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                            break
                        
                    elif pilihan_menu == '0':
                        print(Fore.YELLOW + 'Anda telah logout.')
                        input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + 'Pilihan tidak valid.')
                        input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)

                elif peran_user == 'user':
                    print(f'Selamat Datang, {input_username}'.center(50))
                    print(f'MENU USER'.center(50))
                    print(Fore.YELLOW + str(menu_user))
                    pilihan_menu = input('Pilih menu: ')
                    
                    if pilihan_menu == '1':
                        os.system('cls || clear')
                        print(Fore.YELLOW + 'DATA HASIL PERTANDINGAN'.center(77))
                        tabel = PrettyTable()
                        tabel.field_names = ['ID', 'Pemain Putih', 'Pemain Hitam', 'Jumlah Langkah', 'Pemenang']
                        if not data_pertandingan:
                            print(Fore.RED + '\nBelum ada data pertandingan.')
                        else:
                            for pertandingan in data_pertandingan:
                                tabel.add_row(pertandingan)
                            print(tabel)
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
        os.system('cls || clear')
        print(Fore.YELLOW + '=== HALAMAN REGISTER ===')
        username_baru = input('Masukkan Username Baru: ')
        username_sudah_ada = False
        for user in data_user:
            if user[0] == username_baru:
                username_sudah_ada = True
                break
        if username_sudah_ada:
            print(Fore.RED + '\nUsername sudah digunakan.')
        else:
            password_baru = input('Masukkan Password Baru: ')
            data_user.append([username_baru, password_baru, 'user'])
            print(Fore.GREEN + '\nRegistrasi berhasil! Silakan login.')
        input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
    
    elif pilihan_awal == '0':
        print(Fore.GREEN + '\nTerima kasih telah menggunakan program kami!')
        break
        

    else:
        print(Fore.RED + 'Pilihan tidak valid, silakan pilih 1, 2, atau 0.')
        input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)