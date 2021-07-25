
from time import sleep
k='#'
j=0
k='#'
def fixed_space(i,array):
    g=(' '*len(str(len(array))))
    g=g.replace(' ','',len(str(int(i))))
    return g
def ani(i,array):
    global k
    global j
    per=((i+1)*100)//len(array)
    c=per//5
    if c!=j:
        k+='#'
    y='['+k+'                     '+']'
    y=y.replace(' ','',len(k))
    g=fixed_space(per,array)
    f=fixed_space(i,array)
    print('Status : ',y,g+str(per)+'%',' ('+f+str(i+1)+' / '+str(len(array))+' ) ',end='\r')
    j=c

array = range(100)
for i in array:
    ani(i,array)
    sleep(0.1)
