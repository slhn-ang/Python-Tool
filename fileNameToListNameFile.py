import os

def save_file_names_to_txt(folder_path, output_file):
    with open(output_file, 'w') as file:
        for filename in os.listdir(folder_path):
            file.write(filename + '\n')

# Ganti path_folder dengan path folder yang ingin Anda baca
folder_path = r''
output_file = r''

save_file_names_to_txt(folder_path, output_file)
