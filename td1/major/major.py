N,M=map(int, input().split())
coefs=list(map(int, input().split()))
max=0
premier=""
count=0
for i in range(N):
    student = input().split()
    name = student[0]
    marks = list(map(int,student[1:]))
    moyenne=0
    for j in range(M):
        moyenne+= marks[j]*coefs[j]
    if max<moyenne:
        count=0
        max=moyenne
        premier=name
    else:
        if max==moyenne:
            count+=1

if(count>0):
    premier="EX AEQUO"

print(premier)