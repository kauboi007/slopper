from PIL import Image
from DCT import twoddct
from analyzers import hfr,slope,flatness,spike
from viz import visualize,visualize_residual

img=Image.open("image1.JPG").convert("L")
pixels=list(img.getdata())
width,height=img.size
matrix=[pixels[i*width:(i+1)*width]for i in range(height)]
matrix = [[matrix[i][j] - 128.0 for j in range(width)] for i in range(height)]
blocks = []
for i in range(0, height-7, 8):
    for j in range(0, width-7, 8):
        block = [matrix[i+r][j:j+8] for r in range(8)]
        blocks.append(block)
nblocks=len(blocks)
p = [[0.0] * 8 for i in range(8)]
for block in blocks:
    coeff=twoddct(block)
    for k in range(8):
        for l in range(8):
            p[k][l]+=coeff[k][l]**2
for k in range(8):
        for l in range(8):
            p[k][l]/=nblocks

print(f"hfr value:{hfr(p)}")
print(f"flatness:{flatness(p)}")
print(f"spike score:{spike(p)}")
alpha, intercept = slope(p)
print(f"slope value:{alpha}")
visualize_residual(p, alpha, intercept)