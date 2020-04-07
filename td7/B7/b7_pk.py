A={}
j=0
caractere=''
maxi=0
for i in input():
    if i in A:
        if A[i][1]<j-A[i][0]:
            A[i]=(A[i][0],j-A[i][0])
        if maxi<A[i][1]:
            maxi=A[i][1]
            caractere=i
        A[i]=(j,A[i][1])
    else:
        A[i]=(j,0)
    j+=1
print(caractere,maxi-1)
