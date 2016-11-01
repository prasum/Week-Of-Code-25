#!/bin/python

import sys



n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))
a.sort()
b.sort()
i=len(a)-1
j=0
p=0
q=0
k=a[i]

while k<=b[0]:
    for p in xrange(len(a)):
        if(k%a[p]==0):
            if(p==len(a)-1):
                for q in xrange(len(b)):
                    if(b[q]%k==0):
                        
                        if(q==len(b)-1):
                            
                            #print k
                            j=j+1
                    else:
                        break
        else:
            break
    k=k+1
    p=0
    q=0
    
print j