#import time

H,W=list(map(int, input().split()))
#grille=[(input().split()) for i in range(H)]
grille=[list(input())for i in range(H)]
#grilleBord=[]


def create_copy():
    grilleBord=[]
    grilleBord.append([0 for i in range(W+2)])
    for element in grille:
        grilleBord.append( [0]+element+[0])

    grilleBord.append([ 0 for i in range(W+2)])
    return grilleBord


def main():
    copy=create_copy()
    max=0
    for i in range(len(copy)-2,0,-1):
        for j in range(1,W+2):
            if copy[i][j]==0:
                continue

            if copy[i][j]=='#':
                copy[i][j]=0

            if copy[i][j]=='.':
                copy[i][j]=min(copy[i+1][j-1],copy[i+1][j],copy[i+1][j+1])+1
                
                if copy[i][j]>max:
                    max=copy[i][j]
    print(max)

#start=time.time()
main()
#end=time.time()

#print("My main take: ",end-start," seconds")

