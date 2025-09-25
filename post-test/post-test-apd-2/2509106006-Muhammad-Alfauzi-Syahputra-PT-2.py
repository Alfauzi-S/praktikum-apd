#input
print("="*80)
print(f'{'PROGRAM CEK BERAT BADAN IDEAL'}'.center(80))
print("="*80)
nama_pasien = str(input(f"{'Masukkan nama pasien':<{30}}: "))
tinggi_badan = float(input(f"{'Masukkan tinggi badan (cm)':<{30}}: "))
berat_badan = float(input(f"{'Masukkan berat badan (kg)':<{30}}: "))
print("="*80)

# Logic
statuslist = ["Tidak Kelebihan Berat Badan","Kelebihan Berat Badan"]
beratideal = tinggi_badan - 100
iskelebihan = berat_badan > beratideal
status = statuslist[int(iskelebihan)]

# Output
lebar = 78
print(f"┌{'─'*lebar}┐")
print(f"│{'HASIL CEK BERAT BADAN':^{lebar}}│")
print(f"├{'─'*lebar}┤")
print("│ {:<20} : {:<54}│".format("Nama Pasien", nama_pasien))
print("│ {:<20} : {:<54}│".format("Tinggi Badan", f"{tinggi_badan:.0f} cm"))
print("│ {:<20} : {:<54}│".format("Berat Badan", f"{berat_badan:.0f} kg"))
print("│ {:<20} : {:<54}│".format("Berat Ideal", f"{beratideal:.0f} kg"))
print("│ {:<20} : {:<54}│".format("Status", status))
print(f"└{'─'*lebar}┘")
