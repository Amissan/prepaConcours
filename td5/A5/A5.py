N=int(input())
Couples=[]

TabX=[]
TabY=[]

x,y=map(int,input().split())

Xmin=x
Xmax=x

Ymin=y
Ymax=y

Couples.append((x,y))

TabX.append(x)
TabY.append(y)

for _ in range(1,N):
    a,b=map(int,input().split())
    if a<Xmin:
        Xmin=a
    if a>Xmax:
        Xmax=a
    if b<Ymin:
        Ymin=b
    if b>Ymax:
        Ymax=b
print(Xmax-Xmin,Ymax-Ymin)