import math
import cv2
import numpy as np


img = cv2.imread("tall.jpg",0)
cv2.imwrite("in.jpg",img)
res=img.copy()


pi=2*math.pi
Tx=int(input("Enter value of Tx: "))
Ty=int(input("Enter value of Ty: "))
Ax=int(input("Enter value of Ax: "))
Ay=int(input("Enter value of Ay: "))

def cal(x,y):
    a=x+Ax*math.sin((pi*y)/Tx)
    b=y+Ay*math.sin((pi*x)/Ty)
    return int(a),int(b)

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        a,b=cal(i,j)
        if(a<0 or b<0  or a>=img.shape[0] or b>=img.shape[1]):
            res[i][j]=0
        else :
            res[i][j]=img[a][b]


cv2.imwrite("out.jpg",res)
cv2.waitKey(0)
cv2.destroyAllWindows()