
import matplotlib.pyplot as plt
import numpy as n
from pre import Image_preprocessor
lib=Image_preprocessor('./test','./test.csv')

plt.style.use('fivethirtyeight')
f=open('test.csv').read().split('\n')
label=f[0]
f=f[1:]
k=[]
org={}
for i in f:
    i=i.split(',')
    try:
        k.append(i[1])
        org[i[0]]=int(i[1])
    except:
        break;

dit={}
for i in k:
    dit[int(i)]=k.count(i)
label=sorted([i for i in dit])
img=[[k for k,v in org.items() if v == i] for i in label]

count=[]

for i in label:
    count.append(dit[i])

Max=n.max(count)
needed=[(Max-i) for i in count]
print(needed,count)
ct=0
ct2=0
for i in img:
    for j in i:
       img=lib.single_image(j,str(ct))
       lib.ani(ct2,i,'status : '+img)
       ct2+=1
    ct2=0
    print('\nLoop',ct+1,'ended')
    ct+=1

plt.figure(0)
plt.bar(label,count)
plt.title('inital images')
plt.figure(1)
plt.bar(label,needed)
plt.title('needed images')
plt.show()