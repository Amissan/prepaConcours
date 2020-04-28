from math import sqrt as sqrt
import time
n = int(input(), 16)

def heron(nombre):
    u=int(sqrt(nombre))
    while True:
        if u==0.5*(u+nombre/u):
            return u
        u=0.5*(u+nombre/u)
    return u

def inverse():
    inv=int(-0.5 + heron(1+8*n)/2) 
    
    if inv>=0:
        return inv
    else:
        return int(-0.5 - heron(1+8*n)/2)



s=inverse()
x=int(n- s*(s+1)/2)
y=s-x
print(hex(x)[2:],hex(y)[2:])

''' COMPREHENSION
n=s*(s+1)/2
2*n=s**2+s
s**2 +s -2*n=0
s**2 +s +1/4 -1/4 -2*n=0
(s+1/2)**2 -1/4 -2*n=0
(s+1/2)**2 - (1+8*n)=0
(s+1/2)**2 = (1+8*n)
s+1/2= sqrt (1+8*n)
s =-1/2 + or - sqrt(1+8*n)

def inverse():
    inv= int(-1/2 + sqrt(1+8*n))
    if inv>=0:
        return inv
    return int(-1/2 -sqrt(1+8*n))




n=1/2(s**2+s)
n= 1/2(s**2+s+1/4-1/4)
n=1/2((s+1/2)**2-1/4)
2*n=(s+1/2)**2 -1/4
2*n + 1/4= (s+1/2)**2
2*n=-1/4 + or - sqrt(s+1/2)
n=1/2(-1/4 + or - sqrt(s+1/2))


def inversebis():
    inv= int(( -1/4 + sqrt(n+1/2) )//2)
    if inv>=0:
        return inv
    return int(( -1/4 - sqrt(n+1/2) )//2)



RIGHT!!
n=s*(s+1)/2
2*n=s**2+s
s**2 +s -2*n=0

delta=1-4*(-2*n)
delta=1+8*n

s=(-1 + or - sqrt(1+8*n))/2

x**2 +x -2*10= x**2+x+1/4-1/4-20=(x+1/2)**2-1/4-20

'''