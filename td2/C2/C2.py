#import time
N,M=map(int, input().split())
Ligne2=list(map(int,input().split()))
Ligne3=list(map(int, input().split()))

def difference():
    somme=0

    if M!=0:
        while len(Ligne2)>1:
            a=(Ligne2.pop(),Ligne2.pop())
            Ligne3.append(abs(Ligne3[a[0]]-Ligne3[a[1]]))
            Ligne3[a[0]]=0
            Ligne3[a[1]]=0
    
    for i in Ligne3:
        somme+=i

    liste=[]
    liste.append(True)
    for i in range(1, somme//2 +1):
        liste.append(False)

    for element in Ligne3:
        if element==0 or element> somme//2:
            continue
        j=somme//2
        for i in liste[::-1]:
            if  i==True:
                if(0<=j+element<=somme//2):
                    liste[j+element]=True
            j-=1

    sommePartInf=somme//2
    for i in liste[::-1]:
        if i==True:
            sommePartSup=somme-sommePartInf
            return abs(sommePartInf-sommePartSup)
        sommePartInf-=1
    
def main():
    #start=time.time()
    print(difference())
    #end=time.time()
    #print("function takes", end-start, "seconds")
main()