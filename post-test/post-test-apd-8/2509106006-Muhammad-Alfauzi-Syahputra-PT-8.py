from colorama import Fore, Style, init
from menu_display import main_display
from tools import clear
from auth import login, register
from menu import menu_admin, menu_user
from tools import get_number
from data import users

init(autoreset=True)

# prosedur
def main():
    while True:
        clear()
        print('PENCATATAN HASIL PERTANDINGAN CATUR'.center(50))
        print(Fore.YELLOW + str(main_display))
        pilihan = get_number('Masukkan pilihan Anda: ')

        if pilihan == 1:
            sukses, username, peran = login()
            if sukses:
                if peran == 'admin':
                    menu_admin(username)
                else:
                    menu_user(username)
        elif pilihan == 2:
            nama_baru, data_baru = register()
            if nama_baru is not None:
                users[nama_baru] = data_baru
                print(Fore.GREEN + '\nBerhasil register! Silakan login.')
                input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
        elif pilihan == 0:
            print(Fore.GREEN + '\nTerima kasih telah menggunakan program kami!')
            break
        else:
            print(Fore.RED + 'Pilihan tidak valid, silakan pilih 1, 2, atau 0.')
            input(Fore.CYAN + 'Tekan Enter untuk mencoba lagi...' + Style.RESET_ALL)

if __name__ == "__main__":
    main()