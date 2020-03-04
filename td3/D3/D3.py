Mot1=input()
Mot2=input()

def buildMatrice(chaine1, chaine2):
    N=len(chaine1)
    M=len(chaine2)
    Matrice=[]

    Matrice.append([" "]+[" "]+ [chaine2[i] for i in range(M)])
    Matrice.append([" "]+[3*i for i in range (M+1) ])

    for i in range (N):
        Matrice.append([chaine1[i]]+[3*(i+1)]+[0 for k in range(2,M+2)] )

    return Matrice

'''
def buildMatriceCout(Matrice):
    Cout=[]
    Cout.append(Matrice[0])
    for i in range(2, len(Matrice)):
        Cout.append([Matrice[i][0]]+[2*int(not Matrice[i][0]==Matrice[0][j]) for j in range(len(Matrice[0]))])
    return Cout
'''

def editDistance(chaine1, chaine2):
    Matrice=buildMatrice(chaine1,chaine2)
    #Cout=buildMatriceCout(Matrice)
    lenLigneMatrice=len(Matrice)
    lenColMatrice=len(Matrice[0])
    #print(*Matrice,sep="\n")
    #print(Matrice)
    for i in range(2, lenLigneMatrice):
        for j in range(2, lenColMatrice):
            Matrice[i][j]=min(Matrice[i-1][j]+3, Matrice[i][j-1]+3, Matrice[i-1][j-1]+2*int(not Matrice[i][0]==Matrice[0][j]))#Cout[i-1][j-1])
    
    print(Matrice[lenLigneMatrice-1][lenColMatrice-1])

def main():
    editDistance(Mot1,Mot2)
main()