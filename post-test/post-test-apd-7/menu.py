from colorama import Fore, Style
from menu_display import admin_display, user_display
from tools import get_input, get_number, clear
from crud import get_data_for_read, get_data_for_create, get_data_for_update, get_id_for_delete
from data import matches

# prosedur
def menu_admin(nama):
    while True:
        clear()
        print(f'Selamat Datang, {nama}'.center(50))
        print(f'MENU ADMIN'.center(50))
        print(Fore.YELLOW + str(admin_display))
        
        pilih = get_number('Pilih menu: ')

        if pilih == 1:
            tabel_data = get_data_for_read()
            if tabel_data:
                print(tabel_data)
                input(Fore.CYAN + '\nTekan Enter untuk kembali...' + Style.RESET_ALL)
            else:
                print(Fore.RED + '\nBelum ada data pertandingan.')

        elif pilih == 2:
            id_baru, data_baru = get_data_for_create()
            if id_baru is not None:
                matches[id_baru] = data_baru
                print(Fore.GREEN + '\nData berhasil ditambahkan!')
                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
        
        elif pilih == 3:
            id_update, data_update = get_data_for_update()
            if id_update is not None:
                matches[id_update] = data_update
                print(Fore.GREEN + '\nData berhasil diubah!')
                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
        
        elif pilih == 4:
            id_hapus = get_id_for_delete()
            if id_hapus is not None:
                del matches[id_hapus]
                print(Fore.GREEN + f'\nData ID {id_hapus} berhasil dihapus!')
                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
        
        elif pilih == 0:
            print(Fore.YELLOW + 'Anda telah keluar.')
            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + 'Pilihan tidak valid.')
            input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)

# prosedur
def menu_user(nama):
    while True:
        clear()
        print(f'Selamat Datang, {nama}'.center(50))
        print(f'MENU PENGGUNA'.center(50))
        print(Fore.YELLOW + str(user_display))

        pilih = get_number('Pilih menu: ')

        if pilih == 1:
            clear()
            tabel_data = get_data_for_read()
            if tabel_data:
                print(tabel_data)
                input(Fore.CYAN + '\nTekan Enter untuk kembali...' + Style.RESET_ALL)
            else:
                print(Fore.RED + '\nBelum ada data pertandingan.')
                
        elif pilih == 0:
            print(Fore.YELLOW + 'Anda telah keluar.')
            input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL) 
            break
        else:
            print(Fore.RED + 'Pilihan tidak valid.')
            input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)