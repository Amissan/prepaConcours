import time
N,R,P=map(int,input().split())
entiers=list(map(int,input().split()))
requetes=[]
for i in range(R):
    a,b=map(int,input().split())
    requetes.append([a,b])

def C4(N,R,P,entiers,requetes):
    if P!=0:

        res=1
        '''
        somme=0
        for i in range(N):
            somme+=entiers[i]
            entiers[i]=somme
        #print(entiers)
        
        #print(requetes)

        for item in requetes:
            somme=0
            #print(item)
            #somme=somme+entiers[item[0]]
            if item[0]==0:
                somme=entiers[item[0]]
                for j in range(item[0]+1,item[1]+1):
                    somme+=entiers[j]-entiers[j-1]
                print(somme%P)
            else:
                for j in range(item[0],item[1]+1):
                    somme+=entiers[j]-entiers[j-1]
                print(somme%P)
        '''
        for i in range(N):
            if entiers[i]==0:
                res=1
                entiers[i]=0
            else:
                res*=entiers[i]
                entiers[i]=res
        entiers.insert(0,0)

        print(entiers)


        for item in requetes:
            #res=
            for iteme in entiers[item[0]:item[1]+1]:
                if iteme==0:
                    res=0
                    break
                res*=iteme   
            print(pow(res,1,P))


        '''

        for item in requetes:
            res=1
            for iteme in entiers[item[0]:item[1]+1]:
                if iteme==0:
                    res=0
                    break
                res*=iteme   
            print(pow(res,1,P))
    else:
        for item in requetes:
            res=1
            print(set(entiers[item[0]:item[1]+1]))
            for iteme in entiers[item[0]:item[1]+1]:
                if iteme==0:
                    res=0
                    break
                res*=iteme
                #res*=pow(iteme,1,P)   
            print(res)
    '''

    return 0

def main():
    C4(N,R,P,entiers,requetes)

    #print(pow(2,5-2,))
    #print(pow(10,-1,12))

start=time.time()
main()
end=time.time()

print(end-start," seconds")