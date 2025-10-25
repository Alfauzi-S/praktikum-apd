import os
from colorama import Fore

# prosedur
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# fungsi dengan parameter dan rekursif
def get_input(prompt):
    masukan = input(prompt)
    if masukan.strip():
        return masukan
    else:
        print(Fore.RED + "Input tidak boleh kosong.")
        return get_input(prompt)

# fungsi dengan parameter dan rekursif
def get_number(prompt):
    masukan = get_input(prompt)
    try:
        return int(masukan)
    except ValueError:
        print(Fore.RED + "Input harus berupa angka.")
        return get_number(prompt)