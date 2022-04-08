#!/usr/bin/python3
import glob
from PIL import Image
from fpdf import FPDF


# single image to pdf
image1 = Image.open('/home/jaki/Pictures/cake.png')
im1 = image1.convert('RGB')
im1.save('/home/jaki/Dev/django_scripts/apps/converter/scripts/single.pdf')


# list of image to pdf - 01
images = [
    Image.open('/home/jaki/Pictures/' + f) for f in ['cake.png', 'cake_1.jpeg', 'pizza.jpeg']
]

pdf_path = '/home/jaki/Dev/django_scripts/apps/converter/scripts/multiple.pdf'

images[0].save(pdf_path, "PDF", esolution=100.0, save_all=True, append_images=images[1:])


# list of image to pdt - 02
pdf = FPDF('P', 'mm', 'A4')

image_list = glob.glob('/home/jaki/Pictures/ImageToPDF/*.jpg')

for img in image_list:
    pdf.add_page()
    # pdf.image(img, 10, 210, 297)
    pdf.image(img, x=None, y=None, w=190.0, h=0)

pdf_path2 = "/home/jaki/Dev/django_scripts/apps/converter/scripts/multiple2.pdf"

pdf.output(pdf_path2, "F")
