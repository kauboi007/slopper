import  math
#dct functions
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

def twoddct(block):
    intermediate=[]
    for i in range(0,8):
        intermediate.append(dct(block[i]))
    tfinal=[]
    for i in range(0,8):
        temp=[]
        for j in range(0,8):
            temp.append(intermediate[j][i])
        tfinal.append(dct(temp))

    final=[[tfinal[j][i] for j in range(8)]for i in range(8)]
    p=[]
    for k in range(8):
        temp=[]
        for l in range(8):
            temp.append(final[k][l])
        p.append(temp)
    return p