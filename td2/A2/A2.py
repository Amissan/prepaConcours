import time
M,N=map(int,input().split())
terres=[list(input())for i in range(N)]

def nombre():
    for i in range(N):
        for j in range(M):
            if terres[i][j]=='#':
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

    count=0
    for i in range(N):
        for j in range(M):
            if terres[i][j]!='.':
                continue
            else:
                count+=1

    print (count)

    return count
 
def main():

    start=time.time()
    nombre()
    end=time.time()
    print("function takes", end-start, "seconds")
main()