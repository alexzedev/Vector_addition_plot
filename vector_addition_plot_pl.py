# Importuje NumPy
import numpy as np
# Importuje pyplot  biblioteki Matplotlib
import matplotlib.pyplot as plt

# Liczba elementów = 3
n = int(3)

# Wiersz poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map() dla pierszego wektora
list1 = list(map(int, 
	input("\nEnter the numbers of the first vector : ").strip().split()))[:n]
# Wiersz poniżej odczytuje dane wejściowe od użytkownika za pomocą funkcji map() dla drugiego wektora
list2 = list(map(int, 
	input("\nEnter the numbers of the second vector : ").strip().split()))[:n]


u = np.array(list1)   # vector u
v = np.array(list2)   # vector v
  

# Tworzy projekcję 3D 
fig = plt.figure()
ax = plt.axes(projection = "3d")

# Tworzy wektoryi dodaje je na projekcji 3D z odpowiednimi parametrami
start = [0,0,0]
ax.quiver(start[0],start[1],start[2],u[0],u[1],u[2],color='red')
ax.quiver(start[0],start[1],start[2],v[0],v[1],v[2])
ax.quiver(v[0],v[1],v[2],u[0],u[1],u[2],color="green")
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])
ax.set_zlim([-20, 20])


#Pokazuje wykres przestrzenny
plt.show()