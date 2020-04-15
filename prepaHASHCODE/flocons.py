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
i=1
j=3
tmp=j
print("."*((N-1)//2)+"*"*(1)+"."*((N-1)//2))
while i<N-1:
    print("."*((N-j)//2)+"*"*(j)+"."*((N-j)//2))
    if tmp>=N:
        j=j-2
    else:
        j=j+2
    tmp=tmp+2
    i+=1
print("."*((N-1)//2)+"*"*(1)+"."*((N-1)//2))
