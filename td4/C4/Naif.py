import time

N,R,P=map(int,input().split())
entiers=list(map(int,input().split()))
requetes=[]
for i in range(R):
    a,b=map(int,input().split())
    requetes.append([a,b])

def C4(N,R,P,entiers,requetes):
    res=1
    for item in requetes:
        res=1
        for iteme in entiers[item[0]:item[1]+1]:
            #print ("iteme: ",iteme,"\n--------")
            res*=iteme
        print(res%P)
    return 0

def main():
    #C4(N,R,P,entiers,requetes)


start=time.time()
main()
end=time.time()

print(end-start," seconds")