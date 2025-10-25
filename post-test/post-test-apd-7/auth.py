from colorama import Fore, Style
from data import users
from tools import get_input, clear

# fungsi tanpa paremeter
def login():
    clear()
    print(Fore.YELLOW + (f'{'='*18}{'HALAMAN LOGIN'}{'='*18}'))

    username = get_input('Masukkan Username: ')
    password = get_input('Masukkan Password: ')

    if username in users and users[username]['password'] == password:
        print(Fore.GREEN + (f'\n{'-'*18}{'Login berhasil'}{'-'*18}'))
        input(Fore.CYAN + 'Tekan Enter untuk melanjutkan...' + Style.RESET_ALL)

        peran = users[username]['role']
        return True, username, peran
    else:
        print(Fore.RED + (f'\n{'-'*19}{'Login gagal'}{'-'*19}'))
        input(Fore.CYAN + 'Tekan Enter untuk kembali...' + Style.RESET_ALL)
        
        return False, None, None

# fungsi tanpa parameter
def register():
    while True:
        clear()
        print(Fore.YELLOW + f'\n{'='*18}{'HALAMAN REGISTER'}{'='*18}')
        
        new_username = get_input('Username Baru (ketik "x" untuk kembali): ')
        if new_username.lower() == 'x':
            return None, None 

        if new_username in users:
            print(Fore.RED + '\nUsername sudah digunakan.')
            input(Fore.CYAN + 'Tekan Enter untuk coba lagi...' + Style.RESET_ALL)
        else:
            new_password = get_input('Password Baru: ')
            data_baru = {'password': new_password, 'role': 'user'}
            return new_username, data_baru