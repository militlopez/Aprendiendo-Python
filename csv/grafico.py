# importa una parte de la librería para que cargue más rápido
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[1,4,2,3]

plt.plot(x,y)
plt.xlabel( 'Titulo sobre el X' ) 
plt.ylabel( 'Titulo sobre el Y' ) 
plt.title( 'Gráfico de línea básico' ) 
plt.show()