import  math
rows=[67,56,78,86,43,99,234,143]

def dct(rows):
    x=[]
    for k in range(0,8):
        s=0
        if(k==0) :
            a=math.sqrt(1/8)
        else:
            a=math.sqrt(2/8)
        for n in range(0,8):
            s+=rows[n]*math.cos((k*math.pi*(2*n+1))/16)
        x.append(a*s)
    return x

def idct(X):
    N = 8
    x = []
    for n in range(N):
        s = 0
        for k in range(N):
            if k == 0:
                a = math.sqrt(1/N)
            else:
                a = math.sqrt(2/N)
            s += a * X[k] * math.cos((math.pi * (2*n+1) * k) / 16)
        x.append(s)
    return x


ans=dct(rows)
for x in ans:
    print(x)

recovered = idct(ans)
for val in recovered:
    print(round(val, 4))

print(sum(r**2 for r in rows))
print(sum(a**2 for a in ans))