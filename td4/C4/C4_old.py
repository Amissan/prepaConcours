#import time

N,R,P=map(int,input().split())
entiers=list(map(int,input().split()))
requetes=[]
for i in range(R):
    a,b=map(int,input().split())
    requetes.append([a,b])


def Naif(N,R,P,entiers,requetes):
    res=1
    for item in requetes:
        res=1
        for iteme in entiers[item[0]:item[1]+1]:
            res*=iteme
        print(res%P)
    return 0


def C4(N,R,P,entiers,requetes):
    res=1
    tmp=entiers.copy()
    for i in range(N):
        if entiers[i]==0:
            res=1
            entiers[i]=0
        else:
            res*=entiers[i]
            entiers[i]=res

    entiers.insert(0,1)
    print(tmp)
    print(entiers)

    for item in requetes:
        L=item[0]+1
        R=item[1]+1
        if L==R:
            print(tmp[L-1])
            continue
        if L==1:
            if entiers[L]==0:
                print(0)
                continue
            else:
                if P==0:
                    produit=entiers[R]#//entiers[1]
                if P!=0:
                    produit=(entiers[R])%P#//entiers[1])%P
            print(produit)
            continue

        #produit=1
        if entiers[L-1]==0:
            print(0)
        else:
            if P==0:
                produit=entiers[R]//entiers[L-1]
            else:
                produit=(entiers[R]//entiers[L-1])%P
            print(produit)

    return 0

def main():
    C4(N,R,P,entiers,requetes)


#start=time.time()
main()
#end=time.time()

#print(end-start," seconds")