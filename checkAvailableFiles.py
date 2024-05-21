import os
from datetime import datetime

# Lokasi folder A dan B
folder_a = r'C:\Users\Aang Solihin\Pictures\256x256'
folder_b = r'C:\Users\Aang Solihin\Pictures\64x64'

# Mendapatkan daftar nama file di masing-masing folder
files_in_a = set(os.listdir(folder_a))
files_in_b = set(os.listdir(folder_b))

# Mencari file yang belum tersedia di folder B
files_not_in_b = files_in_a - files_in_b

# Mendapatkan waktu saat ini
current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

# Membuat atau membuka file log
with open('log_file_status.txt', 'a') as log_file:
    if files_not_in_b:
        # Jika ada file yang belum ada di folder B, mencatat di log
        log_message = f"{current_time} : {', '.join(files_not_in_b)} Belum Ada Dalam Folder B.\n"
        print(log_message)
        log_file.write(log_message)
    else:
        # Jika semua file sudah ada di folder B
        log_message = f"{current_time} : Semua File Sudah Tersedia\n"
        print(log_message)
        log_file.write(log_message)
