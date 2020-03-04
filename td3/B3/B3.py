#import time

H,W=(map(int,input().split()))
LeMot=input()
def main():
    #global start
    #global end
    Liste=[]
    ListeCol=[]
    longeurMot=len(LeMot)
    nbre=0
    for i in range(H):
        Liste.append(input())
    

    for i in range(W):
        Colonne=""
        for element in Liste:
            Colonne+=element[i]
        ListeCol.append(Colonne)

    for element in Liste:
        for i in range(W-longeurMot+1):
            if element[i:i+longeurMot]==LeMot:
                nbre+=1
            #tmp=element[::-1]
            if element[::-1][i:i+longeurMot]==LeMot :
                nbre+=1

    for element in ListeCol:
        for i in range(H-longeurMot+1):
            if element[i:i+longeurMot]==LeMot:
                nbre+=1
            #tmp=''.join(reversed(element))
            #tmp=element[::-1]
            if element[::-1][i:i+longeurMot]==LeMot :
                nbre+=1
    

    print(nbre)


#start=time.time()

main()

#end=time.time()

#print("function takes", end-start, "seconds")