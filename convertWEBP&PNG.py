from PIL import Image
import os
from colorama import init, Fore, Style

# Inisialisasi colorama
init(autoreset=True)

def check_and_convert_image(file_path, output_path):
    try:
        with Image.open(file_path) as img:
            # Cek format gambar
            if img.format == 'WEBP':
                # Konversi jika format asli adalah WEBP
                img.save(output_path, 'PNG')
                return True, f"File '{file_path}' (WEBP) dikonversi ke '{output_path}'"
            elif img.format == 'PNG':
                # Salin jika format asli adalah PNG
                if file_path != output_path:
                    img.save(output_path, 'PNG')
                return True, f"File '{file_path}' (PNG asli) disalin ke '{output_path}'"
            else:
                return False, f"File {file_path} bukan format PNG atau WEBP."
    except Exception as e:
        return False, f"Error processing file {file_path}: {e}"

# Path ke direktori input dan output
input_dir = r'C:\Users\Aang Solihin\Pictures\Madrid'
output_dir = r'C:\Users\Aang Solihin\Pictures\Real Madrid'

# Pastikan direktori output ada
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Cek apakah direktori input ada
if not os.path.exists(input_dir):
    print(Fore.RED + f"Error: Direktori input '{input_dir}' tidak ditemukan.")
else:
    # Inisialisasi variabel
    processed_files = []
    error_messages = []

    # Loop melalui semua file di direktori input
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.png') or file_name.endswith('.webp'):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.png')
            
            # Panggil fungsi untuk mengonversi file
            success, message = check_and_convert_image(input_path, output_path)
            if success:
                processed_files.append(file_name)
            else:
                error_messages.append(message)
        else:
            error_messages.append(Fore.RED + f"File {file_name} bukan format PNG atau WEBP.")

    # Output hasil proses
    print(Fore.YELLOW + "---- Proses Di Mulai ----")
    for file_name in processed_files:
        print(Fore.GREEN + f"• {file_name}")
    print(Fore.YELLOW + f"---- Proses Berhasil Dijalankan Dengan {Fore.CYAN}{len(processed_files)}{Fore.YELLOW} Tersedia ----")
    
    # Tampilkan pesan error jika ada
    if error_messages:
        print(Fore.RED + "---- Pesan Error ----")
        for error in error_messages:
            print(Fore.RED + error)
