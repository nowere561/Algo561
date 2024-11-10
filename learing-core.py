import matplotlib.pyplot as plt
import numpy as np

k=int(input("enter the value of K:"))
xc=[]
yc=[]
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta']


for i in range (0,k):
    xc.append(np.random.rand(1) *10)
    yc.append(np.random.rand(1) *10)
   


x=[7.140484932845048, 0.7621359749281376, 0.01964966931324419, 3.283625760370027, 9.883486603985657, 9.80455308506285, 5.157681228979467, 2.2021100868452015, 6.128964446656654, 1.6152275206280153]
y=[9.9771326116337846, 5.866867440927098, 2.216373083540699, 5.282882945169403, 0.3989111558089853, 7.962315116320976, 6.019854320309622, 1.2225895206942494, 0.700240649037791, 4.13513252653905]
# x = [1, 3, 5, 1, 3, 5]  
# y = [1, 1, 1, 2, 2, 2] 
plt.figure(figsize=(10, 10))




for i in range(0,len(x)):
    distances=[]
    for c in range(0,k):
        distances.append(np.sqrt((xc[c] - x[i])**2 + (yc[c] - y[i])**2))


    min_index = distances.index(min(distances))
  

    plt.scatter(x[i],y[i],color=colors[min_index])
 
for c in range(0,k):
    plt.scatter(xc[c],yc[c],s=100, color=colors[c])




plt.grid(True)
plt.show()





     




      



    




    







