#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

'''
lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
'''	
N=int(input())
Couleurs=[input() for _ in range(N)]
nbre=0
Couleurs.sort()
Val=Couleurs[0]
tmp=1
for i in range(1,N):
    if Val==Couleurs[i]:
        tmp+=1
        if tmp==2:
            nbre+=1
            tmp=0
    else:
        Val=Couleurs[i]
        tmp=1
print(nbre)