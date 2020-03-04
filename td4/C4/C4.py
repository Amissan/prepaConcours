import time

N,R,P=map(int,input().split())
entiers=list(map(int,input().split()))
requetes=[]
for i in range(R):
    a,b=map(int,input().split())
    #requetes.append([a,b])


'''
def Naif(N,R,P,entiers,requetes):
    res=1
    for item in requetes:
        res=1
        for iteme in entiers[item[0]:item[1]+1]:
            res*=iteme
        print(res%P)
    return 0
'''

def C4(N,R,P,entiers,requetes):
    res=1
    S=[]
    C=[]
    val=1
    for _ in entiers:
        #print(_)
        if _==0:
            val+=1
            C.append(0)
        else:
            C.append(val)


    S.append(1)
    for i in range(N):
        if entiers[i]==0:
            res=1
            S.append(1)
        else:
            res*=entiers[i]
            S.append(res%P)
    
    #print(entiers)
    #print(S)
    #print(C)

    '''
    for i in range(N):
        if entiers[i]==0:
            res=1
            entiers[i]=1
        else:
            res*=entiers[i]
            entiers[i]=res%P
    '''


    #entiers.insert(0,1)

    for a,b in requetes:
        #a=item[0]+1
        #b=item[1]+1
        
        #a=a+1
        #b=b+1

        if C[a]==0 or C[a]!=C[b]:
        #if C[a-1]!=C[b-1]:
            print(0)
            continue
        
        '''
        if entiers[a]==0:
        #if entiers[a-1]==0:
            print(entiers[b+1]%P)
            #print(entiers[b]%P)
        else:
        '''
        print ( (S[b+1]*pow(S[a],P-2,P) ) %P)

        #print ( (entiers[b+1]*pow(entiers[a],P-2,P) ) %P)
        #print ( (entiers[b]*pow(entiers[a-1],P-2,P) ) %P)
    return 0

def main():
    C4(N,R,P,entiers,requetes)

start=time.time()
main()
end=time.time()

print(end-start," seconds")