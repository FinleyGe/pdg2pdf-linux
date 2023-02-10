#! /usr/bin/env python3
# transfer .pdg to pdf

import sys
import zipfile
from PIL import Image
import os
import shutil
import fitz
from nipype.interfaces.io import glob

def pdg2pdf(pdgfile:zipfile.ZipFile, target: str):
    # extract all .pdg file 
    for file in pdgfile.namelist():
        if file[-4:] == ".pdg":
            pdgfile.extract(file, "temp")
    pdgfile.close()
    toc:list[str] = []
    content:list[str] = []
    cov1:str = ''
    cov2:str = ''
    bok:list[str] = []
    fow:list[str] = []
    leg:list[str] = []
    # file_path is the path of .pdg file 

    file_path = "temp/"
    if os.path.isdir("temp/" + os.listdir(file_path)[0]):
        file_path = os.path.join('temp/', os.listdir('temp')[0])
        file_path+='/'

    for file in os.listdir(file_path):
        if file.endswith('.pdg'):
            if file.startswith('!'):
                toc.append(file)
            elif file.startswith('fow'):
                fow.append(file)
            elif file.startswith('leg'):
                leg.append(file)
            elif file == 'cov001.pdg':
                cov1 = 'cov001.pdg'
            elif file == 'cov002.pdg':
                cov2  = 'cov002.pdg'
            elif file.startswith('bok'):
                bok.append(file)
            else:
                content.append(file)
    content.sort()
    fow.sort()
    leg.sort()
    toc.sort()
    image_path_list:list[str] = []
    image_list:list[Image.Image] = []

    if cov1 != '':
        image_path_list.append(file_path + cov1)
        image_list.append(Image.open(file_path + cov1))

    for b in bok:
        image_path_list.append(file_path + b)
        image_list.append(Image.open(file_path + b))

    for l in leg:
        image_path_list.append(file_path + l)
        image_list.append(Image.open(file_path + l))

    for f in fow:
        image_path_list.append(file_path + f)
        image_list.append(Image.open(file_path + f))

    for t in toc:
        image_path_list.append(file_path + t)
        image_list.append(Image.open(file_path + t))

    for c in content:
        image_path_list.append(file_path + c)
        image_list.append(Image.open(file_path + c))

    if cov2 != '':
        image_path_list.append(file_path + cov2)
        image_list.append(Image.open(file_path + cov2))

    doc = fitz.open()
    length = len(image_path_list)
    now = 0
    for img in image_path_list:
        now += 1
        print("\rProcessing: " + str(now) + "/" + str(length) + "    " + "{:.2f}".format(now / length * 100) + "%", end="")
        imgdoc = fitz.open(img, filetype="png")
        pdfbytes = imgdoc.convert_to_pdf()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)
    doc.save(target)
    doc.close()

    # image_list[0].save(target, "PDF", save_all=True, append_images=image_list[1:])

    # delele all temp file 
    shutil.rmtree("temp")
def main():
    param:list[str] = sys.argv
    if len(param) != 3:
        print("Usage: python pdg2pdf.py filename output.pdf")
        return
    file_path:str = param[1]
    if file_path[-4:] != ".zip":
        print("Usage: Input FileType must be .zip")
        return
    pdgfile:zipfile.ZipFile = zipfile.ZipFile(file_path)
    pdg2pdf(pdgfile, param[2])

if __name__ == '__main__':
    main()
