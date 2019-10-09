
# https://pypi.org/project/pytesseract/
#! pip install pytesseract
#! pip install opencv-python
#! pip install Pillow


path = input('Write path for processing: ')

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract'

rewrite = True
rewrite_type = input('Rewrite all files [y\\n]? ')
if rewrite_type =='y':
    rewrite = True
elif rewrite_type =='n':
    rewrite = False
else:
    print('Incorrect choosing')
    exit()

try:
    from PIL import Image
    from PIL import ImageFile
except ImportError:
    import Image
    import ImageFile
import pytesseract
# import argparse
# import cv2
import os
from tqdm import tqdm

ImageFile.LOAD_TRUNCATED_IMAGES = True

pytesseract.pytesseract.tesseract_cmd = tesseract_path

type_file_short = ('.jpg', '.png', '.bmp', '.dip', '.jpe', '.tif')
type_file_long = ('.tiff', 'jpeg')

number_path = len(list(os.walk(path)))

for root, dirs, files in tqdm(os.walk(path), total=number_path):
    for file in files:
        if file[-4:].lower() in type_file_short or  file[-5:].lower() in type_file_long:
            if file + '.txt' not in files or rewrite:
                image_path = os.path.join(root, file)
                text_file= open(root + '\\' + file + '.txt',"w+")
                try:
                    text = pytesseract.image_to_string(Image.open(image_path), lang='rus')
                    text_file.write(text.lower())
                    text_file.close()
                except OSError as error:
                    print(error)
                #print(image_path)

