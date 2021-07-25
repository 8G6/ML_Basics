from time import time,sleep
import cv2
import os

k='■'
j=0
r=0

def static(array,per):
     return ((' '*len(str(len(array)))).replace(' ','',len(str(int(per)))))

def ani(i,array,text='complted : '):
    q=''
    w=['|', '/', '-', '\\']
    l=len(array)
    per=int(((i+1)*100)/l)
    current=int(per/5)
    e='\r'
    if j!=current:
        k+='■'
    elif r==3:
        r=0
        q=w[r]
    elif r<3:
        r+=1
        q=w[r]
    y='['+k+'□□□□□□□□□□□□□□□□□□□□]'
    laoding=y.replace('□','',len(k))
    g=static(array,per)
    t=static(array,i)
    if per>99:
        k=''
        e='\n'
    print(text,str(per)+g+'% ',laoding,' ('+str(i)+t+'/'+str(len(array)),')',q,end=e)
    j=current
    

def img_show_fixed(name,array,height=600,width=800):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, width, height)
    cv2.imshow(name,array)
#  img_show_fixed('Before',img)
#        img_show_fixed('After',res)
#       cv2.waitKey(0)
def csv(dir):
    image_groudturuths=[]
    f=open(dir).read().split('\n')
    label=f[0].split(',')
    f=f[1:]
    c=0
    for i in f:
        ani(c,f)
        c+=1
        i=i.split(',')
        i=i[1:]
        image_groudturuths.append(i)
    return image_groudturuths,label

def create(csv_dir,datapath):
    img_with_labels=[]
    info,label=csv(csv_dir)
    path=os.listdir(datapath)
    start=time()
    for i in range(len(path)):
        img = cv2.imread(datapath+'//'+path[i])
        res = cv2.resize(img,(277,300))
        r, g, b = cv2.split(res)
        k=[r,g,b]
        res = cv2.merge(k)
        img_with_labels.append([res,info[i]])
        ani(i,path)
    end=time()
    print(end-start)
    return img_with_labels,label

create('./test.csv','./test/')

