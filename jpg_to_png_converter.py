import sys
import os
from PIL import Image

input_directory = sys.argv[1]
output_directory = sys.argv[2]

if not os.path.isdir(output_directory):
    os.mkdir(output_directory)
    
for file in os.listdir(input_directory):
    with Image.open(f'{input_directory}\\{file}') as img:
        file_name = os.path.splitext(file)[0]
        img.save(f'{output_directory}\\{file_name}.png')

