#import time
M,N=map(int,input().split())
terres=[list(input())for i in range(N)]

def nombre():
    liste=[]
    #diez=0
    #boolean=False
    for i in range(N):
        for j in range(M):
            if terres[i][j]=='#':
                #diez+=1
                #liste.append((i,j))
                terres[i][j]=0
                if(0<=i-1<N and 0<=j-1<M ):
                    if terres[i-1][j-1]!='#':
                        terres[i-1][j-1]=0

                if 0<=i-1<N and 0<=j<M:
                    if terres[i-1][j]!='#':    
                        terres[i-1][j]=0

                if 0<=i-1<N and 0<=j+1<M:
                    if terres[i-1][j+1]!='#':
                        terres[i-1][j+1]=0

                if 0<=i<N and 0<=j-1<M:
                    if terres[i][j-1]!='#':
                        terres[i][j-1]=0

                if 0<=i<N and 0<=j+1<M:
                    if terres[i][j+1]!='#':
                        terres[i][j+1]=0

                if 0<=i+1<N and 0<=j-1<M:
                    if terres[i+1][j-1]!='#':
                        terres[i+1][j-1]=0

                if 0<=i+1<N and 0<=j<M:
                    if terres[i+1][j]!='#':
                        terres[i+1][j]=0

                if 0<=i+1<N and 0<=j+1<M:
                    if terres[i+1][j+1]!='#':
                        terres[i+1][j+1]=0

    composantes=list()
    LENGHT_composantes=0

    for i in range(N):
        for j in range(M):
            if terres[i][j]==0:
                continue
            else:
                composante=list()
                composante.append((i,j))
                if 0<=i-1<N and 0<=j<M:
                    if terres[i-1][j]=='.':    
                        composante.append((i-1,j))
                if 0<=i<N and 0<=j-1<M:
                    if terres[i][j-1]=='.':
                        composante.append((i,j-1))
                if 0<=i<N and 0<=j+1<M:
                    if terres[i][j+1]=='.':
                        composante.append((i,j+1))
                if 0<=i+1<N and 0<=j<M:
                    if terres[i+1][j]=='.':
                        composante.append((i+1,j))
                
                if LENGHT_composantes==0:
                    composantes.append(composante)
                    LENGHT_composantes+=1
                else:
                    commun=False
                    for el in composante:
                        for z in range(LENGHT_composantes):
                            if el in set(composantes[z]):
                                composantes[z]=composantes[z]+composante
                                commun=True
                    if commun==False:
                        composantes.append(composante)
                        LENGHT_composantes+=1

    print (LENGHT_composantes)
   
def main():
    #nombre()
    nombre()
main()