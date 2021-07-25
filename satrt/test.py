from tools import resizer,random_adjust,img_show_fixed,brightness,csv_get_data,save
from os import listdir
from time import time
p='../training/'

img,needed,count,last=csv_get_data('../training.csv')

path=listdir(p)
c=0

print(needed)

start=time()
a=[]
b=[]
for i in img:
    for j in i:
        val=brightness(p+j)
        a.append(val)
        img=resizer(p+j,{'r_width':345,'r_height':277})
        img_show_fixed('before',img,{'delay':1})
        img=random_adjust(img,val)
        img_show_fixed('after',img,{'delay':1})
        save(img,'../finally/new/'+str(c)+'/',j)
    b.append(a)
    a=[]
    c+=1

c=0

c=[]

index=0

end=time()

print(end-start)