import operator as Operator
from functools import reduce
#start=time.time()
S,K=map(int,input().split())
entiers=list(map(int,input().split()))



def factorielle(entier):
    res=1

    while entier>1:
        res=res*entier
        entier-=1
    return res

def combinaison(n, p):
    p = min(p, n-p)
    numerator = reduce(Operator.mul, range(n, n-p, -1), 1)
    denominator = reduce(Operator.mul, range(1, p+1), 1)
    return numerator // denominator

'''
def combinaison(n,p):
    res=1
    for i in range(n-p+1, n+1):
        res*=i
    return res//factorielle(p)
'''

P=S-sum(entiers)
if P<0:
    print(0)
    exit( 0)

N=P+K-1

print(combinaison(N,P))

#end=time.time()
#print(end-start," seconds")