from numpy import arange,array
from random import choice as c
from imutils import rotate as r
from PIL import Image,ImageStat
from cv2 import namedWindow,WINDOW_NORMAL,resizeWindow,imshow,waitKey,imread,LUT,convertScaleAbs

def img_show_fixed(name,array):
    namedWindow(name,WINDOW_NORMAL)
    resizeWindow(name, 800,600 )
    imshow(name,array)
    waitKey(1000)
img = imread('IDRiD_001.jpg')

 
def adjust_gamma(image, gamma=1.0):
	invGamma = 1.0 / gamma
	table = array([((i / 255.0) ** invGamma) * 255
		for i in arange(0, 256)]).astype("uint8")
	return LUT(image, table)

def brightness( im_file ):
   print(im_file)

gama=arange(0.9,1.6,0.02)
bright=range(1,100)
contrast=arange(1,3,0.1)
same=[]
pg=0
cont=0
while True:
    gamma=1.2
    Contrast=2
    cont+=1
    img_show_fixed('before',img)
    cg='Contrast : '+str(Contrast)+' Gamma : '+str(gamma)+"   len : "+str(pg*100/cont)
    if cg in same:
        gamma=c(gama)
        pg+=1
        Contrast=c(contrast)
        cg='Contrast : '+str(Contrast)+' Gamma : '+str(gamma)+"   len : "+str(pg*100/cont)
    same.append(cg)
    print(cg)
    rotated = convertScaleAbs(adjust_gamma(img,gamma),alpha= Contrast)
    img_show_fixed("after",rotated,c)
