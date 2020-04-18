import os
import json

CLASS_IDS = {'person':0, 'bicycle':1, 'car':2, 'motorbike':3, 'bus':4, 'truck':5}
CUR_PATH = os.path.dirname(os.path.abspath(__file__))
ANNO_PATH = os.path.join(CUR_PATH, 'annotations')
IMAGE_PATH = os.path.join(CUR_PATH, 'images')

annotation_list = os.listdir(ANNO_PATH)
json_annotation_list = [annotation for annotation in annotation_list if annotation.endswith('.json')]
    
def json_to_csv(anno_dir_path, image_dir_path, class_ids, output_filename):
    annotation_list = os.listdir(anno_dir_path)
    json_annotation_list = [annotation for annotation in annotation_list if annotation.endswith('.json')]

    json_datas = []

    for json_annotation in json_annotation_list:
        with open(os.path.join(anno_dir_path, json_annotation), "rb") as f:
            json_datas.append(json.load(f))
    
    with open(output_filename, 'w') as train_csv_file:
        for annotation_data in json_datas:
            for image_data in annotation_data:
                full_image_name = os.path.join(image_dir_path, image_data['External ID']).replace(' ', '')
                #if os.path.isfile(full_image_name) == False:
                    #print(full_image_name, "doesn't exist")
                object_list = image_data['Label']['objects']

                if len(object_list) == 0:
                    print(full_image_name, ' is empty')
                    continue
                bbox_str_list = ' '
                for object_data in object_list:
                    bbox = object_data['bbox']
                    class_id = class_ids[object_data['title']]
                    left = int(bbox['left'])
                    top = int(bbox['top'])
                    right = left + int(bbox['width'])
                    bottom = top + int(bbox['height'])
                    bbox_str = ('{0},{1},{2},{3},{4}').format(left, top, right, bottom, class_id)
                    bbox_str_list = bbox_str_list + bbox_str + ' '
                train_csv_file.write(full_image_name + bbox_str_list + '\n')

json_to_csv(ANNO_PATH, IMAGE_PATH, CLASS_IDS, os.path.join(ANNO_PATH, 'capstone.csv'))