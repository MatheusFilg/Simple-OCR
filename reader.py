import glob
import pytesseract

img = glob.glob('files_images/*.jpg')

for i, image in enumerate(img):
    text = pytesseract.image_to_string(image,lang='por')
    print(text)