import os
import shutil
from colorama import init, Fore, Style
from datetime import datetime

# Inisialisasi colorama
init()

def read_numbers_from_file(file_path):
    numbers = {}
    try:
        with open(file_path, 'r') as file:
            line_number = 1
            for line in file:
                line = line.strip()
                if line.startswith('-'):  # Abaikan baris yang dimulai dengan "-"
                    line_number += 1
                    continue
                try:
                    number = int(line)
                    numbers[str(number)] = line_number  # Simpan nomor dan nomor baris
                except ValueError:
                    # Jika baris tidak bisa dikonversi ke integer, abaikan
                    continue
                line_number += 1
    except FileNotFoundError:
        print(Fore.RED + "~ Oops! sepertinya anda tak memasukan list file - file atau path yang salah." + Style.RESET_ALL)
        return None
    return numbers

def get_png_files_from_folder(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.png')]

def extract_number_from_filename(filename):
    if filename.startswith('l') and filename.endswith('.png'):
        return filename[1:-4]  # Menghapus 'l' di depan dan '.png' di belakang
    return None

def move_files(source_folder, destination_folder, valid_numbers, log_file):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    png_files = get_png_files_from_folder(source_folder)
    moved_files = 0
    moved_file_list = []
    failed_file_list = []
    
    with open(log_file, 'w') as log:
        # Tambahkan timestamp ke log
        log.write(f"~ {datetime.now().strftime('%A, %H:%M:%S (%d-%m-%Y)')}\n")
        
        for filename in png_files:
            number = extract_number_from_filename(filename)
            if number and number in valid_numbers:
                source_path = os.path.join(source_folder, filename)
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(source_path, destination_path)
                moved_file_list.append((filename, valid_numbers[number]))
                log.write(f"- Line : {valid_numbers[number]} -> {filename}\n")
                print(Fore.GREEN + f"• {filename}" + Style.RESET_ALL)
                moved_files += 1
                valid_numbers.pop(number)  # Remove the number to avoid duplicate processing

        if moved_file_list:
            log.write(f"------> {len(moved_file_list)}\n")
        
        # Check for files that could not be moved because they do not exist
        if valid_numbers:
            log.write("\n[File Ini Gagal Di Pindahkan]\n")
            for number, line in valid_numbers.items():
                failed_file_list.append((f"l{number}.png", line))
                log.write(f"- Line : {line} -> l{number}.png\n")
            log.write(f"------> {len(failed_file_list)}\n")
    
    return len(png_files), moved_files, moved_file_list, failed_file_list

def main():
    # Definisikan path file teks dan folder
    numbers_file = r'C:\Users\Aang Solihin\Pictures\numbers.txt'  # Ganti dengan path ke file teks Anda
    source_folder = r'C:\Users\Aang Solihin\Pictures\Gas'  # Ganti dengan path ke folder sumber Anda
    destination_folder = r'C:\Users\Aang Solihin\Pictures\Done'  # Ganti dengan path ke folder tujuan Anda
    log_file = os.path.join(os.path.dirname(__file__), 'file_moving_log.txt')
    
    print(Fore.YELLOW + "---- Program Dimulai ----" + Style.RESET_ALL)
    
    valid_numbers = read_numbers_from_file(numbers_file)
    if valid_numbers is None:
        print(Fore.RED + "~ Oops! sepertinya anda tak memasukan list file - file atau path yang salah." + Style.RESET_ALL)
    else:
        total_files, moved_files, moved_file_list, failed_file_list = move_files(source_folder, destination_folder, valid_numbers, log_file)
        
        if moved_files > 0:
            print(Fore.GREEN + "[File Berhasil Di Pindahkan]" + Style.RESET_ALL)
            for file, line in moved_file_list:
                print(Fore.GREEN + f"• {file}" + Style.RESET_ALL)
        
        if failed_file_list:
            print(Fore.RED + "[File Gagal Di Pindahkan]" + Style.RESET_ALL)
            for file, line in failed_file_list:
                print(Fore.RED + f"• {file}" + Style.RESET_ALL)
        
        if moved_files > 0 and failed_file_list:
            print(Fore.YELLOW + f"~ File yang ada dalam '{os.path.basename(source_folder)}' yang berisi {total_files} file, serta {moved_files} file telah berhasil dipindahkan dan {len(failed_file_list)} file tak tersedia dalam folder." + Style.RESET_ALL)
        elif moved_files > 0 and not failed_file_list:
            print(Fore.YELLOW + f"~ File yang ada dalam '{os.path.basename(source_folder)}' yang berisi {total_files} file, serta {moved_files} semuanya telah berhasil dipindahkan." + Style.RESET_ALL)
        elif not moved_files:
            print(Fore.RED + "~ Oops! file tak tersedia dalam folder." + Style.RESET_ALL)

    print(Fore.YELLOW + "---- Program Selesai ----" + Style.RESET_ALL)

if __name__ == "__main__":
    main()