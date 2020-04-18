import os
from os import rename, listdir

files = listdir('.')
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
dir_list = [dir_name for dir_name in files if os.path.isdir(dir_name) and dir_name.startswith('.') != True]
IMAGE_FORMAT = '.png'
print(dir_list)
for dir_name in dir_list:
    full_dir_name = os.path.join(CUR_PATH, dir_name)
    file_names = listdir(full_dir_name)
    image_names = [image_name for image_name in file_names if image_name.endswith(IMAGE_FORMAT)]
    for image_name in image_names: 
        new_name = image_name.replace(' ', '')
        rename(os.path.join(full_dir_name, image_name), os.path.join(full_dir_name, new_name))
