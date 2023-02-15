
from ast import literal_eval
import numpy as np
s=(720,607)
pic=open('canny.txt','r')
test=np.zeros(s)
line=pic.readline()
line=literal_eval(line)
for i in line:
    tmp=i.split('.')
    print(tmp)
    test[int(tmp[0])][int(tmp[1])]=255

print(test)