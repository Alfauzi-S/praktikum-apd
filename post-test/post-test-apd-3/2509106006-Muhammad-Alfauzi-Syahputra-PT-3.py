nama_produk1 = 'Kopi Gula Aren G.A'
harga_produk1 = 10000
nama_produk2 = 'kopi Susu Kekinian'
harga_produk2 = 8000
nama_produk3 = 'Teh Tarik Selow'
harga_produk3 = 7000
nama_produk4 = 'Pisang Goreng Nugget'
harga_produk4 = 12000
nama_produk5 = 'Indomie Hypebeast'
harga_produk5 = 13000

username = 'alfauzi'
password = '006'

print(f'='*72)
print(f'Selamat Datang di Warkop Titik Kumpul'.center(72))
print(f'='*72)

status_member = input('Apakah Anda adalah seorang member? (y/n) : ').lower()

if status_member == 'y':
    print(f'\n{'-'*20}{' Silakan Login Terlebih Dahulu'.center(32)}{'-'*20}')
    username_input = input(f'{'Masukkan Username':<{20}}: ')
    password_input = input(f'{'Masukkan Password':<{20}}: ')
    status_login = True if username_input == username and password_input == password else print(f'\n{'-'*15}{' Maaf, username atau password Anda salah. '.center(40)}{'-'*15}')

    if status_login == True:
        pesan = f'Selamat datang kembali, {username}'
        print(f'{'-'*28}{' Login Berhasil '.center(16)}{'-'*28}\n{pesan.center(70)}\n{'-'*72}\n')

        print(f'Khusus buat kamu, member setia Titik Kumpul! Nikmati diskon 15%.'.center(70))
        print(f'Yuk, langsung pilih menu andalan kami di bawah ini.'.center(70))
        print(f'┌{'─'*70}┐')
        print(f'│{'Menu Warkop Titik Kumpul Kami'.center(70)}│')
        print(f'├{'─'*70}┤')
        print(f'│ 1. {nama_produk1:<30} : Rp{harga_produk1:>30,.0f} │')
        print(f'│ 2. {nama_produk2:<30} : Rp{harga_produk2:>30,.0f} │')
        print(f'│ 3. {nama_produk3:<30} : Rp{harga_produk3:>30,.0f} │')
        print(f'│ 4. {nama_produk4:<30} : Rp{harga_produk4:>30,.0f} │')
        print(f'│ 5. {nama_produk5:<30} : Rp{harga_produk5:>30,.0f} │')
        print(f'└{'─'*70}┘')

        print('\nSilakan masukkan jumlah pesanan (isi 0 jika tidak memesan):')
        jml_produk1 = int(input(f'- {nama_produk1:<25}: '))
        jml_produk2 = int(input(f'- {nama_produk2:<25}: '))
        jml_produk3 = int(input(f'- {nama_produk3:<25}: '))
        jml_produk4 = int(input(f'- {nama_produk4:<25}: '))
        jml_produk5 = int(input(f'- {nama_produk5:<25}: '))

        total_produk1 = (jml_produk1 * harga_produk1)
        total_produk2 = (jml_produk2 * harga_produk2)
        total_produk3 = (jml_produk3 * harga_produk3)
        total_produk4 = (jml_produk4 * harga_produk4)
        total_produk5 = (jml_produk5 * harga_produk5)
        harga_total = total_produk1 + total_produk2 + total_produk3 + total_produk4 + total_produk5

        if harga_total > 0:
            diskon = 0.15
            total_diskon = harga_total * diskon
            harga_setelah_diskon = harga_total - total_diskon

            print(f'\n┌{'─'*70}┐')
            print(f'│{'Struk Pembayaran Member'.center(70)}│')
            print(f'├{'─'*70}┤')
            
            if jml_produk1 > 0:
                print(f'│ {f'{nama_produk1} (x{jml_produk1})':<33} : Rp{total_produk1:>30,.0f} │')
            if jml_produk2 > 0:
                print(f'│ {f'{nama_produk2} (x{jml_produk2})':<33} : Rp{total_produk2:>30,.0f} │')              
            if jml_produk3 > 0:
                print(f'│ {f'{nama_produk3} (x{jml_produk3})':<33} : Rp{total_produk3:>30,.0f} │')
            if jml_produk4 > 0:
                print(f'│ {f'{nama_produk4} (x{jml_produk4})':<33} : Rp{total_produk4:>30,.0f} │')
            if jml_produk5 > 0:
                print(f'│ {f'{nama_produk5} (x{jml_produk5})':<33} : Rp{total_produk5:>30,.0f} │')

            print(f'├{'─'*70}┤')
            print(f'│ {'Harga Sebelum Diskon':<33} : Rp{harga_total:>30,.0f} │')
            print(f'│ {'Total Diskon (15%)':<33} : Rp{total_diskon:>30,.0f} │')
            print(f'├{'─'*70}┤')
            print(f'│ {'Total':<33} : Rp{harga_setelah_diskon:>30,.0f} │')
            print(f'└{'─'*70}┘') 
        else:
            print(f'\n{'-'*6}{' Lho, kok cuma lihat-lihat? Pesan dong, biar gak penasaran! '.center(58)}{'-'*6}')

else :
    print('-'*72)
    print(f'Selamat datang! Silakan pilih menu kami.'.center(72))
    print('-'*72)
    
    print(f'┌{'─'*70}┐')
    print(f'│{'Menu Warkop Titik Kumpul Kami'.center(70)}│')
    print(f'├{'─'*70}┤')
    print(f'│ 1. {nama_produk1:<30} : Rp{harga_produk1:>30,.0f} │')
    print(f'│ 2. {nama_produk2:<30} : Rp{harga_produk2:>30,.0f} │')
    print(f'│ 3. {nama_produk3:<30} : Rp{harga_produk3:>30,.0f} │')
    print(f'│ 4. {nama_produk4:<30} : Rp{harga_produk4:>30,.0f} │')
    print(f'│ 5. {nama_produk5:<30} : Rp{harga_produk5:>30,.0f} │')
    print(f'└{'─'*70}┘')

    print('\nSilakan masukkan jumlah pesanan (isi 0 jika tidak memesan):')
    jml_produk1 = int(input(f'- {nama_produk1:<25}: '))
    jml_produk2 = int(input(f'- {nama_produk2:<25}: '))
    jml_produk3 = int(input(f'- {nama_produk3:<25}: '))
    jml_produk4 = int(input(f'- {nama_produk4:<25}: '))
    jml_produk5 = int(input(f'- {nama_produk5:<25}: '))

    total_produk1 = (jml_produk1 * harga_produk1)
    total_produk2 = (jml_produk2 * harga_produk2)
    total_produk3 = (jml_produk3 * harga_produk3)
    total_produk4 = (jml_produk4 * harga_produk4)
    total_produk5 = (jml_produk5 * harga_produk5)
    harga_total = total_produk1 + total_produk2 + total_produk3 + total_produk4 + total_produk5
    
    if harga_total > 0:
        print(f'\n┌{'─'*70}┐')
        print(f'│{'Struk Pembayaran Member'.center(70)}│')
        print(f'├{'─'*70}┤')
        
        if jml_produk1 > 0:
            print(f'│ {f'{nama_produk1} (x{jml_produk1})':<33} : Rp{total_produk1:>30,.0f} │')
        if jml_produk2 > 0:
            print(f'│ {f'{nama_produk2} (x{jml_produk2})':<33} : Rp{total_produk2:>30,.0f} │')              
        if jml_produk3 > 0:
            print(f'│ {f'{nama_produk3} (x{jml_produk3})':<33} : Rp{total_produk3:>30,.0f} │')
        if jml_produk4 > 0:
            print(f'│ {f'{nama_produk4} (x{jml_produk4})':<33} : Rp{total_produk4:>30,.0f} │')
        if jml_produk5 > 0:
            print(f'│ {f'{nama_produk5} (x{jml_produk5})':<33} : Rp{total_produk5:>30,.0f} │')
            
        print(f'├{'─'*70}┤')
        print(f'│ {'Total':<33} : Rp{harga_total:>30,.0f} │')
        print(f'└{'─'*70}┘')
    else:
        print(f'\n{'-'*6}{' Lho, kok cuma lihat-lihat? Pesan dong, biar gak penasaran! '.center(58)}{'-'*6}')
print('-'*72)
print("Makasih udah mampir! Ditunggu nongkrong lagi di Titik Kumpul ya".center(70))
print('-'*72)