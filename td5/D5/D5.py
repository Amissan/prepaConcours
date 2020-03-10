N=int(input())
Couples=[]

x,y=map(int,input().split())

Pivot=(x,y)

#RECHERCHE DU PIVOT

for _ in range(1,N):
    a,b=map(int,input().split())
    if b<Pivot[1]:
        Pivot=(a,b)
    if b==Pivot[1]:
        Pivot=(min(x,a),b)

    Couples.append((a,b))

Tab=[]
Tab.append(Pivot)


#TRI DES POINTS
for  a,b in Couples:
    

for