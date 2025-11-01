from prettytable import PrettyTable

# variabel global
main_display = PrettyTable()
main_display.field_names = ['Pilihan', 'Deskripsi']
main_display.align['Deskripsi'] = 'l'
main_display.add_row(['1', 'Login                               '])
main_display.add_row(['2', 'Register                            '])
main_display.add_row(['0', 'Keluar                              '])

# variabel global
admin_display = PrettyTable()
admin_display.field_names = ['Pilihan', 'Deskripsi']
admin_display.align['Deskripsi'] = 'l'
admin_display.add_row(['1', 'Lihat Data Pertandingan (Read)      '])
admin_display.add_row(['2', 'Tambah Data Pertandingan (Create)   '])
admin_display.add_row(['3', 'Ubah Data Pertandingan (Update)     '])
admin_display.add_row(['4', 'Hapus Data Pertandingan (Delete)    '])
admin_display.add_row(['0', 'Logout'])

#variabel global
user_display = PrettyTable()
user_display.field_names = ['Pilihan', 'Deskripsi']
user_display.align['Deskripsi'] = 'l'
user_display.add_row(['1', 'Lihat Data Pertandingan              '])
user_display.add_row(['0', 'Logout                               '])