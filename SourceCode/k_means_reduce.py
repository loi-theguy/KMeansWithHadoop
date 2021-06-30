#!/usr/bin/env python3
import sys
#cong 2 vector voi nhau
def add_vector(x,y):
    for i in range(len(x)):
        x[i]+=y[i]
#qua trinh reduce
def reduce():
    imgs={}
    for line in sys.stdin:
        line=line.rstrip('\n')
        values=line.split(',')
        key=values[0]
        img=[]
        for i in range(1,len(values)):
            img.append(float(values[i]))
        try:
            add_vector(imgs[key],img)
        except:
            imgs[key]=img.copy()
    for key in imgs.keys():
        line=''
        line+=key
        for value in imgs[key]:
            line+=','+str(value)
        print(line)
    
reduce()
