import os
import xml.etree.ElementTree as ET
from PIL import Image


data_dir = os.path.join(os.getcwd() , "DataSet/MaskRecognition")
img_dir = os.path.join(data_dir , "images")
anno_dir = os.path.join(data_dir , "annotations")
woc = 0
wc = 0

def Imagecrop(filename,status,x1,x2,y1,y2):
    global woc , wc
    img_path = os.path.join(img_dir , filename)
    full_img = Image.open(img_path)
    box = (x1,y1,x2,y2)
    cropped_image = full_img.crop(box)
    if(status=="without_mask"):
        woc +=1 
        cropped_image.save(f"/home/hcp_0/DL/Mask Detection/Data/Images/Without Mask/wo{woc}.png")
    else:
        wc += 1
        cropped_image.save(f'/home/hcp_0/DL/Mask Detection/Data/Images/With Mask/wc{wc}.png')
    
    
    

   

for file in os.listdir(anno_dir):
    file_path = os.path.join(anno_dir , file)
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    for object in root.findall('object'):
            status  = object.find('name').text
            square = object.find('bndbox')
            Imagecrop(root.find('filename').text,status,int(square.find('xmin').text),int(square.find('xmax').text),int(square.find('ymin').text),int(square.find('ymax').text))
 
        
