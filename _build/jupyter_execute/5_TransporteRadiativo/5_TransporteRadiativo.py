#!/usr/bin/env python
# coding: utf-8

#  <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # 5. Transporte Radiativo
# <br><br><br><br>
# Profesor: Francisco Ramírez Cuevas<br>
# Fecha: 9 de Septiembre 2022

# ## Coherencia de la luz e interferencia
# Como veremos en las próximas clases, las vibraciones moleculares en la materia son las responsables de emitir radiación en forma de ondas electromagnéticas. El mecanismo es similar, pero inverso, al mecanismo de absorción de luz, el cual es originado por la interacción de ondas electromagnéticas con las vibraciones moleculares (ver clase 3).

# Dicho esto, dos moléculas pueden emitir radiación con una pequeña variación en la longitud de onda $\Delta\lambda$. Esto ocurre porque las vibraciones no están 100% correlacionadas, es decir, existe un grado de aletoriedad en las vibraciones.

# Por ejemplo, consideremos una fuente de luz en el vacío que emite ondas electromagnéticas en dirección $\hat{k} = \hat{x}$. Consideremos esta fuente como $N$ emisores, donde cada emisor $j$ emite radiación con una longitud de onda $\lambda \pm\Delta \lambda_j$, donde $\Delta \lambda_j$ es escogido aleatoriamente a partir de una distribución normal.
# 
# La onda resultante está definida por:
# 
# \begin{equation*}
# \vec{E}_{tot} = \sum_j^N E_0e^{i\left(k_jx - \omega_j t\right)} \hat{z},
# \end{equation*}
# 
# donde $k_j = \frac{2\pi}{\lambda \pm\Delta \lambda_j}$, y $\omega_j = c_0k_j$

# En este ejemplo, $\lambda = 500$ nm es la longitud de onda central de la fuente. Además, definiremos una variable $\sigma \in [0,1]$ de manera que $\Delta\lambda_j = \sigma\lambda$.

# In[1]:


import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt
c0 = 3E8          # velocidad de la luz (m/s)
lam = 0.5         # longitud de onda (um)
k0 = 2*np.pi/lam  # vector de onda (rad/um)
w0 = c0*k0        # Frecuencia angular (rad/s)

def light_packet(kdir, x, t, lam, sig, N):
    xx = np.meshgrid(x,np.ones(N))[0]
    
    # Generamos arreglo de ondas aleatorias
    dlamj =  normal(0, lam*sig,N)
    kj = (2*np.pi/(lam + dlamj)).reshape(-1,1)
    wj = c0*kj
    Erand = np.exp(1j*(kdir*kj*xx-wj*t)) 
    
    # Sumamos todas las ondas
    return np.sum(Erand,axis=0)

def plot_light_packet(N, t, sig):
    '''
    n: número de ondas generadas
    t: tiempo en ns
    sig: % de ancho de banda (dlam = sig*lam)
    '''
    t = t*1E-9 # convertimos ns a s
    
    # recorrido de la onda
    x = np.linspace(-2,2,1000)  # desde 0 a 4 micrones
    E = light_packet(1, x, t, lam, sig, N)
    
    # Graficamos
    fig, ax = plt.subplots()
    fig.set_size_inches(9, 5)
    plt.rcParams['font.size'] = '18'
    
    ax.plot(x,np.real(E), 'k')
    ax.set_xlabel('x ($\mu$m)')
    ax.set_ylabel('Amplitud $|E|/E_0$')
    ax.set_ylim(-N*1.1,N*1.1)
    ax.grid()


# In[2]:


from ipywidgets import interact

@interact( N=(1,1000,1), 
           t=(-10,10,0.1),
           sig=(0,1,0.01))
def g(N=1000, t=0, sig=0.3):
    return plot_light_packet(N,t,sig)


# ### Longitud de coherencia
# Definimos como **longitud de coherencia**, $l_c$, a la distancia donde un grupo de ondas electromagnética mantiene un determinado grado de coherencia. Para longitudes mayores a $l_c$, decimos que la luz es incoherente, es decir, el desface entre las distintas ondas es completamente aleatorio.

# <img src="./images/coherence_length.png" width="300px" align= center>

# La relación entre $l_c$, la longitud de onda central $\lambda$ y el ancho de banda $\Delta\lambda$ está dado aproximadamente por la relación:
# 
# \begin{equation*}
# l_c \approx \frac{\lambda^2}{n\Delta \lambda},
# \end{equation*}
# 
# donde $n$ es el indice de refracción del medio donde se propaga la luz.
# 
# Por ejemplo, para lasers He-Ne (laser rojo)  $l_c\approx 0.2 - 100$ m.  

# Para radiación emitida por un cuerpo a temperatura $T$, la longitud de coherencia está dada por:
# 
# \begin{equation*}
# l_c T = 2167.8~\mathrm{\mu m~K}
# \end{equation*}
# 
# Así, por ejemplo, la radiación solar ($T \approx 5800~\mathrm{K}$) tiene una longitud de coherencia, $l_c \approx 370~\mathrm{nm}$

# ### Régimen de trasporte de luz
# Consideremos dos paquetes de onda con una longitud de coherencia $l_c$, viajando en sentido opuesto.

# Podemos ver que ambos paquetes de luz interfieren en $x = 0$ en un instante $t$. Al continuar su camino, ambos paquetes de onda recuperan su forma original.

# In[3]:


def plot_2light_packet(n, t, sig):
    '''
    n: número de ondas generadas
    t: tiempo en ns
    sig: % de ancho de banda (dlam = sig*lam)
    '''
    t = t*1E-9 # convertimos ns a s
    lam = 0.5
    
    # recorrido de la onda
    x = np.linspace(-2,2,1000)  # desde 0 a 4 micrones
    k0 = 2*np.pi/lam
    Efw = light_packet( 1, x - x[ 0], t, lam, sig, n)
    Ebw = light_packet(-1, x - x[-1], t, lam, sig, n)
    
    # Graficamos
    fig, ax = plt.subplots()
    fig.set_size_inches(9, 5)
    plt.rcParams['font.size'] = '18'
    
    ax.plot(x,np.real(Efw + Ebw), 'k')
    ax.set_xlabel('x ($\mu$m)')
    ax.set_ylabel('Amplitud $|E|/E_0$')
    ax.set_ylim(-n*2.1,n*2.1)
    ax.grid()


# In[4]:


from ipywidgets import interact

@interact( N=(1,1000,1), 
           t=(0,20,0.1),
           sig=(0,1,0.01))
def g(N=1000, t=2, sig=0.3):
    return plot_2light_packet(N,t,sig)


# A partir de esto, podemos concluir que los fenómenos de interferencia en películas de capa delgada de espesor $d$ no estarán presentes en si $d > l_c$. En otras palabras, el fenómeno de interferencia solo existe si el paquete de onda interfiere consigo mismo.

# <img src="./images/interference_thinfilm.png" width="200px" align= center>

# En general, para una longitud características $D$:
# 
# - Si $D > l_c$ el **transporte de luz incoherente** . En este régimen, podemos ignorar las propiedades oscilatorias de la luz, y analizar el problema como el transporte de pequeños paquetes de onda, o simplemente como partículas.
# 
# - Si $D < l_c$, el **transporte de luz coherente**. En este régimen debemos considerar las propiedades oscilatorias a partir de las Ecuaciones de Maxwell.

# Así, los coeficientes de Fresnel para una película delgada solo son válidos para $d < l_c$. 

# Los coeficientes de Fresnel para una interface, en cambio, siempre son válidos.

# <img src="./images/interference_interface.png" width="350px" align= center>

# ## Referencias
# - Rao S. S. **Chapter 4 - Vibration Under General Forcing Conditions** in *Mechanical Vibrations*, 6th Ed, Pearson, 2018
# 
# - Griffths D., **Chapter 4.1 - Polarization** in *Introduction to Electrodynamics*, 4th Ed, Pearson, 2013
# 
# - Simmons J. and Potter K., **Chapter 2 and 3** in *Optical Materials*, 1st Ed, Academic Press, 2000

# In[ ]:




