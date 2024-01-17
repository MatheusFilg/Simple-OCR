import glob
from pdf2image import convert_from_path

files = glob.glob("files/*.pdf")

for i, file in enumerate(files):
    images = convert_from_path(file, use_pdftocairo=True, poppler_path=r"C:\Users\matheus\Desktop\Programaçao\Projetos\Release-23.11.0-0\poppler-23.11.0\Library\bin")

    for j in range(len(images)):
        file_name = file.split('.')[0].split('\\')[1]
        images[j].save('files_images/' + file_name + '-page' + str(j) + '.jpg')