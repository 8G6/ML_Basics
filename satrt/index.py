from os import listdir
from time import time

def Dir(imgdir):
    path=listdir(imgdir)
    k=[imgdir+'/'+i for i in path]
    return k
class Data_Optimizer():
    def __init__(self,imgdir,csvpath,options):
        self.imgdir  = imgdir
        self.csvpath = csvpath
        self.path    = Dir(imgdir)
        self.options = options
    


    def create(self,img,fn):
        img=resizer(p+i,{'width':300,'height':277})
        img_show_fixed('brfore',img,{'delay':100})
        img=random_adjust(img,val)
        img_show_fixed('image',img,{'delay':10})
        makedirs(self.imgdir+'/'+fn,exist_ok=True)
        image=resizer(self.imgdir+'/'+img,self.options)
        status = imwrite(self.imgdir+'/'+fn+'/'+img,image)
        if status:
            return 'File written '+self.imgdir+'/'+fn+'/'+img
        else:
            return 'error writing'
