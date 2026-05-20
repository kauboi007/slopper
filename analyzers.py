import math
#all the anal - hfr,flatness,slope,spikes
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

def finalscore(p):
    h = hfr(p)
    a, intercept = slope(p)
    f = flatness(p)
    sp = spike(p)

    slopescore = max(0, min(1, (a - (-2.0)) / (-5.0 - (-2.0))))   # real= < -3.5, AI= > -2.0
    hfrscore = max(0, min(1, 1 - (h / 0.3)))                      # real= low, AI= high
    flatscore = max(0, min(1, 1 - (f / 0.8)))                     
    spikescore = max(0, min(1, 1 - (sp / 0.6)))                    

    score = (slopescore*0.25+hfrscore*0.20 +flatscore*0.35+spikescore*0.20)*100
    return round(score, 1)
