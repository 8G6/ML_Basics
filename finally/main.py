from time import time
start=time()
from cv2 import imread,imshow,namedWindow,resizeWindow,waitKey,WINDOW_NORMAL
from os import listdir,system
from random import shuffle 
from numpy import array
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten,Conv2D,MaxPooling2D
end=time()
print("\n\nImported all modules in\n\n",end-start)

def img_show_fixed(name,array,options={'delay':1,'s_width':800,'s_height':600}):
    default=options
    namedWindow(name,WINDOW_NORMAL)
    resizeWindow(name, default['s_width'], default['s_height'])
    imshow(name,array)
    waitKey(options['delay'])

img,label,temp=[],[],[]
c=1
start=time()
for i in range(5):
    for j in listdir('./new/'+str(i)):
        print(c,"/",len(listdir('./new/'+str(i))),end='\r')
        try:
            data=imread('./new/'+str(i)+'/'+j)
            temp.append([i,data])
        except:
            pass
        c+=1
    c=0
    print('\nend\n')

shuffle(temp)

width=345
height=277


for i,j in temp:
    label.append(i)
    img.append(j)

img=array(img).reshape(-1,width,height,3)
img=img/255.0

end=time()
print("\n\nArray convertion Completed\n\n",end-start)
model=Sequential([
    Conv2D(filters= 16, kernel_size = (3,3), activation = 'relu',padding ='same', input_shape = (345,277,3) ),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Conv2D(filters= 32, kernel_size = (3,3), activation = 'relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Conv2D(filters= 32, kernel_size = (3,3), activation = 'relu'),
    MaxPooling2D(pool_size=(2,2), strides=(2,2)),
    Flatten(),
    Dense( units = 5, activation = 'softmax')
])

model.compile(
              loss = 'categorical_crossentropy', 
              metrics = ['accuracy']
)

model.summary()