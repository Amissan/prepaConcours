import time
start=time.time()
N,R,P=map(int,input().split())
entiers=list(map(int,input().split()))

#LOOP FOR COMPOSANTES TAB AND FOR CUMULATIVE TAB
C=[]
val=1

S=[]
res=1
S.append(1)

for item in entiers:
    if item==0:
        val+=1
        C.append(0)
        res=1
        S.append(1)
    else:
        C.append(val)
        res=(res*item)%P
        S.append(res)
##############################

#LOOP FOR RESULT PRINTING
for i in range(R):
    a,b=map(int,input().split())
    if C[a]==0 or C[a]!=C[b]:
        print(0)
        continue
    print ( (S[b+1]*pow(S[a],P-2,P) ) %P)
##########################

end=time.time()

print(end-start, " secondes")
