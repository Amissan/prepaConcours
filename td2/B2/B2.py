N= int(input())

def gagnant(n):

    if n==0:
        return False
    else:
        return not (gagnant((n-1)//2) and gagnant((n-1)//3) and gagnant((n-1)//7))

        
def main():
    resultat=gagnant(N)

    print("First player" if resultat else "Second player")

main()