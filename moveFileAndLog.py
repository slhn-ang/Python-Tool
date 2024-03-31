import os
import shutil
from datetime import datetime

def move_files_between_folders(source_folder, destination_folder, log_file):
    # Step 1: Cek isi dari folder "A"
    files_to_move = set(os.listdir(source_folder))

    # Step 2: Cek isi dari folder "B"
    existing_files = set(os.listdir(destination_folder))

    # Step 3: Seleksi file untuk dipindahkan (file yang ada di "A" tetapi tidak ada di "B")
    files_to_copy = files_to_move - existing_files

    # Step 4: Pindahkan file ke folder "B" jika belum ada
    for file_to_copy in files_to_copy:
        source_path = os.path.join(source_folder, file_to_copy)
        destination_path = os.path.join(destination_folder, file_to_copy)

        # Pindahkan file hanya jika belum ada di folder "B"
        if file_to_copy not in existing_files:
            shutil.copyfile(source_path, destination_path)

    # Step 5: Buat file log
    with open(log_file, 'a') as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp}\n")  # Menulis waktu
        
        if files_to_copy:
            for file_name in files_to_copy:
                log.write(f"{file_name}\n")  # Menulis nama file yang dipindahkan
        else:
            log.write("Tidak ada file yang perlu dipindahkan\n")

# Menggunakan contoh folder dan log_file
folder_A = r''
folder_B = r''
log_file = r''

# Panggil fungsi untuk memindahkan file
move_files_between_folders(folder_A, folder_B, log_file)
