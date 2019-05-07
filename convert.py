import os

from flask import Flask, render_template, request
from wand.image import Image
from pyPdf import PdfFileReader, PdfFileWriter

# Function for preparing images from pdf
def prepare_images(pdf_path):
    # Output dir
    output_dir = os.path.join('', 'image')

    with(Image(filename=pdf_path, resolution=300, width=600)) as source:
        images = source.sequence
        pages = 1
        
        Image(images[1]).save(filename=output_dir + str(i) + '.png')
        
