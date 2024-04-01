from PIL import Image
import os

input_folder = r''
output_folder = r''
target_size = (32, 32)
files_per_batch = 20  # Jumlah file per kelompok

# Ambil semua file PNG dari folder input
png_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".png")]

# Bagi file menjadi kelompok-kelompok dengan jumlah yang ditentukan
file_batches = [png_files[i:i + files_per_batch] for i in range(0, len(png_files), files_per_batch)]

# Proses resize secara bertahap untuk setiap kelompok
for batch_index, file_batch in enumerate(file_batches, start=1):
    print(f"Processing Batch {batch_index} = {len(file_batch)} File")

    for filename in file_batch:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Pastikan direktori output ada
            output_directory = os.path.dirname(output_path)
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            img = Image.open(input_path)

            # Pastikan gambar memiliki format PNG dan ukuran awal adalah 256x256
            if img.format == 'PNG' and img.size == (256, 256):
                img_resized = img.resize(target_size, resample=Image.LANCZOS)
                img_resized.save(output_path)
            else:
                print(f"Ignoring {filename} because it is not a PNG image or its size is not {initial_size}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Resize selesai.")
