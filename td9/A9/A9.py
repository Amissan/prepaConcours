V,E=list(map(int,input().split()))
Voisins=[]
Numeros=[]
Ancetres=[]
Valeurs=[]
pile=[]
ponts=0
R=[]
for _ in range(V):
    Voisins.append([])
    Valeurs.append(None) 
    Numeros.append(None)
    Ancetres.append(None)
for _ in range(E):
    a,b=list(map(int,input().split()))
    Voisins[a-1].append(b)
    Voisins[b-1].append(a)

def algo(Pile):
    global ponts
    K=Pile.pop()
    minV=Numeros[K-1]
    for i in Voisins[K-1]:
        if i==Ancetres[K-1]:
            continue
        if Valeurs[i-1]==None:
            minV=min(Numeros[i-1],minV)
        else:
            minV=min(Valeurs[i-1],minV)
    Valeurs[K-1]=minV
    if Ancetres[K-1]!=None and Valeurs[K-1]==Numeros[K-1]:
        R.append( sorted((K,Ancetres[K-1])) )
        ponts+=1

def dfs():
    pile.append(1)
    Numeros[0]=1
    j=1
    A=1
    while j!=V:
        T=True
        while T:
            T=False
            for i in Voisins[A-1]:
                if Numeros[i-1]==None:
                    j+=1
                    pile.append(i)
                    Numeros[i-1]=j
                    Ancetres[i-1]=A
                    A=i
                    T=True
                    break
                T=False
        if pile:
            if j==V:
                while pile:
                    A=Ancetres[A-1]
                    algo(pile)
                print(ponts)
                for i in sorted(R):
                    print(*i)
                exit(0)
            else:
                A=Ancetres[A-1]
                algo(pile)
        if not pile:
            for x in range(V):
                if Numeros[x]==None:
                    j+=1
                    x+=1
                    pile.append(x)
                    Numeros[x-1]=j
                    A=x
                    break
    print(ponts)
    for i in sorted(R):
        print(*i)
dfs()