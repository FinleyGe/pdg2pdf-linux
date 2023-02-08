#! /usr/bin/env python3
# transfer .pdg to pdf

import sys
import zipfile
from PIL import Image
import os
def pdg2pdf(pdgfile:zipfile.ZipFile, target: str):
    pdgfile.extractall('./temp')
    pdgfile.close()
    toc:list[str] = []
    content:list[str] = []
    cov1:str = ''
    cov2:str = ''
    bok:list[str] = []
    fow:list[str] = []
    leg:list[str] = []
    for file in os.listdir('./temp'):
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
    image_list:list[Image.Image] = []

    if cov1 != '':
        image_list.append(Image.open('./temp/' + cov1))

    for b in bok:
        image_list.append(Image.open('./temp/' + b))

    for l in leg:
        image_list.append(Image.open('./temp/' + l))

    for f in fow:
        image_list.append(Image.open('./temp/' + f))

    for t in toc:
        image_list.append(Image.open('./temp/' + t))

    for c in content:
        image_list.append(Image.open('./temp/' + c))

    if cov2 != '':
        image_list.append(Image.open('./temp/' + cov2))
    
    image_list[0].save(target, "PDF", save_all=True, append_images=image_list[1:])

    # delele all temp file 
    for file in os.listdir('./temp'):
        os.remove('./temp/' + file)
    os.rmdir('./temp')

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
