L=list(map(int, input().split()))
pente=1
s=L[0]-L[1]
for i in range(1, len(L)-1):
    if s>0:
        if L[i]<L[i+1]:
            pente+=1
            s=L[i]-L[i+1]
    else:
        if s==0:
            s=L[i]-L[i+1]
        else:
            if L[i]>L[i+1]:
                pente+=1
                s=L[i]-L[i+1]

print(pente)