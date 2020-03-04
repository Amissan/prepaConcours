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
    print(tmp)
    C=[]

    val=1
    #C.append(0)
    for _ in tmp:
        if _==0:
            val+=1
            C.append(0)
        else:
            C.append(val)

    #print(C)

    for i in range(N):
        if entiers[i]==0:
            res=1
            entiers[i]=0
        else:
            res*=entiers[i]
            entiers[i]=res%P

    entiers.insert(0,1)

    for item in requetes:
        a=item[0]+1
        b=item[1]+1

        if a==b:
            print(tmp[a-1]%P)
            continue
        
        if C[a]==0:
            print(0)
            continue

        if C[a]!=C[b]:
            print(0)
            continue
        
        if C[a]!=C[b]:
            if entiers[a-1]==0:
                print(entiers[b]%P)
            else:
                print ( (entiers[b]*pow(entiers[a-1],P-2,P) ) %P)
            continue



    return 0

def main():
    C4(N,R,P,entiers,requetes)


#start=time.time()
main()
#end=time.time()

#print(end-start," seconds")