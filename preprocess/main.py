from os import listdir, path
from tools import resizer,init,show_sample,static
from time import time,sleep

class Image_preprocessor:
    def __init__(self,imgdir,csvpath,anime='■',options={'color_mode':'rgb'}):
        self.imgdir = imgdir
        self.csvpath = csvpath
        self.path=listdir(imgdir)
        self.options=init(options)
        self.anime=anime
        self.k=anime
        self.temp=0

    def ani(self,i,array,text='progress : '):
        per=((i+1)*100)//len(array)
        current=per//5
        p='['+self.k+'                    ]'.replace(' ','',len(self.k))
        if per>99:
            e='\n'
            self.k=''
        else:
            e='\r'
            if self.temp!=current:
                self.k+=self.anime
                self.temp=0
        g=static(self.path,i+1)
        q='   '.replace(' ','',len(str(per)))
        a=i+1
        b=len(self.path)
        print(f'{text} {per}{q}% {p} ({a}{g}/{b})',end=e)
        self.temp=current

    def csv(self):
        image_groudturuths=[]
        start=time()
        f=open(self.csvpath).read().split('\n')
        label=f[0].split(',')
        f=f[1:]
        c=0
        for i in f:
            self.ani(c,self.path)
            c+=1
            i=i.split(',')
            i=i[1:]
            image_groudturuths.append(i)
        end=time()
        t=(end-start)
        ips=int(len(self.path)/t)
        t='%.4f'%t
        print(f'Saved all data from {self.csvpath} to an array \ncompleted in {t}\n{ips} line per second\n')
        return image_groudturuths,label
    def single_image(self,img):
            return resizer(self.imgdir+'/'+img+'.jpg',self.options)

    def create(self):
        img_with_labels=[]
        info,label=self.csv()
        print("Started creating low res images")
        start=time()
        for i in range(len(self.path)):
            self.ani(i,self.path)
            img=resizer(self.imgdir+'/'+self.path[i],self.options)
            img_with_labels.append([img,info[i]])
        print("Ended creating low res images")
        end=time()
        t=(end-start)
        ips=int(len(self.path)/t)
        t='%.4f'%t
        print(f'Saved all data to an array \ncompleted in {t}\n{ips} images per second\n')
        return img_with_labels,label

    def show_sample(self,index,options):
        options=init(options)
        show_sample(self.imgdir+'/'+self.path[index-1],options)

    def for_loop(self,Time=0.05):
        for i in range(len(self.path)):
            self.ani(i,self.path)
            sleep(Time)