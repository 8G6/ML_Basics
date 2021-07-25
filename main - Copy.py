from os import replace
import numpy as np 
import matplotlib.pyplot as plt
from time import sleep,time
import cv2
k='#'
j=0
y='['+k+'□□□□□□□□□□□□□□□□□□□□□'+']'
    laoding=y.replace('□','',len(k))
def ani(i,array,at):
    global j
    global k
    per=((i+1)/len(array)*100)
    current=int(per/at)
    if j!=current:
        k+='#'
    laoding='['+k+'                     ]'
    laoding=laoding.replace(' ','',len(k))
    e='\r'
    if current==int(len(array)/at):
        e='\n'
    print('converting '+' '+laoding+' '+str(int(per))+'% completed',end=e)
    j=current
def csv(dir):
    d=[]
    p=[]
    f=open(dir).read().split('\n')
    label=f[0].split(',')
    f=f[1:]
    c=0
    for i in f:
        i=i.split(',')
        p.append(i[0])
        d.append([int(i[1]),int(i[2])])
        ani(c,f,5)
        c+=1
    return [d,label,p]

def create(csv_dir,datapath,img_type='jpg'):
    data=[]
    val,lab,path=csv(csv_dir)
    start=time()
    j=0
    k='#'
    print('Started')
    for i in range(len(path)):
        img = cv2.imread(datapath+'//'+path[i]+'.'+img_type)
        res = cv2.resize(img,(70,50))
        per=((i+1)/len(path)*100)
        p=int(per/5)
        if p!=j:
            k+='#'
        laoding='['+k+'                     ]'
        laoding=laoding.replace(' ','',len(k))
        e='\r'
        if p==20:
            e='\n'
        print('converting '+' '+laoding+' '+str(int(per))+'% completed',end=e)
        data.append([res,val[i]])
        j=p
    end=time()
    t=(end-start)
    ips=len(path)/t
    print("Finished in "+str(int(t))+' seconds (',int(ips),'images per second )')
    return lab,data,t

create('./training.csv','./training')