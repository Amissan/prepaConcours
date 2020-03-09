N=int(input())
etudiants=[]
for _ in range(N):
    a,b=map(float,input().split())
    etudiants.append([b,a,_+1])

etudiants.sort(reverse=True)


if etudiants[0][1]!=1:
    print(etudiants[0][2])
    exit(0)

rangs=set()
rangs.add(etudiants[0][1])

menteur=0
tempp=etudiants[0]
for i in range(1,N):
    if etudiants[i][1]<tempp[1]:
        if etudiants[i][1] in rangs or etudiants[i][0]==tempp[0]:
            menteur=etudiants[i][2]
        else:
            menteur=tempp[2]
    else:
        rangs.add(etudiants[i][1])
        tempp=etudiants[i]

print(menteur)    
