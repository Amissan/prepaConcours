N=int(input())
Couples=[]

for _ in range(N):
    a,b=map(int,input().split())
    Couples.append((a,b))

Sx=0
Sy=0

for i in range(N):

    if i==N-1:
        Sx+=Couples[0][1]*Couples[i][0]
        Sy+=Couples[0][0]*Couples[i][1]
    else:
        Sy+=Couples[i][1]*Couples[i+1][0]
        Sx+=Couples[i][0]*Couples[i+1][1]


print(abs(Sx-Sy))


'''
print(N)
print(*Couples,sep="\n")
'''