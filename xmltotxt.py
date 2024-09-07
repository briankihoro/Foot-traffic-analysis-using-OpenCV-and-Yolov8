import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(annotations_folder, output_folder, classes):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in os.listdir(annotations_folder):
        if file.endswith('.xml'):
            tree = ET.parse(os.path.join(annotations_folder, file))
            root = tree.getroot()

            image_width = int(root.find('size/width').text)
            image_height = int(root.find('size/height').text)

            output_file = os.path.join(output_folder, file.replace('.xml', '.txt'))
            with open(output_file, 'w') as f:
                for obj in root.iter('object'):
                    class_name = obj.find('name').text
                    class_id = classes.index(class_name)

                    xml_box = obj.find('bndbox')
                    x_min = float(xml_box.find('xmin').text)
                    y_min = float(xml_box.find('ymin').text)
                    x_max = float(xml_box.find('xmax').text)
                    y_max = float(xml_box.find('ymax').text)

                    # YOLO format requires normalized coordinates
                    x_center = (x_min + x_max) / 2.0 / image_width
                    y_center = (y_min + y_max) / 2.0 / image_height
                    width = (x_max - x_min) / image_width
                    height = (y_max - y_min) / image_height

                    # Write to the output file
                    f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

# Example usage:
annotations_folder = r"C:\Users\Administrator\Documents\Projects\yolov8Object-Detection-for-Public-Transport-Monitoring\images"
output_folder = r"C:\Users\Administrator\Documents\Projects\yolov8Object-Detection-for-Public-Transport-Monitoring\images2"
classes = ['person']  # List of class names

convert_voc_to_yolo(annotations_folder, output_folder, classes)
