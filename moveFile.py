import os
import shutil
from colorama import init, Fore, Style

# Inisialisasi colorama
init(autoreset=True)

# Direktori sumber dan tujuan
source_dir = r'Target Awal'  # Ganti dengan path folder sumber
destination_dir = r'Target Akhir'  # Ganti dengan path folder tujuan

# Buat folder tujuan jika belum ada
folders = ['body', 'faces', 'hair', 'hairlod', 'heads']
for folder in folders:
    os.makedirs(os.path.join(destination_dir, folder), exist_ok=True)

# Pemetaan awalan file ke folder tujuan
prefix_to_folder = {
    'eyes_': 'heads',
    'head_': 'heads',
    'face_': 'faces',
    'hair_': 'hair',
    'hairlod_': 'hairlod',
    'playerskin_': 'body'
}

# Menyimpan daftar file yang dipindahkan ke setiap folder
files_moved = {folder: [] for folder in folders}

# Fungsi untuk memindahkan file
def move_files():
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.rx3'):
                for prefix, folder in prefix_to_folder.items():
                    if file.startswith(prefix):
                        src_path = os.path.join(root, file)
                        dest_path = os.path.join(destination_dir, folder, file)
                        shutil.move(src_path, dest_path)
                        files_moved[folder].append(file)
                        break

# Panggil fungsi untuk memindahkan file
print(Fore.GREEN + "---- OPERASI DI MULAI ----\n")
move_files()

# Cetak hasil
for folder in folders:
    print(Fore.CYAN + f"~ Dipindahkan ke folder -> {folder} :")
    for i, file in enumerate(files_moved[folder], 1):
        print(f"- {i}. {file}")
    print(Fore.RED + f"~ Yang berjumlah {len(files_moved[folder])} file\n")

print(Fore.GREEN + "---- SELAMAT OPERASI BERHASIL ----")
