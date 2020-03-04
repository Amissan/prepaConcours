N=int(input())
def main():
    mots=[]
    for i in range(N):
        mots.append(input())

    petit=""
    petit=mots[0]
    for i in range(1,N):

        if len(petit)==len(mots[i]):
            if petit>mots[i]:
                petit=mots[i]
        else:
            if len(petit)>len(mots[i]):
                petit=mots[i]
    print (petit)

main()