import sys
hG="\u250C"
hD="\u2510"
bG="\u2514"
bD="\u2518"
fract=[[hG,hD,"\n"],[bG,bD,"\n"]]
N=int(input())
for i in range(1,N):
    H=[[],[]]
    B=[]
    for tab in fract:
        indice=fract.index(tab)

        for element in tab:
            if element=="\n":
                H[indice].append(element)
                B.append(element)
                for i in B:
                    H[indice].append(i)
                B=[]

            if element==hG:
                H[indice].append(hG)
                H[indice].append(hD)
                B.append(bG)
                B.append(element)
            if element==hD:
                H[indice].append(hG)
                H[indice].append(hD)
                B.append(element)
                B.append(bD)
            if element==bG:
                H[indice].append(hG)
                H[indice].append(element)
                B.append(bG)
                B.append(bD)
            if element==bD:
                H[indice].append(element)
                H[indice].append(hD)
                B.append(bG)
                B.append(bD)
    
    #fract=[H[0].copy(),H[1].copy()]
    fract=H.copy()

for element in fract:
    for j in element:
        sys.stdout.buffer.write(j.encode('utf-8'))