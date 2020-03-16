N=int(input())
Couples=[]
Tab=[]
Tab.append(0)
feuilles=0
for _ in range(N-1):
    Tab.append(0)
    a,b=map(int,input().split())
    Couples.append((a,b))
for a,b in Couples:
    Tab[a-1]+=1
    Tab[b-1]+=1
for item in Tab:
    if item<2:
        feuilles+=1
print(feuilles)