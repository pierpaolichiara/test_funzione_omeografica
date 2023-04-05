#progetto per calcolare e plottare autovalori e autostati di un elettrone in una buca di potenziale infinita e larga L
#import
import numpy as np
import matplotlib.pyplot as plt 
import scipy as sp


#parameters electron_mass, hbar, elementary_charge
#hbar = constants.hbar
hbar=1  #6.58*10**(-16) #eV s
m = 1 #constants.m_e
#pi = constants.pi
pi=3,14

#input n, L
print('This programme gives the first n eigenfunctions and eigenvalues of an electron in a infinite potential well with a width L.') 
width =float(input('Please, insert the width of the potential well in Angstrom: L = '))           
n=int(input('Please, insert the number of the first eigenvalues and eigenstates of the electron you want to know: n = ')) 

#x?????
L=width                             #convertire unita' di misura

#definition of functions, to be put in separate files py
def eigenfunction(L,n,x):
    psi_n=np.sqrt(2/L)*np.sin(n*np.pi*x/L)
    return(psi_n)

def eigenvalues(L,n):         #definisco direttamente  E_n senza E_1?
  E_1=hbar**2*np.pi**2/(2*m*L**2)   #meglio definirla fuori dalla funzione? altrimenti a ogni n la ricalcola inutilmente
  E_n=n**2*E_1                            # 
  return(E_n)

#calculations
for level in range (1,n):
  print(level, eigenfunction(L,level), eigenvalues(L,level))
  
#plot
x_array = np.linspace(-L/2, L/2, 100)
fig, ax = plt.subplots()
for level in range (1, n+1):
    print(level, eigenvalues(L,level)/eigenvalues(L,1))
    y_array = [eigenfunction(L,level ,x) + 0.1*eigenvalues(L,level)/eigenvalues(L,1) for x in x_array]
    z_array = [eigenvalues(L,level)/eigenvalues(L,1) for x in x_array]
ax.plot(x_array, y_array)
ax.plot(x_array, z_array)
ax.vlines(x=-L/2, ymin=0, ymax=1)
fig.legend()

fig.show()

