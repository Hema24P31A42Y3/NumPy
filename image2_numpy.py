import numpy as np
img=np.zeros([25,20,3])
img[:,:]=65
import matplotlib.pyplot as plt
plt.imshow(img)
img[2:3, 9:10] = 0
img[3:4, 8:11] = 0
img[4:5, 7:12] = 0
img[5:6, 6:13] =0
img[6:7, 5:14] = 0
img[7:8, 4:15] = 0
img[8:9, 3:16] = 0
img[9:10, 4:15] = 0
img[10:11, 5:14] = 0
img[11:12, 6:13] = 0
img[12:13, 7:12] = 0
img[13:14, 8:11] = 0
img[14:15, 9:10] = 0
img[14:23,8:11]=0
plt.imshow(img)
