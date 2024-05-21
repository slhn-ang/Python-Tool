import os
import shutil

# Direktori sumber dan tujuan
source_dir = 'path/to/Realface'  # Ganti dengan path folder sumber
destination_dir = 'path/to/destination'  # Ganti dengan path folder tujuan

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
                        print(f"Memindahkan {file} ke {folder}")
                        break

# Panggil fungsi untuk memindahkan file
move_files()