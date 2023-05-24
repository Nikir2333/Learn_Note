# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:08:58 2023

@author: Administrator
"""
#Monte Carlo Modle#
from time import time
from math import exp,sqrt
from random import gauss,seed

seed(20000)
t0=time()
K=100.0
T=1.0
r=0.05
sigma=0.2
M=50
dt=T/M
I=250000

S=[]
for i in range(I):
    path=[]
    for t in range(M+1):
        if t==0:
            path.append(50)
        else:
            z=gauss(0.0,1.0)
            St=path[t-1]*exp((r-0.5*sigma**2)*dt+sigma*sqrt(dt)*z)
            path.append(St)
    S.append(path)        
                        
C0=exp(-r*T)*sum([max(path[-1]-K,0)for path in S])/I
tpy=time()-t0

print (C0)
print (tpy)