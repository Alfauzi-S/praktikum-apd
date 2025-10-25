# tools.py

import os
from colorama import Fore

# prosedur
def clear():
    """Prosedur untuk membersihkan layar."""
    os.system('cls' if os.name == 'nt' else 'clear')

# fungsi dengan parameter
def get_input(prompt):
    """Fungsi rekursif untuk memastikan input tidak kosong."""
    masukan = input(prompt)
    if masukan.strip():
        return masukan
    else:
        print(Fore.RED + "Input tidak boleh kosong.")
        return get_input(prompt)

# fungsi dengan parameter
def get_number(prompt):
    """Fungsi rekursif untuk memastikan input adalah angka."""
    masukan = get_input(prompt)
    try:
        return int(masukan)
    except ValueError:
        print(Fore.RED + "Input harus berupa angka.")
        return get_number(prompt)