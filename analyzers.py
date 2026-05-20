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
    n=0
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
            n+=1
    a=(n*sumxy-sumx*sumy)/(n*sumx2-(sumx)**2)
    intercept = (sumy - a*sumx) / n
    return a,intercept

def flatness(p):
    n=0
    logsum=0
    ah=0
    for i in range(8):
        for j in range(8):
            if(i==0 and j==0):
                continue
            if(i>=4 or j>=4):
                logsum+=math.log(p[i][j])
                ah+=p[i][j]
                n+=1
    gm=math.e**(logsum/n)
    am=ah/n
    return gm/am 

def autocorr(x):
    n=len(x)
    r0=sum(x[i]**2 for i in range(n))
    res=[]
    for d in range(1,n):
        s=0
        for i in range(n-d):
            s+=x[i]*x[i+d]
        res.append(s/r0)
    return res

def spike(p):
    h = []
    for l in range(8):
        s = 0
        for k in range(8):
            s += p[k][l]
        h.append(s)
    v = []
    for k in range(8):
        s = 0
        for l in range(8):
            s += p[k][l]
        v.append(s)
    h=h[1:]
    v=v[1:]
    score = max(max(autocorr(h)), max(autocorr(v)))
    return score