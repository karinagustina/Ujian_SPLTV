#Ujian_SPLTV

import numpy as np

# Diketahui persamaan LTV:
#  x - 2y +  z =  6
# 3x +  y - 2z =  4 
# 7x - 6y -  z = 10

# Mencari Nilai x, y, z
a = np.array([[1,-2,1],[3,1,-2],[7,-6,-1]])
b = np.array([6,4,10])

hasil = np.linalg.solve(a,b)
print('\n', 'Nilai x =', hasil[0], '\n', 'Nilai y =', round(hasil[1]), '\n', 'Nilai z =', hasil[2])

#Menggambar 3D Plotting
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure('SPLTV 3D Plotting')

# Menggambar Grafik Persamaan 1
# x - 2y +  z =  6
a1 = np.array([[1]])
b1 = np.array([[-2]])
c1 = np.array([[1]])
d1 = np.array([6])

x1 = np.linalg.solve(a1,d1)
y1 = np.linalg.solve(b1,d1)
z1 = np.linalg.solve(c1,d1)
# print(x1)
# print(y1)
# print(z1)

titikA1 = np.array([x1[0],0,0])
titikB1 = np.array([0,y1[0],0])
titikC1 = np.array([0,0,z1[0]])
# print(titikA1)
# print(titikB1)
# print(titikC1)

i1 = plt.subplot2grid((1,3), (0,0), projection = '3d')
i1.scatter(titikA1, titikB1, titikC1, color = 'blue')
i1.plot_trisurf(titikA1, titikB1, titikC1, color = 'red', alpha = 0.5)
i1.set_xlabel('Nilai X')
i1.set_ylabel('Nilai Y')
i1.set_zlabel('Nilai Z')
i1.text(-3, -1, 7, 'x - 2y +  z =  6', color = 'black') 

# Menggambar Grafik Persamaan 2
# 3x +  y - 2z =  4 
a2 = np.array([[3]])
b2 = np.array([[1]])
c2 = np.array([[-2]])
d2 = np.array([4])

x2 = np.linalg.solve(a2,d2)
y2 = np.linalg.solve(b2,d2)
z2 = np.linalg.solve(c2,d2)
# print(x2)
# print(y2)
# print(z2)

titikA2 = np.array([x2[0],0,0])
titikB2 = np.array([0,y2[0],0])
titikC2 = np.array([0,0,z2[0]])
# print(titikA2)
# print(titikB2)
# print(titikC2)

i2 = plt.subplot2grid((1,3), (0,1), projection = '3d')
i2.scatter(titikA2, titikB2, titikC2, color = 'red')
i2.plot_trisurf(titikA2, titikB2, titikC2, color = 'yellow', alpha = 0.5)
i2.set_xlabel('Nilai X')
i2.set_ylabel('Nilai Y')
i2.set_zlabel('Nilai Z') 
i2.text(0, 0, 1.1, '3x +  y - 2z =  4', color = 'black') 

# Menggambar Grafik Persamaan 3
# 7x - 6y -  z = 10
a3 = np.array([[7]])
b3 = np.array([[-6]])
c3 = np.array([[-1]])
d3 = np.array([10])

x3 = np.linalg.solve(a3,d3)
y3 = np.linalg.solve(b3,d3)
z3 = np.linalg.solve(c3,d3)
# print(x3)
# print(y3)
# print(z3)

titikA3 = np.array([x3[0],0,0])
titikB3 = np.array([0,y3[0],0])
titikC3 = np.array([0,0,z3[0]])
# print(titikA3)
# print(titikB3)
# print(titikC3)

i3 = plt.subplot2grid((1,3), (0,2), projection = '3d')
i3.scatter(titikA3, titikB3, titikC3, color = 'green')
i3.plot_trisurf(titikA3, titikB3, titikC3, color = 'blue', alpha = 0.5) 
i3.set_xlabel('Nilai X')
i3.set_ylabel('Nilai Y')
i3.set_zlabel('Nilai Z')
i3.text(-1, 0, .1, '7x - 6y -  z = 10', color = 'black') 

plt.show()