
#usd vectoer way is more faster than the old one#

import math
from numpy import * #mean import all#
from time import time

random.seed(20000) #usd way is interesting#
t0=time()#count this program time taken#

S0=100.0;K=105.0;T=1.0;r=0.05;sigma=0.2
M=50;dt=T/M;I=25000

S=S0*exp(cumsum((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*random.standard_normal((M+1,I)),axis=0))

S[0]=S0

C0=math.exp(-r*T)*sum(maximum(S[-1]-K,0))/I

tnp2=time()-t0

print(C0)
print(tnp2)

"""
import random 

def randomness():
    num=random.randint(1,100)
    print(num)
    
def random_seed(seed=1):
    random.seed(seed)
    num=random.randint(1, 100)
    print(num)

#more faster way#
"""

"""
np.random.seed(2000)
t0=time()

S0=100.0;K=105.0;T=1.0;r=0.05;sigma=0.2
M=50;dt=T/M;I=25000

S=np.zeros((M+1),I)
S[0]=50

for t in range(1,M+1):
    z=np.random.standard_normal(I)
    S[t]=S[t-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*z)
    
C0=math.exp(-r*T)*sum(maximum(S[-1]-K,0))/I

tnp2=time()-t0

print(C0)
print(tnp2)
"""
    