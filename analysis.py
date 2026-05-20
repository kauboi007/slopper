import math
def hfr(p):
    lsum=0
    sum=0
    for k in range(8):
        for l in range(8):
            if(k==0 and l==0):
                continue
            sum+=p[k][l]
            if(k<4 and l<4):
                lsum+=p[k][l]
    highsum=sum-lsum
    return highsum/sum

def slope(p):
    sumxy=0
    sumx=0
    sumy=0
    sumx2=0
    for k in range(8):
        for l in range(8):
            if(k==0 and l==0):
                continue
            f=math.sqrt(k**2+l**2)
            e=p[k][l]
            fl=math.log(f)
            el=math.log(e)
            sumx+=fl
            sumy+=el
            sumxy+=fl*el
            sumx2+=fl**2
    #pearson coerr : α = (N·Σ(xy) - Σx·Σy) / (N·Σ(x²) - (Σx)²)
    a=(63*sumxy-sumx*sumy)/(63*sumx2-(sumx)**2)
    return a
