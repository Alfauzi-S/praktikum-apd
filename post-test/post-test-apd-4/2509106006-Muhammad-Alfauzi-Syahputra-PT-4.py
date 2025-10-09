# free postes posttest 4 



import os
import time

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

nama_produk1 = 'Kopi Gula Aren G.A'
harga_produk1 = 10000
nama_produk2 = 'Kopi Susu Kekinian'
harga_produk2 = 8000
nama_produk3 = 'Teh Tarik Selow'
harga_produk3 = 7000
nama_produk4 = 'Pisang Goreng Nugget'
harga_produk4 = 12000
nama_produk5 = 'Indomie Hypebeast'
harga_produk5 = 13000

username_valid = 'alfauzi'
password_valid = '006'

while True:
    clear_screen()
    print(f'='*72)
    print(f'Selamat Datang di Warkop Titik Kumpul'.center(72))
    print(f'='*72)

    status_member = input('Apakah Anda adalah seorang member? (y/n) : ').lower()

    is_member = False
    
    if status_member == 'y':
        percobaan_login = 3
        while percobaan_login > 0:
            print(f'\n{'-'*20}{' Silakan Login Terlebih Dahulu'.center(32)}{'-'*20}')
            username_input = input(f'{'Masukkan Username':<{20}}: ')
            password_input = input(f'{'Masukkan Password':<{20}}: ')
            # Validasi input tidak boleh kosong atau hanya spasi
            if not username_input.strip() or not password_input.strip():
                percobaan_login -= 1
                print(f'\n{'-'*10} Username atau Password tidak boleh kosong! Sisa percobaan: {percobaan_login} {'-'*10}')
                time.sleep(2)
                continue
            if username_input == username_valid and password_input == password_valid:
                pesan = f'Selamat datang kembali, {username_valid}'
                print(f'\n{'-'*28}{' Login Berhasil '.center(16)}{'-'*28}\n{pesan.center(72)}\n{'-'*72}\n')
                is_member = True
                break
            else:
                percobaan_login -= 1
                if percobaan_login > 0:
                    print(f'\n{'-'*10} Maaf, username atau password Anda salah. Sisa percobaan: {percobaan_login} {'-'*10}')
                    time.sleep(2)
                else:
                    print(f'\n{'-'*15}{' Anda gagal login sebanyak 3 kali. '.center(42)}{'-'*15}')
                    print(f'Transaksi akan dilanjutkan sebagai non-member.'.center(72))
                    time.sleep(3)
                    break
    
    # Bagian ini akan dijalankan jika user bukan member atau gagal login
    clear_screen()
    if is_member:
        print(f'Khusus buat kamu, member setia Titik Kumpul! Nikmati diskon 15%.'.center(72))
        print(f'Yuk, langsung pilih menu andalan kami di bawah ini.'.center(72))
    else:
        print('-'*72)
        print(f'Selamat datang! Silakan pilih menu kami.'.center(72))
        print('-'*72)

    # --- Logika Belanja ---
    keranjang_belanja = ""
    total_harga = 0
    
    while True:
        print(f'\n┌{'─'*70}┐')
        print(f'│{'Menu Warkop Titik Kumpul Kami'.center(70)}│')
        print(f'├{'─'*70}┤')
        print(f'│ 1. {nama_produk1:<30} : Rp{harga_produk1:>30,.0f} │')
        print(f'│ 2. {nama_produk2:<30} : Rp{harga_produk2:>30,.0f} │')
        print(f'│ 3. {nama_produk3:<30} : Rp{harga_produk3:>30,.0f} │')
        print(f'│ 4. {nama_produk4:<30} : Rp{harga_produk4:>30,.0f} │')
        print(f'│ 5. {nama_produk5:<30} : Rp{harga_produk5:>30,.0f} │')
        print(f'├{'─'*70}┤')
        print(f'│ 6. {'Checkout'.center(65)}│')
        print(f'└{'─'*70}┘')
        
        pilihan = input('\nSilakan pilih menu (1-6) : ')

        if pilihan == '1':
            total_harga += harga_produk1
            keranjang_belanja += f'│ {nama_produk1:<33} : Rp{harga_produk1:>30,.0f} │\n'
            pesan_item = f'{nama_produk1} berhasil ditambahkan ke keranjang!'
        elif pilihan == '2':
            total_harga += harga_produk2
            keranjang_belanja += f'│ {nama_produk2:<33} : Rp{harga_produk2:>30,.0f} │\n'
            pesan_item = f'{nama_produk2} berhasil ditambahkan ke keranjang!'
        elif pilihan == '3':
            total_harga += harga_produk3
            keranjang_belanja += f'│ {nama_produk3:<33} : Rp{harga_produk3:>30,.0f} │\n'
            pesan_item = f'{nama_produk3} berhasil ditambahkan ke keranjang!'
        elif pilihan == '4':
            total_harga += harga_produk4
            keranjang_belanja += f'│ {nama_produk4:<33} : Rp{harga_produk4:>30,.0f} │\n'
            pesan_item = f'{nama_produk4} berhasil ditambahkan ke keranjang!'
        elif pilihan == '5':
            total_harga += harga_produk5
            keranjang_belanja += f'│ {nama_produk5:<33} : Rp{harga_produk5:>30,.0f} │\n'
            pesan_item = f'{nama_produk5} berhasil ditambahkan ke keranjang!'
        elif pilihan == '6':
            break
        else:
            clear_screen()
            print("Pilihan tidak valid, silakan masukkan nomor menu yang benar.")
            clear_screen()
            continue
        
        clear_screen()
        print(f'{pesan_item.center(72)}')
        print(f'Total belanja sementara: Rp{total_harga:,.0f}'.center(72))
        time.sleep(2)
        clear_screen()


    clear_screen()
    if total_harga > 0:
        print(f'┌{'─'*70}┐')
        if is_member:
            print(f'│{'Struk Pembayaran Member'.center(70)}│')
        else:
            print(f'│{'Struk Pembayaran'.center(70)}│')
        print(f'├{'─'*70}┤')
        
        # Mencetak isi keranjang
        print(keranjang_belanja, end="")

        print(f'├{'─'*70}┤')

        if is_member:
            diskon = 0.15
            total_diskon = total_harga * diskon
            harga_setelah_diskon = total_harga - total_diskon
            print(f'│ {'Harga Sebelum Diskon':<33} : Rp{total_harga:>30,.0f} │')
            print(f'│ {'Total Diskon (15%)':<33} : Rp{total_diskon:>30,.0f} │')
            print(f'├{'─'*70}┤')
            print(f'│ {'Total yang harus dibayar':<33} : Rp{harga_setelah_diskon:>30,.0f} │')
        else:
            print(f'│ {'Total yang harus dibayar':<33} : Rp{total_harga:>30,.0f} │')
        
        print(f'└{'─'*70}┘')
    else:
        print(f'\n{'-'*6}{' Lho, kok cuma lihat-lihat? Pesan dong, biar gak penasaran! '.center(60)}{'-'*6}')

    # --- Konfirmasi Transaksi Baru ---
    print('\n' + '-'*72)
    transaksi_baru = input("Apakah Anda ingin memulai transaksi baru? (y/n) : ").lower()
    if transaksi_baru != 'y':
        break

# --- Pesan Penutup ---
clear_screen()
print('-'*72)
print("Makasih udah mampir! Ditunggu nongkrong lagi di Titik Kumpul ya".center(72))
print('-'*72)