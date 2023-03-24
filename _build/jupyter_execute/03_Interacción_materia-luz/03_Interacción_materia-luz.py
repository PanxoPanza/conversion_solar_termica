#!/usr/bin/env python
# coding: utf-8

# # Interacción materia-luz

# ## Repaso de vibraciones mecánicas

# ### Frecuencia natural de un sistema vibratorio

# La frecuencia natural de un sistema vibratorio representa la frecuencia de oscilación del sistema en ausencia de amortiguación y fuerzas externas.

# Por ejemplo, en el caso simplificado de un sistema masa resorte
# 
# <img src="./images/free_sistem_one_degree.png" width="250px" align= center>
# 
# donde, $k$ es la constante de rigidez del resorte, y $m$ es la masa.

# La ecuación gobernante está dada por:
# 
# \begin{equation*}
# \ddot{x} + \omega_n^2 x = 0 
# \end{equation*}
# 
# donde $\omega_n = \sqrt{k/m}$, es la frecuencia natural del sistema

# ### Vibración forzada amortiguada con un grado de libertad
# La frecuencia natural cobra relevancia cuando analizamos vibraciones forzadas.
# 
# Consideremos, por ejemplo, el sistema masa-resorte amortiguado, con constante de amortiguación $c$, excitado por una fuerza externa oscilatoria de la forma $F(t) = F_0 e^{i\omega t}$, donde $F_0$ es una constante. 

# <img src="./images/forced_damped_system.png" width="150px" align= center>

# La ecuación gobernante de este sistema está dada por:
# 
# \begin{equation*}
# \ddot{x} + 2\zeta\omega_n\dot{x} +  \omega_n^2 x = \frac{F_0}{m} e^{i\omega t},
# \end{equation*}
# 
# donde $\zeta = \frac{c}{2\omega_nm}$ es la razón de amortiguación

# En su forma general, la solución a este sistema está dada $x(t) = x_p(t) + x_h(t)$, donde:

# \begin{eqnarray*}
# x_h(t) &=& C e^{-\zeta \omega_n t}e^{i\omega_n\sqrt{1 - \zeta^2} t} &\quad&\mathrm{solución~homogenea}
# \\[10pt]
# x_p(t) &=& \frac{F_0/k}{\omega^2 - \omega_n^2 + 2i\zeta \omega_n \omega}e^{i\omega t} &\quad&\mathrm{solución~particular}
# \end{eqnarray*}
# 
# donde $C$ es una amplitud arbitraria definida por las condiciones iniciales del sistema.

# En estado estacionario, solo la solución particular $x_p(t)$ es relevante. La solución homogénea $x_h(t)$, decae en el tiempo y se le conoce como **respuesta transciente**. 

# <img src="./images/forced_damped_motion.png" width="400px" align= center>

# Podemos repesentar la amplitud de $x_p = Ae^{i\omega t}$, como $A = |A|e^{i\phi}$, donde $\phi$ es la fase. Asi, la solución estacionaria queda de la forma:
# 
# \begin{equation*}
# x_p = |A|e^{i\left(\omega t + \phi\right)}
# \end{equation*}

# Cuando $\omega/\omega_n = 1$, el sistema entra en resonancia. Esta respuesta se manifiesta con la característica amplificación de $|A|$.
# 
# <img src="./images/resonance.png" width="600px" align= center>

# Revisemos esta herramienta interactiva del <a href="https://www.compadre.org/osp/EJSS/4026/134.htm?F=1">movimiento forzado amortiguado</a>

# ## Interacción de luz con moléculas
# ### El oscilador armónico
# Consideremos la molecula de agua.

# <img src="./images/water_molecule.png" width="400px" align= center>

# Esta molécula está **polarizada**, es decir, posee una **carga eléctrica neta positiva en un extremo y negativa en otro**. 
# 
# Esto ocurre debido a que los electrones se mantienen, preferentemente, en la región cercana al núcleo del oxígeno.

# El enlance entre el hidrógeno y oxígeno genera una fuerza de atracción, la cual es contrarestada por la repulción entre los núcleos. En forma simplificada, podemos representar este fenómeno mediante un sistema *masa-resorte*.

# <img src="./images/water_molecule_spring.png" width="300px" align= center>

# En otras palabras, cada enlace en la molécula de agua representa un oscilador armónico, con una fuerza de restauración:
# 
# \begin{equation*}
# F = -k(r - r_0)
# \end{equation*}
# 
# donde $k$ es la constante de rigidez y $r_0$ es la posición de los núcleos en equilibrio.

# ### Modelo de Lorentz
# 
# Consideremos ahora la interacción de una onda electromagnética con una molécula di atómica.

# <img src="./images/molecule_spring_mass.png" width="200px" align= center>

# El campo eléctrico de la onda oscilatoria ($E_0e^{-i\omega t}$), ejerce una fuerza $F = qE_0e^{-i\omega t}$ sobre cada polo, donde $q$ es la carga eléctrica del polo positivo (o negativo). 

# Consideramos, ademas, una fuerza de amortiguación, $F_{c} = - m\Gamma \dot{x}$, que representa la disipación de energía por la colición entre los electrones y los nucleos, además de otras interacciónes electromagnéticas. La constante **$\Gamma$ es la taza de decaimiento** (se mide en unidades 1/s).

# 
# 
# ***El fenómeno, así, representa un sistema forzado amortiguado***

# Asumiendo un eje de referencia situado en el polo positivo, la ecuación de movimiento está dada por:
# 
# \begin{equation*}
# m\ddot{x} + m\Gamma \dot{x} +  k x = qE_0 e^{-i\omega t},
# \end{equation*}
# 
# donde $m$ es la masa del polo positivo, $k$ es la constante de rigidez del enlace entre los polos.

# La solución estacionaria está dada por la solución particular:
# 
# \begin{equation*}
# x_p(t) = \frac{q/mE_0}{\omega_n^2 - \omega^2 - i\Gamma \omega}e^{-i\omega t}
# \end{equation*}

# El desplazamiento del polo positivo respecto a su estado en equilibrio induce un **momento dipolar**, $\vec{p}$, el cual expresamos a través de la relación:
# 
# \begin{equation*}
# \vec{p} = q\vec{x}_p(t) =  \frac{q^2/m}{\omega_n^2 - \omega^2 - i\Gamma \omega}E_0e^{-i\omega t}\hat{e}\quad\mathrm{[C\cdot m]}
# \end{equation*}
# 
# donde $\hat{e}$ es la dirección del campo eléctrico

# Definimos como **densidad de polarización**, $\vec{P}$, al momento dipolar total por unidad de volumen:
# 
# \begin{equation*}
# \vec{P} = N_p \vec{p} = \frac{N_pq^2/m}{\omega_n^2 - \omega^2 - i\Gamma \omega}\vec{E}\quad\mathrm{\left[\frac{C\cdot m}{m^3}\right]}
# \end{equation*}

# En presencia de un medio polarizado, la ley de Gauss se modifica como: $\nabla\cdot\left(\varepsilon_0\vec{E} + \vec{P}\right) = 0$. 

# Representando esta relación en la forma, $\nabla\cdot\varepsilon_0\varepsilon\vec{E} = \rho$, podemos deducir un modelo para la constante dieléctrica del sistema $\varepsilon$:
# 
# \begin{equation*}
# \varepsilon = 1 +\frac{\omega_p^2}{\omega_n^2 - \omega^2 - i\Gamma \omega},
# \end{equation*}
# 
# con $\omega_p^2 = \frac{N_pq^2}{\varepsilon_0 m}$

# En el caso del agua, la molecula posee un dipolo eléctrico neto adicional al dipolo inducido. El efecto de la polarización neta se puede representar, cambiando el primer término por un valor constante $\varepsilon_\infty$.

# El modelo completo se conoce como **modelo de Lorentz**:
# 
# \begin{equation}
# \varepsilon = \varepsilon_\infty + \frac{\omega_p^2}{\omega_n^2 - \omega^2 - i\Gamma \omega}\quad\mathrm{Modelo~de~Lorentz},
# \end{equation}

# Usaremos la función `lorentz` del módulo `empylib.nklib` para generar el índice de refracción y constante dielectrica a partir del modelo de Lorentz, con los parámetros: $\varepsilon_\infty = 2.0$, $\Gamma = 0.1\omega_n$, y $\omega_p = \omega_n$

# > Notar que el modelo de Lorentz está en función de la frecuencia angular $\omega$ (en $\mathrm{eV}$), mientras que la función de `lorentz` de `empylib.nklib` requiere valores de $\lambda$ en longitudes de onda (en $\mu \mathrm{m}$).

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import empylib.nklib as nk
import empylib as em

# parámetros del modelo
epsinf = 2.0  # adimensional
wp = 1.0      # en eV
wn = 1.0      # en eV
gamma = 0.1   # en eV

# espectro 
w = 1/np.linspace(1E-3,2,1000)          # en "eV"
lam = em.convert_units(w,'eV','um')     # convertimos a "micrones"

# creamos el modelo de lorentz
N1 = nk.lorentz(epsinf,wp,wn,gamma,lam) # índice de refracción a partir del modelo de Lorentz
eps1 = N1**2                            # constante dieléctrica

# formateamos el lienzo para graficar
fig, ax = plt.subplots(1,2)             # número de ejes en la figura
fig.set_size_inches(11, 3)              # tamaño de la figura
plt.rcParams['font.size'] = '12'        # tamaño de fuente

#ploteamos
ax[0].plot(wn/w,np.real(eps1),'b',label=r"$\varepsilon'$")
ax[0].plot(wn/w,np.imag(eps1),'r',label=r"$\varepsilon''$")
ax[1].plot(wn/w,np.real(N1),'b',label=r"$n$")
ax[1].plot(wn/w,np.imag(N1),'r',label=r"$\kappa$")

for i in [0,1]:
    ax[i].set_xlabel('$\omega/\omega_n$ ')
    ax[i].grid()
    ax[i].legend(frameon=False)
ax[0].set_ylabel(r"Constante dielectrica, $\varepsilon = \varepsilon'+ \varepsilon''$")
ax[1].set_ylabel(r'Indice de refracción, $N = n + i\kappa$')
plt.show()


# >**El modelo de Lorentz se utiliza como modelo de ajuste para representar la interacción de la luz con los modos vibratorios en la materia**

# Por ejemplo, la molécula de agua tiene 3 modos de vibración fundamentales en las longitudes de onda $\lambda = $ 2.98, 2.93 y 5.91 $\mu$m (3351, 3412 y 1691 cm$^{-1}$)

# In[2]:


from IPython.display import YouTubeVideo
YouTubeVideo('1uE2lvVkKW0', width=600, height=400,  playsinline=0)


# Usamos el módulo `nklib` de la librería `empylib` para graficar el índice de refracción del agua

# In[3]:


get_ipython().run_cell_magic('capture', 'showplot1', 'import numpy as np\nimport matplotlib.pyplot as plt\nimport empylib.nklib as nk\n\n# creamos el espectro\nlam = np.linspace(0.2,10,1000)   # espectro de longitudes de onda\nN1   = nk.H2O(lam)               # índice de refracción\neps1 = N1**2                     # constante dieléctrica\n\n# formateamos el lienzo para graficar\nfig, ax = plt.subplots(1,2)             # número de ejes en la figura\nfig.set_size_inches(11, 3)              # tamaño de la figura\nplt.rcParams[\'font.size\'] = \'12\'        # tamaño de fuente\n\n# Graficamos el resultado\nax[0].plot(lam,eps1.real,\'b\',label=r"$\\varepsilon\'$")   # constante dieléctrica (parte real)\nax[0].plot(lam,eps1.imag,\'r\',label=r"$\\varepsilon\'\'$")  # constante dieléctrica (parte imaginaria)\nax[1].plot(lam,N1.real,\'b\',label=r"$n$")                # índice de refracción (parte real)\nax[1].plot(lam,N1.imag,\'r\',label=r"$\\kappa$")           # índice de refracción (parte imaginaria)\n\n# marcamos los valores máximos con una línea\nfor i in [280, 599]:\n    ax[0].axvline(x = lam[i], color=\'k\', ls=\'--\', lw=\'1.0\')\n    ax[1].axvline(x = lam[i], color=\'k\', ls=\'--\', lw=\'1.0\')\n    ax[0].text(lam[i]*1.02,eps1[i].imag,r\'%.3f $\\mu$m\'% lam[i], fontsize=\'12\')\n\nfor i in [0,1]:\n    ax[i].set_xlabel(\'Longitud de onda, $\\lambda$ ($\\mu$m)\')\n    ax[i].grid()\n    ax[i].set_xlim(0.2,10)\n    ax[i].legend(frameon=False)\nax[0].set_ylabel(r"Constante dielectrica, $\\varepsilon = \\varepsilon\'+ \\varepsilon\'\'$")\nax[1].set_ylabel(r\'Indice de refracción, $N = n + i\\kappa$\')\nplt.show()\n')


# Al graficar el índice de refracción notamos que la gráfica muestra dos oscilaciones de Lorentz. 

# In[4]:


showplot1()


# La resonancia en $\lambda =$ 2.98 $\mu$m (3351 cm$^{-1}$) no está presente en el espectro.

# Este modo no es compatible con la oscilación de una onda electromagnética plana. Así la luz no interactúa con esta vibración y, por lo tanto, no se ve representada en el espectro del índice de refracción.

# ## Interacción de la luz con materiales sólidos
# El análisis anterior generalmente se aplica a gases, donde las moléculas no interactúan entre sí. En el caso de materiales sólidos, la interacción entre moléculas es fuerte, y genera bandas electrónicas de energía.

# - **Banda de valencia**: corresponde a la banda ocupada por electrones con el mayor nivel de energía. En esta banda los electrones permanecen en un estado "ligado" al núcleo.
# 
# - **Banda de conducción**: corresponde a la banda no ocupada por electrones con el menor nivel de energía. En esta banda los electrones se mueven líbremente por el material
# 
# - **Banda prohibida (*band-gap*)**: Es la diferencia entre la banda de conducción y la banda de valencia

# <img src="./images/bandas_electronicas.png" width="300px" align= center>

# A partir de la separación entre la banda de conducción y la banda de valencia, podemos clasificar tres tipos de materiales en función de sus propiedades electrónicas:
# 
# <img src="./images/energy_bands_clasification.png" width="450px" align= center>

# - **Conductor**, donde las bandas de conducción y valencia están traslapadas (bandgap = 0). En estos materiales, parte de los electrones están alojados en la banda de conducción y, por lo tanto, son capaces de conducir corriente eléctrica en presencia de un campo eléctrico.
# 
# - **Semiconductor**, donde las bandas de conducción y valencia están separadas. Sin embargo, la energía del bandgap es relativamente pequeña, de manera que un electrón puede ser llevado a la banda de conducción mediante un potencial eléctrico razonable, o mediante una onda electromagnética.
# 
# - **Aislante**, donde las bandas de conducción y valencia están muy separadas. El umbral para excitar un electrón a la banda de conducción es demaciado grande y, por lo tanto, el material no es capaz de conducir corriente.

# La respuesta óptica de cada tipo de material está condicionada por sus propiedades electrónicas

# ### Aislantes (modelo de Lorentz)
# Debido a que los electrones en un aislante están fuertemente ligados al núcleo, la respuesta óptica de este material está condicionada por los modos de vibración de la red atómica. Así, la constante dieléctrica y el indice de refración siguen un comportamiento similar al modelo de Lorentz.

# Por ejemplo, el sílice (SiO$_2$)

# In[5]:


get_ipython().run_cell_magic('capture', 'showplot1', 'import numpy as np\nimport matplotlib.pyplot as plt\nimport empylib.nklib as nk\n\nlam = np.linspace(0.2,30,1000)   # espectro de longitudes de onda\nN1   = nk.SiO2(lam)              # índice de refracción\neps1 = N1**2                     # constante dieléctrica\n\n# formateamos el lienzo para graficar\nfig, ax = plt.subplots(1,2)             # número de ejes en la figura\nfig.set_size_inches(11, 3)              # tamaño de la figura\nplt.rcParams[\'font.size\'] = \'12\'        # tamaño de fuente\n\n# Graficamos el resultado\nax[0].plot(lam,eps1.real,\'b\',label=r"$\\varepsilon\'$")   # constante dieléctrica (parte real)\nax[0].plot(lam,eps1.imag,\'r\',label=r"$\\varepsilon\'\'$")  # constante dieléctrica (parte imaginaria)\nax[1].plot(lam,N1.real,\'b\',label=r"$n$")                # índice de refracción (parte real)\nax[1].plot(lam,N1.imag,\'r\',label=r"$\\kappa$")           # índice de refracción (parte imaginaria)\n\nfor i in [0,1]:\n    ax[i].set_xlabel(\'Longitud de onda, $\\lambda$ ($\\mu$m)\')\n    ax[i].grid()\n    ax[i].legend(frameon=False)\nax[0].set_ylabel(r"Constante dielectrica, $\\varepsilon = \\varepsilon\'+ \\varepsilon\'\'$")\nax[1].set_ylabel(r\'Indice de refracción, $N = n + i\\kappa$\')\nplt.show()\n')


# In[6]:


showplot1()


# ### Conductores (modelo de Drude)
# En este caso los electrónes se mueven libremente por la red atómica.

# Podemos representar la interacción de los electrones libres con una onda electromagnética utilizando la ecuación de movimiento. En este caso, la fuerza de restauración $kx = 0$, y la ecuación es:
# 
# \begin{equation*}
# m_e\ddot{x} + m_e\Gamma_e \dot{x} = eE_0 e^{-i\omega t},
# \end{equation*}
# 
# donde $m_e$, $e$ y $\Gamma_e$ son, respectivamente, la masa, la carga elemental y la taza de decaimiento del electrón.

# Mediante un procedimiento similar al utilzado para el modelo de Lorentz, derivamos el **modelo de Drude** para conductores:
# 
# \begin{equation}
# \varepsilon = \varepsilon_\infty - \frac{\omega_p^2}{\omega^2 + i\Gamma_e \omega},\quad\mathrm{Modelo~de~Drude},
# \end{equation}
# 
# donde $\omega_p^2 = \frac{N_ee^2}{\varepsilon_0 m}$ se conoce como frecuencia de plasma, y $N_e$ es la densidad de número de electrones. Similar al modelo de Lorentz, $\varepsilon_\infty$ representa la polarización neta del material.

# Usaremos la función `drude` del módulo `empylib.nklib` para generar el índice de refracción y constante dielectrica a partir del modelo de Drude, con los parámetros: $\varepsilon_\infty = 2.0$, $\Gamma_e = 0.1$, y $\omega_p = 1~\mathrm{eV}$

# > Notar que el modelo de Drude está en función de la frecuencia angular $\omega$ (en $\mathrm{eV}$), mientras que la función `drude` de `empylib.nklib` requiere longitudes de onda en unidades $\mu \mathrm{m}$.

# In[7]:


import numpy as np
import matplotlib.pyplot as plt
import empylib.nklib as nk
import empylib as em

w = 1/np.linspace(1E-3,5,1000)         # espectro de energía (eV)
lam = em.convert_units(w,'eV','um')    # convertimos a longitudes de onda

# contruimos el modelo de Drude
epsinf = 2.0 
wp = 1.0                               # en eV
gamma = 0.1                            # en eV
N1 = nk.drude(epsinf,wp,gamma,lam)     # índice de refracción
eps1 = N1**2                           # constante dieléctrica

# formateamos el lienzo para graficar
fig, ax = plt.subplots(1,2)             # número de ejes en la figura
fig.set_size_inches(11, 3)              # tamaño de la figura
plt.rcParams['font.size'] = '12'        # tamaño de fuente

# graficamos constante dielectrica e índice de refracción
ax[0].plot(wp/w,eps1.real,'b',label=r"$\varepsilon'$")
ax[0].plot(wp/w,eps1.imag,'r',label=r"$\varepsilon''$")
ax[1].plot(wp/w,N1.real,'b',label=r"$n$")
ax[1].plot(wp/w,N1.imag,'r',label=r"$\kappa$")

# formateamos los ejes
for i in [0,1]:
    ax[i].set_xlabel('$\omega_p/\omega$ ')
    ax[i].grid()
    #ax[i].set_xlim(0,5)
    ax[i].legend(frameon=False)
ax[0].set_ylabel(r"Constante dielectrica, $\varepsilon = \varepsilon'+ \varepsilon''$")
ax[1].set_ylabel(r'Indice de refracción, $N = n + i\kappa$')
plt.show()


# Una característica del modelo de Drude es que $\varepsilon' < 0$ para $\omega_p/\omega \gtrsim 1$. Esto se manifiesta en el índice de refracción como $\kappa > n$

# Cuando $\kappa > n$ la reflectividad aumenta significativamente. Así, los materiales conductores tienen alta reflectividad en ambas polarizaciones, cuando $\omega_p/\omega \gtrsim 1$

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from empylib.waveoptics import interface
import empylib as em
import empylib.nklib as nk

# espectro para graficar
w = 1/np.linspace(1E-3,5,1000)             # espectro de energía (eV)
lam = em.convert_units(w,'eV','um')        # convertimos espectro a longitudes de onda

# Modelo de Drude
epsinf = 2.0 
wp = 1.0                                   # en eV
gamma = 0.1                                # en eV
n2 = nk.drude(epsinf,wp,gamma,lam)         # índice de refracción

# índice de refracción aire
n1 = np.ones(n2.shape)                    

# Reflectividad en una interface entre un material de Drude y aire
Rp = interface(0,n1,n2, pol='TM')[0] # TM
Rs = interface(0,n1,n2, pol='TE')[0] # TE

# formateamos el lienzo para graficar
fig, ax = plt.subplots()             # número de ejes en la figura
fig.set_size_inches(6, 3)              # tamaño de la figura
plt.rcParams['font.size'] = '12'        # tamaño de fuente

# graficamos 
ax.plot(1/w,Rp, label='$R_\mathrm{TM}$', color='red', lw=3.0)
ax.plot(1/w,Rs, label='$R_\mathrm{TE}$', color='blue', lw=2.0, ls='--')

# formateamos los ejes
ax.set_xlim([0,5])
ax.set_ylim([0,1.0])
ax.set_xlabel('$\omega_p/\omega$')
ax.set_ylabel('Reflectividad')
ax.legend(frameon=False)
plt.show()


# En general, los metales pueden ser bien representados por el modelo de Drude. En general, $\omega_p$ se ubica en el espectro UV y, por lo tanto, reflejan la luz visible (efecto espejo)

# Por ejemplo, en el caso de aluminio $\omega_p = 15~\mathrm{eV}\approx 90~\mathrm{nm}$

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import empylib.nklib as nk

# índice de refracción y constante dielectrica aluminio
lam = np.linspace(0.01,1.0,1000)        # espectro de longitudes de onda (um)
N1 = nk.Al(lam)                         # índice de refracción
eps1 = N1**2                            # constante dieléctrica

# formateamos el lienzo para graficar
fig, ax = plt.subplots(1,2)             # número de ejes en la figura
fig.set_size_inches(11, 3)              # tamaño de la figura
plt.rcParams['font.size'] = '12'        # tamaño de fuente

# graficamos
ax[0].plot(lam,eps1.real,'b',label=r"$\varepsilon'$")
ax[0].plot(lam,eps1.imag,'r',label=r"$\varepsilon''$")
ax[1].plot(lam,N1.real,'b',label=r"$n$")
ax[1].plot(lam,N1.imag,'r',label=r"$\kappa$")

# formateamos los ejes
for i in [0,1]:
    ax[i].set_xlabel('Longitud de onda, $\lambda$ ($\mu$m)')
    ax[i].grid()
    ax[i].set_xlim(0.01,1.0)
    ax[i].legend(frameon=False)
ax[0].set_ylabel(r"Constante dielectrica, $\varepsilon = \varepsilon'+ \varepsilon''$")
ax[1].set_ylabel(r'Indice de refracción, $N = n + i\kappa$')
plt.show()


# Notemos como para $\lambda \approx 0.8$ $\mu$m, la respuesta del material se desvía del modelo de Drude. Esta respuesta esta asociada a un modo de vibración (modelo de Lorentz).

# ### Semiconductores (absorción interbanda)

# En este caso las interacciones con ondas electromagnéticas están dictadas por bandas de absorción asociadas a la excitación de electrones de valencia a la banda de conducción. 
# 
# Este fenómeno se conoce como **absorpción interbanda**, y ocurre cuando la energía del fotón $\hbar\omega$ ($\hbar = 6.58\times 10^16$ eV$\cdot$s) es superior al bandgap del material.

# <img src="./images/photoexcited_electrons.png" width="300px" align= center>

# Los semiconductores son los materiales fundamentales en transistores, LED y celdas fotovoltaicas. El semiconductor más conocido es el silicio (Si).
# 
# El índice de refracción del silicio es:

# <img src="./images/si_nk.png" width="700px" align= center>

# En general, los materiales pueden presentar más de un tipo de respuesta.

# Por ejemplo, el oro tiene absorción interbanda en longitudes de onda $\lambda < 0.5$ $\mu$m, combinado con el modelo de Drude.
# <img src="./images/gold_nk.png" width="350px" align= center>

# Debido a esta respuesta, el oro absorbe las longitudes de onda correspondientes al azul y violeta, y refleja el resto de los colores.
# 
# La siguiente figura muestra el color del oro según el ángulo de incidencia en base al espectro de reflección de una interface aire/oro.

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
from empylib.waveoptics import interface
from empylib.ref_spectra import AM15
from empylib.ref_spectra import color_system as cs
cs = cs.hdtv

# creamos índices de refracción
lam = np.linspace(0.3,0.8,81)   # espectro de longitudes de onda (en um)
n2 = nk.gold(lam)               # índice de refracción oro
n1 = np.ones(n2.shape)          # índice de refracción aire

# Reflectividad en capa delgada en función del ángulo "tt"
Rp = lambda tt : interface(tt, n1,n2, pol='TM')[0]
Rs = lambda tt : interface(tt, n1,n2, pol='TE')[0]

# formateamos la figura
fig, ax = plt.subplots()                # número de ejes en la figura
fig.set_size_inches(6, 3)               # tamaño de la figura
plt.rcParams['font.size'] = '12'        # tamaño de fuente        

# graficamos el color reflejado según el ángulo de incidencia
theta = np.linspace(0,90,100)           # angulo de incidencia
for i in range(len(theta)): 
    R = 0.5*Rp(np.radians(theta[i])) + 0.5*Rs(np.radians(theta[i]))
    Irad = R*AM15(lam)
    html_rgb = cs.spec_to_rgb(Irad, lam, out_fmt='html')
    ax.axvline(theta[i], color=html_rgb, linewidth=6) 
ax.set_xlim([min(theta),max(theta)])
ax.set_ylim([0,1.0])
ax.axes.yaxis.set_visible(False)
ax.set_xlabel('Ángulo de incidencia (deg)')
plt.show()


# Otro ejemplo es el dioxido de titanio (TiO$_2$), el cual presenta absorción interbanda en el espectro ultravioleta, y oscilaciones de Lorentz en el infrarojo.
# 
# <img src="./images/tio2_nk.png" width="700px" align= center>

# Debido a la absorcion UV, TiO$_2$ es muy utilizado en cremas para protección solar.

# ## Referencias
# - Rao S. S. **Chapter 4 - Vibration Under General Forcing Conditions** in *Mechanical Vibrations*, 6th Ed, Pearson, 2018
# 
# - Griffths D., **Chapter 4.1 - Polarization** in *Introduction to Electrodynamics*, 4th Ed, Pearson, 2013
# 
# - Simmons J. and Potter K., **Chapter 2 and 3** in *Optical Materials*, 1st Ed, Academic Press, 2000
