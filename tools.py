
from cv2 import namedWindow,resizeWindow,imshow,split,merge,imread,resize,waitKey,WINDOW_NORMAL

def img_show_fixed(name,array,image_res):
    namedWindow(name,WINDOW_NORMAL)
    resizeWindow(name, image_res['width'], image_res['height'])
    imshow(name,array)
    
def static(array,per):
     return ((' '*len(str(len(array)))).replace(' ','',len(str(int(per)))))

def sort_array(string,array=[0,0,0]):
    empty=0
    for i in string:
        if i==' ':
            empty+=1
    string=string.replace(' ','',empty)
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
    default={'resize_height':300,'resize_width':250,'show_height':400,'show_width':600,'color_mode':'RGB','close_after':0}
    for i in options:
        default[i] = options[i]
    return default

def show_sample(img_dir,options={'color_mode':'RGB'}):
    default=init(options)
    img = imread(img_dir)
    res = resize(img,(default['resize_height'],default['resize_width']))
    img=convert(img,default['color_mode'])
    res=convert(res,default['color_mode'])
    show={'height':default['show_height'],'width':default['show_width']}
    img_show_fixed('Orginal',img,show)
    img_show_fixed('Resized',res,show)
    waitKey(default['close_after']*1000)

def resizer(img_dir,options):
    img = imread(img_dir)
    default=init(options)
    img=convert(img,default['color_mode'])
    img = resize(img,(default['resize_height'],default['resize_width']))
    return img
