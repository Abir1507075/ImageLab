import cv2
import matplotlib.pyplot as plt


img = cv2.imread('hist.jpg', cv2.IMREAD_GRAYSCALE)
res=img.copy()
cv2.imshow('input image',img)
print(img.shape)
plt.hist(img.ravel(),256,[0,255])
plt.show()

frequency=[]
probablity=[]
s=[]
for i in range(0,256):
    frequency.append(0)
    probablity.append(0)
    s.append(0)

for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        frequency[img[i][j]]+=1

total_pixel=img.shape[0]*img.shape[1]


for i in range(0,256):
        probablity[i]=frequency[i]/total_pixel

for i in range(1,256):
    probablity[i]=probablity[i]+probablity[i-1]
    
for i in range(0,256):
    s[i]=255*probablity[i]
    s[i]=round(s[i])
    
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        res[i][j]=s[res[i][j]]
        

cv2.imshow('out',res)
plt.hist(res.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()