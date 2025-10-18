from prettytable import PrettyTable

menu_utama = PrettyTable()
menu_utama.field_names = ['Pilihan', 'Deskripsi']
menu_utama.align['Deskripsi'] = 'l'
menu_utama.add_row(['1', 'Login                               '])
menu_utama.add_row(['2', 'Register                            '])
menu_utama.add_row(['0', 'Keluar                              '])

menu_admin = PrettyTable()
menu_admin.field_names = ['Pilihan', 'Deskripsi']
menu_admin.align['Deskripsi'] = 'l'
menu_admin.add_row(['1', 'Lihat Data Pertandingan (Read)      '])
menu_admin.add_row(['2', 'Tambah Data Pertandingan (Create)   '])
menu_admin.add_row(['3', 'Ubah Data Pertandingan (Update)     '])
menu_admin.add_row(['4', 'Hapus Data Pertandingan (Delete)    '])
menu_admin.add_row(['0', 'Logout'])

menu_user = PrettyTable()
menu_user.field_names = ['Pilihan', 'Deskripsi']
menu_user.align['Deskripsi'] = 'l'
menu_user.add_row(['1', 'Lihat Data Pertandingan              '])
menu_user.add_row(['0', 'Logout                               '])