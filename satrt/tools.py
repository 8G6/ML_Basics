from cv2 import namedWindow,resizeWindow,imshow,split,merge,imread,resize,waitKey,WINDOW_NORMAL,LUT,convertScaleAbs,imwrite
from numpy import arange,array
from random import choice 
from PIL import Image,ImageStat
from os import makedirs
from math import log
def log_base(num,base=15):
    return log(num)/log(base)

def brightness(img):
    Img=Image.open(img).convert('L')
    image=ImageStat.Stat(Img)
    return image.mean[0]

def img_show_fixed(name,array,options={'delay':0}):
    default=init(options)
    namedWindow(name,WINDOW_NORMAL)
    resizeWindow(name, default['s_width'], default['s_height'])
    imshow(name,array)
    waitKey(options['delay'])

def sort_array(string,array=[0,0,0]):
    string=string.replace(' ','',string.count(' '))
    sorted=[]
    red   = ['R','r']
    green = ['G','g']
    blue  = ['B','b']
    for i in string:
        if i in red:
            sorted.append(array[0])
        elif i in green:
            sorted.append(array[1])
        elif i in blue:
            sorted.append(array[2])
    return sorted

def convert(img_arr,mode):
    r, g, b = split(img_arr)
    mode=sort_array(mode,[r,g,b])
    img_arr = merge(mode)
    return img_arr

def init(options):
    default={'r_height':250,'r_width':300,'color_mode':'RGB','s_width':800,'s_height':600,'delay':0}
    for i in options:
        default[i] = options[i]
    return default

def resizer(img_dir,options):
    img = imread(img_dir)
    default=init(options)
    img=convert(img,default['color_mode'])
    img = resize(img,(default['r_width'],default['r_height']))
    return img

def adjust_gamma(image, gamma=1.0):
	g = 1.0 / gamma
	table = array([((i / 255.0) ** g) * 255
		for i in arange(0, 256)]).astype("uint8")
	return LUT(image,table)

def random_adjust(img,bns):
    bns=abs(2.75-log_base(bns,14))
    gamma=bns
    Contrast=bns
    return convertScaleAbs(adjust_gamma(img,gamma),alpha= Contrast)

def csv_get_data(csvdir):
    k,count,org,dit=[],[],{},{}
    f=open(csvdir).read().split('\n')
    label=f[0]
    f=f[1:]
    last=f[len(f)-1].split(',')[0]
    for i in f:
        i=i.split(',')
        try:
            k.append(i[1])
            org[i[0]]=int(i[1])
        except:
            pass

    for i in k:
        dit[int(i)]=k.count(i)

    label=sorted([i for i in dit])

    img=[[k for k,v in org.items() if v == i] for i in label]
    
    for i in label:
        count.append(dit[i])

    Max=max(count)
    needed=[(Max-i) for i in count]
    last=last.split('.')
    last=[last[0].split('_')[0],last[0].split('_')[1],last[1]]
    return [img,needed,count,last]

def save(img,path,name):
     makedirs(path,exist_ok=True)
     status=imwrite(path+name,img)
     if status:
         print('File written '+path+name,end='\r')
     else:
         print('error writing',end='\r')

