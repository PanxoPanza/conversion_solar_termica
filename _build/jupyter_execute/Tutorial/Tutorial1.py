#!/usr/bin/env python
# coding: utf-8

# **M501 - Manejo y conversión de energía solar térmica**
# # Tutorial
# 
# Este es un tutorial para utilizar las librerías de funciones para el curso. Utilizaremos dos librerías:
# - ```empylib```: Cálculos de reflectividad, transmisividad, scattering de Mie, etc.
# - ```iadpyathon```: Simulaciones de scattering multiple 
# 
# ## Instrucciones de instalación
# - La librería ```empylib``` esta disponible desde github ejecutando la siguiente sentencia en una celda de este notebook:
# ```python
# !git clone https://github.com/PanxoPanza/empylib.git
# ```
# Esto descargará una carpeta "empylib" con todos los módulos necesarios. **Ejecutar solo una vez para descar la carpeta** Posteriormente, no es necesario volver a ejecutar esta línea.
# 
# - La libería ```iadpython``` debe ser instalada desde pip, ejecutando el siguiente script en una celda de este notebook
# ```python
# import sys
# !{sys.executable} -m pip install iadpython
# ```
# Esta instancia debe ser ejecutada solo una vez.

# <h1>Contenidos<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Instrucciones-de-instalación" data-toc-modified-id="Instrucciones-de-instalación-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Instrucciones de instalación</a></span></li><li><span><a href="#Índices-de-refracción-(nklib)" data-toc-modified-id="Índices-de-refracción-(nklib)-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Índices de refracción (<code>nklib</code>)</a></span><ul class="toc-item"><li><span><a href="#Valores-tabulados" data-toc-modified-id="Valores-tabulados-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Valores tabulados</a></span></li><li><span><a href="#Modelos-de-Drude-y-Lorentz" data-toc-modified-id="Modelos-de-Drude-y-Lorentz-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Modelos de Drude y Lorentz</a></span></li></ul></li><li><span><a href="#Reflexión/Transmissión-(waveoptics)" data-toc-modified-id="Reflexión/Transmissión-(waveoptics)-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Reflexión/Transmissión (<code>waveoptics</code>)</a></span><ul class="toc-item"><li><span><a href="#Luz-incidente-en-una-interface-(interface)" data-toc-modified-id="Luz-incidente-en-una-interface-(interface)-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Luz incidente en una interface (<code>interface</code>)</a></span></li><li><span><a href="#Luz-incidente-en-arreglos-multicapas-(multilayer)" data-toc-modified-id="Luz-incidente-en-arreglos-multicapas-(multilayer)-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Luz incidente en arreglos multicapas (<code>multilayer</code>)</a></span></li><li><span><a href="#Luz-incoherente-en-arreglos-multicapas-(incoh_multilayer)" data-toc-modified-id="Luz-incoherente-en-arreglos-multicapas-(incoh_multilayer)-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Luz incoherente en arreglos multicapas (<code>incoh_multilayer</code>)</a></span></li></ul></li><li><span><a href="#Scattering-de-mie-(miescattering)" data-toc-modified-id="Scattering-de-mie-(miescattering)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Scattering de mie (<code>miescattering</code>)</a></span></li><li><span><a href="#Transporte-Radiativo" data-toc-modified-id="Transporte-Radiativo-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Transporte Radiativo</a></span><ul class="toc-item"><li><span><a href="#Beer-Lambert-(T_beer_lambert)" data-toc-modified-id="Beer-Lambert-(T_beer_lambert)-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Beer-Lambert (<code>T_beer_lambert</code>)</a></span></li><li><span><a href="#Scattering-multiple-(iadpython)" data-toc-modified-id="Scattering-multiple-(iadpython)-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Scattering multiple (<code>iadpython</code>)</a></span></li></ul></li></ul></div>

# ## Índices de refracción (```nklib```)
# ### Valores tabulados
# La librería ```empylib.nklib``` contiene una serie de funciones para determinar el coeficiente de refracción complejo, $N = n + i\kappa$.
# 
# Entre la lista de materiales disponibles tenemos:
# - Agua (```H2O```)
# - Oro (```gold```)
# - Plata (```silver```)
# - Cobre (```Cu```)
# - Aluminio (```Al```)
# - Silice (```SiO2```)
# - Silicio (```Si```)
# - Dióxido de Titanio (```TiO2```)
# 
# Para utilizar las funciones debemos, primero, generar un arreglo con las longitudes de onda que deseamos graficar, y luego evaluar la función para determinar el índice de refracción.
# 
# Por ejemplo, supongamos que necesitamos el índice de refracción del sílice en el espectro $\lambda\in[0.5,20]$ $\mu$m.

# In[1]:


import numpy as np
import empylib.nklib as nk
import matplotlib.pyplot as plt

lam = np.linspace(0.5,20,100)   # arreglo de 100 datos entre 0.5 y 5.0 micrones
N   = nk.SiO2(lam)               # índice de refracción del sílice

# graficamos el índice de refracción
plt.plot(lam, N.real,'-b', label = 'n')
plt.plot(lam, N.imag,'-r', label = '$\kappa$')
plt.xlabel('longitud de onda ($\mu$m)')
plt.ylabel('Índice de refracción')
plt.legend()
plt.show()


# ### Modelos de Drude y Lorentz
# La librería ```empylib.nklib``` también posee funciones para determinar el **índice de refracción** a partir de modelos de Drude y Lorentz.
# 
# > Notar que estas funciones entregan el **índice de refracción**. Para esto, cada función toma el modelo de Drude o Lorentz  para determinar la **constante dieléctrica** $\varepsilon$, según lo [visto en clases](https://panxopanza.github.io/conversion_solar_termica/3_Interacci%C3%B3n_materia-luz/3_Interacci%C3%B3n_materia-luz.html). Luego el índice de refracción se determina a partir de $\sqrt{\varepsilon}$
# 
# Cada modelo requiere una serie de parámetros. Podemos verificar los parámetros requeridos mediante la función ```help```.

# In[2]:


help(nk.lorentz)


# Como vemos la función ```lorentz``` requiere los parámetros $\omega_p$, $\omega_n$ y $\Gamma$ en unidades de eV, además de $\varepsilon_\infty$. Por último, la función también requiere el espectro de longitudes de onda en unidades de micrones (um) a partir de la variable ```lam```.
# 
# En el siguiente ejemplo, graficaremos el modelo de Lorentz para $\lambda\in[2,20]$ $\mu$m, considerando los siguientes parámetros:
# - $\omega_n = 0.124$ eV ($\approx 10$ $\mu$m)
# - $\omega_p = 0.150$ eV 
# - $\Gamma = 0.01$ eV
# - $\varepsilon_\infty = 2.25$ 

# In[3]:


import numpy as np
import empylib.nklib as nk
import matplotlib.pyplot as plt

lam = np.linspace(2,20,200)   # arreglo de 100 datos entre 0.5 y 5.0 micrones

wn = 0.124  # Frecuencia natural (eV)
wp = 0.150  # Frecuencia wp (eV)
T = 0.01    # Taza de decaimiento (eV)
eps0 = 2.25

N   = nk.lorentz(eps0,wp,wn,T,lam)  # índice de refracción modelo de drude

# graficamos el índice de refracción
plt.plot(lam, N.real,'-b', label = 'n')
plt.plot(lam, N.imag,'-r', label = '$\kappa$')
plt.xlabel('longitud de onda ($\mu$m)')
plt.ylabel('Índice de refracción')
plt.legend()
plt.show()


# ## Reflexión/Transmissión (```waveoptics```)
# 
# La librería ```empylib.waveoptics``` contiene funciones para calcular los coeficientes de Fresnel y Flujo de energía de la porción transmitida y reflejada de la luz incidente.
# - ```interface``` para una [interface simple](https://panxopanza.github.io/conversion_solar_termica/2_ondas_EM_en_la_materia/2_ondas_EM_en_la_materia.html#coeficientes-de-fresnel)
# - ```multilayer``` para multicapas de [película delgada](https://panxopanza.github.io/conversion_solar_termica/2_ondas_EM_en_la_materia/2_ondas_EM_en_la_materia.html#refleccion-y-transmission-en-peliculas-delgadas)
# 
# - ```incoh_multilayer``` para multicapas de película delgada ignorando fenómenos de interferencia (luz incoherente)

# ### Luz incidente en una interface (```interface```)
# Esta función permite determinar los coeficientes de Fresnel y flujo de energía para la onda reflejada y transmitida a través de una interface. La función toma 4 argumentos: 
# - ```theta```: ángulo de incidencia (en radianes)
# - ```n1```: índice de refracción del medio sobre la interface
# - ```n2```: índice de refracción del medio bajo la interface
# - ```pol```: Polarización de la onda incidente (```'TM' ``` o ```'TE' ```)
# 
# La función necesita como mínimo 3 argumentos: ```theta```, ```n1```, ```n2```. En ese caso, ```pol= 'TM' ``` por defecto.
# 
# En el orden respectivo, el output es:
# - Reflectividad ```R``` y Tranmisividad ```T```
# - coefientes de Fresnel de reflexión ```r``` y transmisión ```t```.

# En el siguiente ejemplo analizaremos una interface que separa aire (índice de refracción 1.0) y un metal de Drude con $\omega_p = 3.1$ eV (aprox 0.4 $\mu$m), $\Gamma = 0.01$ eV y $\varepsilon_\infty = 1.0$. El ángulo de incidencia es $\theta_i = 30°$.
# 
# >Notar que ```n1=1.0``` es un valor ```float``` unidimencional, mientras que ```n2``` es un arreglo en el espectro $\lambda \in [0.3,1.0]$ $\mu$m. En este caso, la función repite ```n1=1.0``` por cada valor espectral de ```n2```. **En el caso que ```n1``` y ```n2``` sean un arreglo, ambos deben tener igual dimención.**

# In[4]:


import numpy as np
import empylib.waveoptics as wv
import empylib.nklib as nk

theta = np.radians(30)         # Angulo de incidencia (radianes)
lam = np.linspace(0.3,1.0,100) # Espectro de longitudes de onda

# Modelo de Drude
epsinf = 1.0 
wp = 3.1      # en eV (aproximadamente 0.4 micrones)
gamma = 0.01  # en eV

n2 = nk.drude(epsinf,wp,gamma,lam) # índice de refracción
n1 = 1.0

# Coeficientes de Fresnel y flujo de energia
Rp, Tp, rp, tp = wv.interface(theta,n1,n2, pol='TM') # polarizacion TM
Rs, Ts, rs, ts = wv.interface(theta,n1,n2, pol='TE') # polarizacion TE


# Abajo graficamos los coeficientes de Fresnel a la izquierda (solo la parte real) y el flujo de energía a la derecha. Notar como la reflectividad aumenta para $\lambda < 2\pi c_0/\omega_p$

# In[5]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2)
fig.set_size_inches(12,4)
ax[0].plot(lam,rs.real, '-r',label = 'r (TE)')
ax[0].plot(lam,rp.real,'--r',label = 'r (TM)')
ax[0].plot(lam,ts.real, '-b',label = 't (TE)')
ax[0].plot(lam,tp.real,'--b',label = 't (TM)')
ax[0].set_title('Coeficientes de Fresnel')
ax[0].set_xlabel('Longitud de onda ($\mu$m)')
ax[0].set_ylabel('Reflexión / Transmisión')
ax[0].legend()

ax[1].plot(lam,Rs, '-r',label = 'R (TE)')
ax[1].plot(lam,Rp,'--r',label = 'R (TM)')
ax[1].plot(lam,Ts, '-b',label = 'T (TE)')
ax[1].plot(lam,Tp,'--b',label = 'T (TM)')
ax[1].set_title('FLujo de energía')
ax[1].set_xlabel('Longitud de onda ($\mu$m)')
ax[1].set_ylabel('Reflectividad / Tranmisividad')
ax[1].legend()
plt.show


# ### Luz incidente en arreglos multicapas (```multilayer```)
# Esta función permite determinar los coeficientes de Fresnel y flujo de energía para la onda reflejada y transmitida a través de un arreglo de multicapas. La función toma 5 argumentos: 
# - ```lam```: Espectro de longitudes de onda (en $\mu$m)
# - ```tt```: ángulo de incidencia (en radianes)
# - ```N```: arreglo tuple con índices de refracción de cada capa + medio superior e inferior al arreglo
# - ```d```: arreglo tuple con espesores de cada capa (en micrones)
# - ```pol```: Polarización de la onda incidente (```'TM' ``` o ```'TE' ```)
# 
# La función necesita como mínimo 4 argumentos: ```lam```, ```tt``` ```N``` y ```d```. En ese caso, ```pol= 'TM' ``` por defecto.
#  
# En el orden respectivo, el output es:
# - Reflectividad ```R``` y Tranmisividad ```T```
# - coefientes de Fresnel de reflexión ```r``` y transmisión ```t```.

# Los elementos de ```N``` y  ```d```, deben estar ordenados según la dirección de la onda incidente. Por ejemplo, si consideramos: 
# - luz incidente ($\theta_i = 45°$, $\lambda\in[0.3,0.8]$ $\mu$m) 
# - Propagandose en aire ($N_1 = 1.0$),
# - La luz incide sobre una película de espesor $d = 300$ nm e índice de refracción $N_2 = 1.5$.
# - La película está depositada sobre un sustrato con índice de refracción $N_3 = 5.0 + 3i$:

# In[6]:


lam = np.linspace(0.3,0.8,100)  # espectro de longitudes de onda (um)
theta = np.radians(45)
N = (1.0, 1.5, 5.0 + 3j) # indices de refracción (above, mid, below)
d = 0.3 # 300 nm de espesor para capa intermedia

Rp, Tp, rp, tp = wv.multilayer(lam,theta, N, d, pol='TM')
Rs, Ts, rs, ts = wv.multilayer(lam,theta, N, d, pol='TE')


# Notar que ```len(d) = len(N) - 2```, debido a que los índices superior e inferior corresponden a los medios semi-infinitos sobre y bajo la capa. 
# 
# Por ejemplo, si ahora queremos determinar la respuesta óptica de un arreglo de una capa delgada de sílice ($d_1 = 100$ nm) sobre una capa de plata ($d_2 = 10$ nm), sobre un sustrato con índice de refracción $n_{back} = 5.0$ 

# In[7]:


lam = np.linspace(0.3,0.8,100)  # espectro de longitudes de onda (um)
theta = np.radians(45)

Nfront = 1.0                 # índice de refracción medio superior
N1     = nk.SiO2(lam)        # índice de refracción sílice
N2     = nk.silver(lam)      # índice de refracción plata
Nback  = 5.0                 # índice de refracción medio inferior
N = (Nfront, N1, N2, Nback)  # indices de refracción (above, mid, below)

d = (0.100, 0.010) # espesor para sílice y plata (en ese orden)

Rp, Tp, rp, tp = wv.multilayer(lam,theta, N, d, pol='TM')
Rs, Ts, rs, ts = wv.multilayer(lam,theta, N, d, pol='TE')

# Graficamos el flujo de energía
plt.plot(lam,Rp,'-r',label='R (TM)')
plt.plot(lam,Tp,'-b',label='T (TM)')
plt.plot(lam,Rs,'--r',label='R (TE)')
plt.plot(lam,Ts,'--b',label='T (TE)')
plt.title('aire/sílice/plata/n4=5.0')
plt.xlabel('Longitud de onda ($\mu$m)')
plt.ylabel('Refletividad / Transmisividad')
plt.ylim(0,1)
plt.legend()
plt.show()


# ### Luz incoherente en arreglos multicapas (```incoh_multilayer```)
# 
# Esta función es similar a ```multilayer``` pero para una fuente de luz incoherente. Considera los mismos 5 argumentos de ```multilayer``` con un argumento adicional ```coh_length``` para condicionar la longitud de coherencia (en $\mu$m). Por defecto, ```coh_length = 0```
# 
# Debido a que la función es para luz incoherente, el output es:
# - Reflectividad ```R``` y Tranmisividad ```T```
# 
# Por ejemplo, evaluemos el ejemplo de la [clase 2](https://panxopanza.github.io/conversion_solar_termica/2_ondas_EM_en_la_materia/2_ondas_EM_en_la_materia.html#refleccion-y-transmission-en-peliculas-delgadas) ($n_\mathrm{front}= 1.0$, $n_\mathrm{layer}= 1.5$, $n_\mathrm{back} = 4.3$), considerando una capa de espesor $d = 300$ nm, y $\theta_i = 30°$

# In[8]:


lam = np.linspace(0.3,0.8,100)  # espectro de longitudes de onda (um)
theta = np.radians(30)          # ángulo de incidencia

Nfront = 1.0                 # índice de refracción medio superior
N1     = 1.5                 # índice de refracción capa delgada
Nback  = 4.3                 # índice de refracción medio inferior
N = (Nfront, N1, Nback)      # indices de refracción (above, mid, below)

d = 0.3                      # espesor capa intermedia (um)

Rp_incoh, Tp_incoh = wv.incoh_multilayer(lam,theta, N, d, pol='TM') # caso luz incoherente

# Graficamos el flujo de energía
plt.plot(lam,Rp_incoh,'--r',label='$R_\mathrm{TM}$ (incoh)')
plt.plot(lam,Tp_incoh,'--b',label='$T_\mathrm{TM}$ (incoh)')
plt.title('arreglo 1.0/1.5/4.3')
plt.xlabel('Longitud de onda ($\mu$m)')
plt.ylabel('Refletividad / Transmisividad')
plt.ylim(0,1)
plt.legend()

# comparamos con el caso luz coherente
Rp, Tp = wv.multilayer(lam,theta, N, d, pol='TM')[:2]
plt.plot(lam,Rp,'-r',label='$R_\mathrm{TM}$ (coh)')
plt.plot(lam,Tp,'-b',label='$T_\mathrm{TM}$ (coh)')

plt.show()


# En el límite de solo una interface, ```interface```, ```multilayer``` y ```incoh_multilayer``` entregan el mismo resultado

# In[9]:


import numpy as np
import empylib.nklib as nk
import empylib.waveoptics as wv

lam = 0.5                # longitud de onda en micrones
theta = np.radians(30)   # ángulo de incidencia (en radianes)                    

N = (1.0, 1.5)  # interface aire/silice
d = ()          # sin espesores (solo una interface)

print('interface:\t\t R = %.3f, T = %.3f' % wv.interface(theta,N[0],N[1])[:2])
print('multilayer:\t\t R = %.3f, T = %.3f' % wv.multilayer(lam,theta,N,d)[:2])
print('incoh_multilayer:\t R = %.3f, T = %.3f' % wv.incoh_multilayer(lam,theta,N,d))


# ## Scattering de mie (```miescattering```)
# En esta librería, la función principal es ```scatter_efficiency```, que permite determinar las secciones transversales de scattering, absorción y extinción para una partícula esférica de diámetro $D$.
# 
# Los pámetros de entrada son:
# - ```lam```: Espectro de longitudes de onda (en $\mu$m)
# - ```Nh```: Índice de refracción del medio circundante
# - ```Np```: Índice de refracción de la partícula
# - ```D```: Diámetro de la partícula (en $\mu$m)
# 
# Los parámetros de salida son
# - ```Qext```: coeficiente de extinción
# - ```Qsca```: coeficiente de scattering
# - ```gcos```: parámetro de asimetría
# 
# Los coeficientes de extinción ($Q_\mathrm{ext}$) y scattering ($Q_\mathrm{sca}$) se relacionan con las respectivas secciones transversales por $C_\mathrm{ext} = Q_\mathrm{ext}A_c$, $C_\mathrm{sca} = Q_\mathrm{sca}A_c$, donde $A_c = \pi D^2/4$ es la sección transversal de la esfera.
# 
# La sección transversal de absorción ($C_\mathrm{abs}$), se determina por $C_\mathrm{abs} = C_\mathrm{ext} - C_\mathrm{sca}$

# En el ejemplo de abajo, calculamos la $C_\mathrm{abs}$, $C_\mathrm{sca}$ y $C_\mathrm{ext}$ para una partícula de oro de $D = 100$ nm de diámetro, alojada de sílice. El espectro considerado es $\lambda\in[0.3,1.0]$ $\mu$m

# In[10]:


import empylib.miescattering as mie
import empylib.nklib as nk
import matplotlib.pyplot as plt

lam = np.linspace(0.3,1.0,100) #espectro de longitudes de onda (arreglo de 100 puntos entre 0.3 y 1.0 micrones)
Nh = nk.SiO2(lam)
Np = nk.gold(lam) 
D = 0.100  # diámetro de la partícula

# determinamos parámetros de eficiencia
qext, qsca, gcos = mie.scatter_efficiency(lam,Nh,Np,D)

# convertimos los resultados a secciones transversales
Ac = np.pi*D**2/4 # sección transversal de la partícula
Csca = qsca*Ac
Cext = qext*Ac
Cabs = Cext - Csca

# graficamos los resultados
plt.plot(lam,Csca,'-r',label='$C_\mathrm{sca}$')
plt.plot(lam,Cabs,'-b',label='$C_\mathrm{abs}$')
plt.plot(lam,Cext,'-k',label='$C_\mathrm{ext}$')
plt.xlabel('Longitud de onda ($\mu$m)')
plt.ylabel('Sección transversal ($\mu$m$^2$)')
plt.title('Scattering EM partícula de oro en sílice')
plt.legend()
plt.show()


# ## Transporte Radiativo
# Para transporte radiativo tenemos dos librerías:
# - ```rad_transfer``` con funciones para cálculos simples (como Beer-Lambert)
# - ```iadpython``` para simulaciones de scattering multiple
# 
# ### Beer-Lambert (```T_beer_lambert```)
# La función ```T_beer_lambert``` de la librería ```empylib.rad_transfer``` permite un rápido cálculo de la transmisivitidad a través de un medio de espesor $d$ con incrustaciones.
# 
# La función requiere los siguientes parámetros de entrada:
# - ```lam```: Espectro de longitudes de onda (en $\mu$m)
# - ```theta```: Ángulo de incidencia (en radianes)
# - ```tfilm```: Espesor del material
# - ```N```: Índice de refracción del medio superior, material intermedio, y medio inferior (arreglo tuple ```len(N) = 3```)
# - ```fv```: Fracción de volumen de las incrustaciones (0.01 corresponde a 1% v/v) 
# - ```D```: Diámetro de la partícula (en $\mu$m)
# - ```Np```: Índice de refracción de las partículas (se debe cumplir la condición: ```len(Np) = len(lam)```)
# 
# Los parámetros de salida son:
# - ```Tspec```: Transmisividad especular
# - ```Ttot```: Transmisividad total

# En el siguiente ejemplo, consideramos una película de sílice de espesor $1.0$ mm, con porosidad de 0.01% donde los poros tienen un de diámetro $D = 200$ $\mu$m ($N_{poro} = 1.0$). Los medios superior e inferior corresponden a aire. La luz incide en dirección $\theta_i = 0°$.

# In[11]:


import empylib.rad_transfer as rt
import numpy as np
import matplotlib.pyplot as plt

lam = np.linspace(0.3,1.0,100)
theta = np.radians(0) # 30 grados en radianes
tfilm = 1000 # espesor en micrones
N = (1.0,nk.SiO2(lam),1.0)  # indice de refracción superior, intermedio e inferior
fv = 0.0001   # fracción de volúmen de los poros
D = 0.2 # diámetro de los poros
Np = np.ones(lam.shape)

Ttot, Tspec = rt.T_beer_lambert(lam,theta,tfilm,N,fv,D,Np)

plt.plot(lam,Tspec,'--k',label = 'Tspec')
plt.plot(lam,Ttot,'-k',label = 'Ttot')
plt.xlabel('Longitud de onda ($\mu$m)')
plt.ylabel('Transmisividad')
plt.title(r'Sílice poroso (fv = 0.01% v/v)')
plt.legend()
plt.ylim(0,1)


# ### Scattering multiple (```iadpython```)
# La modelación de scattering múltiple está considerada en la librería ```iadpython```. Hay muchos detalles de esta libería que están fuera del alcance de este curso. Por esto, se recomienda seguir el siguiente script, y editar solo la sección marcada en el encabezado. Los parámetros de entrada son similares a los de la función ```T_beer_lambert```, **con la diferencia que el espesor del material con incrustaciones debe ir en unidades de mm.**
# 
# En el ejemplo, se modela un sílice poroso con las siguientes características:
# - Espesor de 10 cm (```tfilm = 100```, unidades en mm)
# - porosidad 60%
# - Tamaño de poro $1.0$ $\mu$m
# - Espectro $\lambda\in[0.3,1.0]$ $\mu$m

# In[12]:


import iadpython as iad
import empylib.miescattering as mie
import empylib.nklib as nk
import numpy as np

# Solo modificar estos parámetros
#---------------------------------------------------------------
lam = np.linspace(0.3,1.0,100) # espectro de longitudes de onda
tfilm = 100                    # espesor en mm
Nh = nk.SiO2(lam)              # indice de refracción del material con incrustaciones
fv = 0.6                       # fracción de volúmen de los poros
D = 1.0                        # diámetro de los poros (micrones)
Np = np.ones(lam.shape)        # índice de refracción partícula
#---------------------------------------------------------------

# determinamos parámetros de eficiencia
qext, qsca, gcos = mie.scatter_efficiency(lam,Nh,Np,D)

# convertimos los resultados a secciones transversales
Ac = np.pi*D**2/4 # sección transversal de la partícula
Csca = qsca*Ac
Cext = qext*Ac
Cabs = Cext - Csca
Vp = np.pi*D**3/6

# iteramos en iadpython
Rtot = np.zeros(lam.shape)
Ttot = np.zeros(lam.shape)
for i in range(len(lam)):
    kz_imag = 2*np.pi/lam[i]*Nh[i].imag  # parte imaginaria del vector de onda
    
    mu_s = fv*Csca[i]/Vp  
    mu_a = fv*Cabs[i]/Vp + 2*kz_imag
    g = gcos[i]
    d = tfilm

    a = mu_s/(mu_a+mu_s)
    b = mu_s/(mu_a+mu_s) * d

    # air / sample / air
    s = iad.Sample(a=a, b=b, g=g, n=Nh[i].real, n_above=1.0, n_below=1.0)
    ur1, ut1, uru, utu = s.rt()
    
    Rtot[i] = ur1
    Ttot[i] = ut1

plt.plot(lam,Rtot,'-r',label='R')
plt.plot(lam,Ttot,'-b',label='T')
plt.xlabel('Longitud de onda ($\mu$m)')
plt.ylabel('Reflectividad / Transmisividad')
plt.title(r'Sílice poroso (fv = 60% v/v)')
plt.legend()
plt.ylim(0,1)

