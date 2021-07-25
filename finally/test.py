from tools import csv_get_data,resizer,save,brightness,img_show_fixed,random_adjust
from cv2 import COLOR_BGR2HSV,split,cvtColor
img,count,needed,last=csv_get_data('../test.csv')
c=0
resize=[]
temp=[]

for i in img:
    for j in i:
        c+=1
        print('%d / %d '%(c,len(i)),end='\r')
        p=resizer('../test/'+j)
        img_show_fixed('before',p,{'delay':100})
        b=brightness(p)
        p=random_adjust(p,b)
        img_show_fixed('after',p,{'delay':100})
        temp.append([p,b])
    resize.append(temp)
    temp=[]
    c=0
    print('\nEnded\n')

for i in resize:
    for j in i:
        c+=1
        print('Writting files %d / %d '%(c,len(i)),end='\r')
        save(j[0],'resized/%d/'%resize.index(i),'%d_%d.jpg'%(resize.index(i),c),0)


