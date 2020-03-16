N=int(input())
Couples=[]
Tab=[]
Tab.append(0)
for _ in range(N-1):
    Tab.append(0)
    a,b=map(int,input().split())
    Couples.append((a,b))
def feuilles(arbre):
    Feuilles=[]
    for a,b in arbre:
        Tab[a-1]+=1
        Tab[b-1]+=1
    for i in range(N):
        if Tab[i]<2:
            Feuilles.append(i+1)
    return Feuilles
def main():
    print(Couples)
    print(feuilles(Couples))
main()