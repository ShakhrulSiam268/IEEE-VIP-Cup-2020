import os
import os
from PIL import Image 
import argparse
from tqdm import tqdm


def create_txt_file(select,train, extention = './dataset/'):

                #Define directories
    #=====================================================================================#
    #curdir=os.getcwd()
    if train==True:
        dayImg= extention[0] +'/images/train'
        dayLbs= extention[0] +'/labels/train'
        nightImg= extention[1] +'/images'
        # nightLbs= extention[1] +'/labels'
        nightLbs = '../input/dav-labels/dav_labels/night'

        print('image directory : ', dayImg)

        imgDirs=[dayImg,nightImg]
        lblDirs=[dayLbs,nightLbs]

        fileName=select+'_data.txt'
    else:
        testImg= extention +select+'/images/'
        testLbs= extention +select+'/labels/'

        imgDirs=[testImg]
        lblDirs=[testLbs]

        fileName=select+'_data.txt'

    #=====================================================================================#

    with open(fileName, 'w') as f:
        for xx in range(len(imgDirs)):
            labeldir=lblDirs[xx]
            imgdir=imgDirs[xx]
            labellist=sorted(os.listdir(labeldir))
            print('Length test:',len(labellist))
            for item in tqdm(labellist):
                imgloc=imgdir+'/'+ item.replace('txt','jpg')
                labelloc=labeldir+'/'+item
                f.write("%s " % imgloc)
                im=Image.open(imgloc)
                h,w=im.size
                with open(labelloc, 'r') as file:
                    boxes = file.readlines()
                    for box in boxes:
                        box=box.strip()
                        box=box.split(' ')
                        xcen=float(box[1])*w
                        ycen=float(box[2])*h
                        bw=float(box[3])*w
                        bh=float(box[4])*h
                        xmin=str(int(xcen-bw/2))
                        ymin=str(int(ycen-bh/2))
                        xmax=str(int(xcen+bw/2))
                        ymax=str(int(ycen+bh/2))
                        box=[xmin,ymin,xmax,ymax,box[0]]
                        box=','.join(box)
                        f.write(" %s " % box)
                    f.write("\n")
