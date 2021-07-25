import numpy as np 
import matplotlib.pyplot as plt
from time import time
import cv2

def csv(dir):
    d=[]
    p=[]
    k='>'
    j=0
    c=0
    f=open(dir).read().split('\n')
    label=f[0].split(',')
    f=f[1:]
    for i in f:
        i=i.split(',')
        per=((c+1)/len(f)*100)
        current=int(per/5)
        if current!=j:
            k+='>'
        laoding='['+k+'                     ]'
        laoding=laoding.replace(' ','',len(k))
        e='\r'
        g=((' '*len(str(len(f)))).replace(' ','',len(str(int(per)))))
        o=(' '*len(str(len(f)))).replace(' ','',len(str(c)))
        if int(per)==100:
            e=' '
        print('appending to array from '+dir+' '+laoding+' '+str(int(per))+g+'% (',c,o+'/',len(f),') complete',end=e)
        print('\ncompleted\r') if int(per)==100 else 0
        j=current
        p.append(i[0])
        d.append([int(i[1])])
        c+=1
    return [d,label,p]

def create(csv_dir,datapath,img_type='jpg'):
    data=[]
    val,lab,path=csv(csv_dir)
    start=time()
    j=0
    k='#'
    print('')
    for i in range(len(path)):
        img = cv2.imread(datapath+'//'+path[i]+'.'+img_type)
        res = cv2.resize(img,(70,50))
        per=((i+1)/len(path)*100)
        g=(' '*len(str(len(path)))).replace(' ','',len(str(int(per))))
        o=(' '*len(str(len(path)))).replace(' ','',len(str(i)))
        p=int(per/5)
        if p!=j:
            k+='#'
        laoding='['+k+'                     ]'
        laoding=laoding.replace(' ','',len(k))
        e='\r'
        if p==20:
            e='\n'
        print('converting images to lower resolution '+' '+laoding+' '+str(int(per))+g+'% (',i,o+'/',len(path),') complete',end=e)
        data.append([res,val[i]])
        j=p
    end=time()
    t=(end-start)
    ips=len(path)/t
    print("Finished in "+str(int(t))+' seconds (',int(ips),'images per second )')
    return lab,data,t
for i in range(15):
    create('./test.csv','./test')