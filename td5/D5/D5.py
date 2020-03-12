from math import sqrt as sqrt
N=int(input())
Pousses=[]

for _ in range(N):
    a,b=map(int,input().split())
    Pousses.append((a,b))

def distance(A,B):
    return sqrt( pow ( A[0]-B[0] , 2 ) + pow ( A[1]-B[1] , 2 ) )

def perimeter(C_hull):
    return sum([distance(C_hull[i],C_hull[i+1]) for i in range(len(C_hull)-1)])+distance(C_hull[0],C_hull[-1])

def crossProduct(O,A,B):
    return ( ( A[0]-O[0] ) * (B[1] - O[1] ) ) - ( ( A[1]-O[1] ) * ( B[0]-O[0] ) )

def convex_hull(Points):
    
    if len(Points) < 2:
        print(0)
        return 0

    Points = sorted(set(Points))

    HULL = []
    for point in reversed(Points):
        while len(HULL) > 1 and crossProduct(HULL[-2], HULL[-1], point) <= 0:
            HULL.pop()
        HULL.append(point)
    HULL.pop()

    hull = []
    for point in Points:
        while len(hull) > 1 and crossProduct(hull[-2], hull[-1], point) < 0:
            hull.pop()
        hull.append(point)
    hull.pop()

    Perimetre=perimeter(hull + HULL)

    if Perimetre-int(Perimetre)<0.5:
        print(int(Perimetre))
    else:
        print(int(Perimetre)+1)

def main():

    convex_hull(Pousses)

main()