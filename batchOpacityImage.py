from PIL import Image
import os

def decrease_opacity(input_path, output_path, opacity):
    image = Image.open(input_path).convert('RGBA')

    data = image.getdata()
    new_data = []

    for item in data:
        new_data.append((item[0], item[1], item[2], int(item[3] * opacity)))

    image.putdata(new_data)
    image.save(output_path)

# Path folder tempat file-file PNG berada
input_folder = r''
output_folder = r''
opacity_value = 0.4  # Ganti dengan nilai opacity yang diinginkan (0.0 - 1.0)

# Mendapatkan daftar file dalam folder input
input_files = os.listdir(input_folder)

# Melakukan penurunan opacity dan menyimpan ke folder output dengan nama yang tetap
for input_file in input_files:
    input_path = os.path.join(input_folder, input_file)
    output_path = os.path.join(output_folder, input_file)
    decrease_opacity(input_path, output_path, opacity_value)