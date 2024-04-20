# Importing numpy
import numpy as np
# Importing pyplot from matplotlib library
import matplotlib.pyplot as plt

# Number of elements = 3
n = int(3)

# Below line read inputs from user using map() function
list1 = list(map(int, 
	input("\nEnter the numbers of the first vector : ").strip().split()))[:n]
# Below line read inputs from user using map() function
list2 = list(map(int, 
	input("\nEnter the numbers of the second vector : ").strip().split()))[:n]


u = np.array(list1)   # vector u
v = np.array(list2)   # vector v
  

# Making 3d projection 
fig = plt.figure()
ax = plt.axes(projection = "3d")

# Generating Vectors with addition on 3d projection with parameters
start = [0,0,0]
ax.quiver(start[0],start[1],start[2],u[0],u[1],u[2],color='red')
ax.quiver(start[0],start[1],start[2],v[0],v[1],v[2])
ax.quiver(v[0],v[1],v[2],u[0],u[1],u[2],color="green")
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])


#Showing plot
plt.show()