from fractions import Fraction

def calcul(expr):
    pile=[]
    val1=0.0
    val2=0.0
    for e in expr:
        if e!="+" and e!="-" and e!="*" and e!="/":
            pile.append(Fraction(e))
        else:
            try:
                val1=pile.pop()
                val2=pile.pop()
            except:
                return "false"

            if(e=="/"):
                if(Fraction (val1)==0):
                    return "false"
                else:
                    pile.append(Fraction(val2/val1))
            else:
                if(e=="+"):
                    pile.append(Fraction(val2+val1))
                if(e=="-"):
                    pile.append(Fraction(val2-val1))
                if(e=="*"):
                    pile.append(Fraction(val2*val1))
    res=pile.pop()
    
    try:
        err=pile.pop()
        return "false"
    except:
        return Fraction(res)
    
expression1=input().split()
expression2=input().split()

print(calcul(expression1)==calcul(expression2))