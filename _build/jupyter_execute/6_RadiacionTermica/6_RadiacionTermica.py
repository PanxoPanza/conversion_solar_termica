#!/usr/bin/env python
# coding: utf-8

#  <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # Radiación Térmica
# <br><br><br><br>
# Profesor: Francisco Ramírez Cuevas<br>
# Fecha: 30 de Septiembre 2022

# ## Introducción a la Transferencia de Calor
# A nivel molecular, los átomos que compomen la materia siempre está vibrando. La magnitud de estas vibraciones está caracterizada estadísticamente por la temperatura:

# <img src="./images/temperature_brownian_motion.gif" width="400px" align= center>

# Consideremos un sólido extendido con una diferencia de temperatura, $\Delta T$, entre sus extremos, tal que el lado izquierdo tiene una mayor temperatura que el lado derecho

# <img src="./images/heat_transfer.gif" width="300px" align= center>

# Debido a la diferencia de temperatura, la vibración molecular en el lado izquierdo es mayor. Esta energía cinética es transmitida a través del material hacia el lado derecho.

# Definimos como **calor**, $Q$, a la energía térmica intercambiada entre dos medios cuya diferencia de temperatura es $\Delta T$. A mayor $\Delta T$, mayor es el intercambio de calor, matematicamente: 
# 
# \begin{equation*}
# Q \propto \Delta T,\quad\mathrm{J}
# \end{equation*}
# 
# 

# La **taza de transferencia de calor**:
# \begin{equation*}
# \dot{Q} = \frac{dQ}{dt},\quad\mathrm{W}
# \end{equation*}
# 
# corresponde al calor tranferido por unidad de tiempo.

# Por último, definimos como **flujo de calor**: 
# \begin{equation*}
# q'' = \dot{Q}/A,\quad\frac{\mathrm{W}}{\mathrm{m}^2}
# \end{equation*}
# a la taza de transferencia de calor por unidad de área.

# Existen tres mecanismo de transferencia de calor:
# 
# - Conducción de calor
# - Convección de calor
# - Radiación

# <img src="./images/heat_transfer_mechanism.png" width="500px" align= center>

# ### Conducción de Calor
# **Definimos como *conducción de calor* al calor transferido a través de un material en reposo**. El mecanismo generalmente se asocia a **sólidos**, donde el calor es transferido a travéz de la red atómica del material. Sin embargo, la definición también incluye **líquidos y gases en reposo.** En este caso, las moléculas se mueven eleatoriamente, de manera tal que la velocidad neta del fluido es cero.

# Matemáticamente, para un material de espesor $t$ y diferencia de temperatura $\Delta T$, la **taza de transferencia de calor por conducción** a través de una superficie $A$, es:
# 
# <img src="./images/heat_conduction_formula.png" width="700px" align= center>

# La conductividad térmica, $k_c$, es una propiedad del material que varía según la temperatura.
# 
# <img src="./images/thermal_conductivity.png" width="800px" align= center>

# En su forma diferencial, $\dot{Q}_\mathrm{cond}= - k\nabla T$, y para el caso unidimensional:
# 
# \begin{equation}
# \dot{Q}_\mathrm{cond} = - kA\frac{dT}{dx},\quad\mathrm{W}
# \end{equation}

# A partir de esta fórmula podemos deducir expresiones para taza de transferencia de calor por conducción según la geometría:

# <img src="./images/heat_conduction_resistance.png" width="600px" align= center>

# Notar que, como fórmula general, podemos expresar la taza de conducción de calor en la forma:
# 
# \begin{equation*}
# \dot{Q}_\mathrm{cond} = \frac{T_H - T_C}{R_\mathrm{cond}},\quad\mathrm{W}
# \end{equation*}
# 
# donde, $R_\mathrm{cond}$ (K/W) es la **resistencia térmica** asociada al mecanismo de conducción.

# ### Convección de Calor
# **Definimos como *convección de calor* al calor transferido a través de fluidos en movimiento.** El movimiento de un fluido puede ocurrir naturalmente, debido a los efectos de flotación a raíz de los cambio de densidad con la temperatura; o de forma inducida, como por ejemplo mediante un ventilador.

# A partir de esto, clasificamos la transferencia de calor por convección, respectivamente, como:
# - **convección natural**
# - **convección forzada**.

# <img src="./images/heat_convection_mechanism.png" width="300px" align= center>

# La convección de calor esta asociada al contacto de fluidos con una superficie, $A$. Así, independiente del mecanismo de convección de calor (natural o forzada), expresamos la **taza de transferencia de calor por convección** como:
# 
# <img src="./images/heat_convection_formula.png" width="700px" align= center>

# Notar que la taza de transferencia de calor por convección puede ser expresada en la forma:
# 
# \begin{equation*}
# \dot{Q}_\mathrm{conv} = \frac{T_\infty - T}{R_\mathrm{conv}},\quad\mathrm{W}
# \end{equation*}
# 
# donde $R_\mathrm{conv}=1/hA$ es la resistencia térmica asociada a la convección de calor.

# A diferencia de la conducción de calor, el coeficiente convectivo, $h$, **no es una propiedad del fluido**. Esto porque no solo depende de las propiedades del fluido (densidad, viscocidad y conductividad térmica, entre otras), sino que además depende de condiciones externas, como la velocidad del flujo, la diferencia de temperaturas, y la geometría del cuerpó sometido a conveccción de calor.

# El coeficiente convectivo se determina a partir de relaciones expresadas en términos del número de Nusselt, $\mathrm{Nu} = \frac{hL_c}{k_f}$, donde $L_c$ es una longitud característica y $k_f$ es la conductividad térmica del fluido. En la mayoría de los casos, las relaciones para el número de Nusselt para cada caso se determinan experimentalmente.

# Comúnmente, los valores para el número de Nusselt se encuentran dentro de los siguientes rangos:
# 
# - Convección forzada, $\mathrm{Nu} \sim 5 - 1000 $
# - Convección natural, $\mathrm{Nu} \sim 0 - 100$

# ### Transferencia de calor en estado estacionario
# 
# En estado estacionario, el flujo de calor es constante. En este caso, podemos simplificar el análisis de transferencia de calor por convección y conducción utilizando resistencias térmicas.
# 
# <img src="./images/stationary_heat_transfer.png" width="700px" align= center>

# ## Fundamentos de la radiación térmica
# 
# Las vibraciones a nivel molecular también inducen polarización en la materia. Esto es similar al fenómeno de polarización inducida por ondas electromagnéticas estudiada en la unidad 3. Estos dipolos inducidos térmicamente, oscilan constantemente generando campos electromagnéticos que se propagan en dirección radial.
# 
# <img src="./images/radiating_dipole.png" width="700px" align= center>

# En la siguiente animación podemos ver el proceso de emisión de ondas electromagnéticas por un dipolo oscilatorio. El mapa de colores representa la intensidad del campo magnético, es decir $|\vec{H}|$, donde rojo y azul corresponden, respectivamente, a los valorse máximos y mínimos.
# 
# <img src="./images/HW_vertical_noground.gif" width="300px" align= center>

# ### Poder de emisión
# Un cuerpo a temperatura $T$ emite ondas electromagnéticas en todas las direcciones y en un rango de longitudes de onda. En general, la distribución angular ($\Omega$) y espectral ($\lambda$) de la radiación emitida depende de las propiedades ópticas de la superficie y la temperatura del material. 

# Para caracterizar la intensidad de la radiación emitida por una superficie a tempertura $T$, usamos la **intensidad específica o radiancia espectral**, $I_\lambda(\lambda,\Omega,T)$.

# La taza de calor total emitido por una superficie $dA$ de un cuerpo negro en función de $\lambda$ y $\Omega$, $d\dot{Q}_\mathrm{rad}$, está dada por:
# 
# \begin{equation}
# d\dot{Q}_\mathrm{rad} = I_{\lambda}(\lambda,T,\theta,\phi) \sin\theta \cos\theta dA d\Omega d\lambda
# \end{equation}

# El término $\cos\theta dA$ corresponde a la proyección de $dA$ en la dirección $\Omega$
# 
# <img src="./images/specific_intensity.png" width="300px" align= center>

# Definimos como **poder de emisión** direccional y espectral a la relación:
# 
# \begin{equation}
# E_{\lambda,\Omega}(T) = \frac{d\dot{Q}_\mathrm{rad}}{dAd\Omega d\lambda}=I_{\lambda}(\lambda,\Omega)\cos\theta ,\quad\quad\frac{\mathrm{W}}{\mathrm{m}^2\cdot\mu\mathrm{m}\cdot\mathrm{sr}}
# \end{equation}

# A diferencia de la intensidad específica, el poder de emisión considera la radiación effectiva emitida por una superficie.

# <img src="./images/emissive_power.png" width="500px" align= center>

# A partir de este término podemos derivar:

# - **Poder de emisión hemisférica espectral**, 
# \begin{equation*}
# E_{\lambda}(T) = \frac{d\dot{Q}}{dAd\lambda}=  \int_\mathrm{hemi}I_{\lambda}(\lambda,\Omega)\cos\theta d\Omega,\quad\quad\frac{\mathrm{W}}{\mathrm{m}^2\cdot\mu\mathrm{m}}
# \end{equation*}
# donde $\int_\mathrm{hemi} d\Omega = \int_0^{2\pi}d\phi\int_0^{\pi/2}\sin\theta d\theta$

# - **Poder de emisión**, 
# \begin{equation*}
# E(T) = \frac{d\dot{Q}}{dA}=\int_0^\infty\int_\mathrm{hemi}I_{\lambda}(\lambda,\Omega)\cos\theta d\Omega d\lambda ,\quad\quad\frac{\mathrm{W}}{\mathrm{m}^2}
# \end{equation*}

# ### Distribución de Planck
# 
# Max Planck en 1901 determinó que la **máxima radiancia espectral o intensidad específica** (flujo de energía por unidad de longitud de onda y ángulo sólido) emitida por un cuerpo a temperatura $T$, en un medio con índice de refracción $n_1$, está dada por:
# 
# \begin{equation}
# I_{\mathrm{bb},\lambda}(\lambda,T,\Omega) = \frac{C_1}{n_1\lambda^5\left[\exp\left(C_2/\lambda T\right) - 1\right]},\quad\quad\frac{\mathrm{W}}{\mathrm{m}^2\cdot\mu\mathrm{m}\cdot\mathrm{sr}}
# \end{equation}
# 
# donde 
# \begin{align*}
# C_1 &= 2hc_0^2 = 1.19104238\times 10^8 ~\mathrm{W}\cdot\mu\mathrm{m}^4/\mathrm{m}^2 \\
# C_2 &= hc_0/k_\mathrm{B} = 1.43878\times10^{4}~\mu\mathrm{m}\cdot\mathrm{K}
# \end{align*}
# 
# $k_\mathrm{B} = 1.381\times 10^{-23}$ J/K $=8.617\times 10^{-5}$ eV/K, es la constante de Boltzmann. La unidad "sr" correponde a un esteroradian.

# Esta es la **distribución de Planck**. Representa la radiancia espectral emitida por un cuerpo idealizado, denominado **cuerpo negro**. Un cuerpo negro, así, representa un emisor perfecto, capaz de emitir la máxima radiacion posible a una temperatura $T$.

# El poder de emisión espectral de la superficie de un cuerpo negro, $E_\mathrm{bb}(\lambda,T)$, se obtiene integrando la radiancia espectral por ángulo sólido en el límite de una hemiesfera:
# 
# \begin{equation}
# \int_\mathrm{hemi} I_{\mathrm{bb},\lambda}(\lambda,T,\Omega)\cos\theta d\Omega = \pi I_{\mathrm{bb},\lambda}(\lambda,T) = E_\mathrm{bb}(\lambda,T),\quad\quad\frac{\mathrm{W}}{\mathrm{m}^2\cdot\mu\mathrm{m}}
# \end{equation}
# 
# donde $\int_\mathrm{hemi} d\Omega = \int_0^{2\pi}d\phi\int_0^{\pi/2}d\theta$

# A partir de la integral de $E_\mathrm{bb}(\lambda,T)$ en el espectro de longitudes de onda, obtenemos el flujo de radiación emitida o el poder de emisión de un cuerpo negro:
# 
# \begin{equation}
# \int_0^\infty E_\mathrm{bb}(\lambda,T) d\lambda = \sigma T^4,\quad\quad\frac{\mathrm{W}}{\mathrm{m}^2}
# \end{equation}
# 
# donde $\sigma = 5.670\times10^{-8}$ W/m$^2\cdot$K$^4$, es la *constante de Stefan-Boltzmann.* Esta fórmula se conoce como la **ley de Stefan-Boltzmann**

# En la siguiente figura, se ilustra $E_\mathrm{bb}(\lambda,T)$ función de la temperatura y longitud de onda.
# 
# <img src="./images/blackbody_rad.png" width="700px" align= center>

# A medida que $T$ aumenta, notamos que el máximo de la curva se desplaza hacia el azul. La longitud de onda correspondiente a este máximo, $\lambda_\mathrm{peak}$, está definida por la **ley de desplazamiento de Wien:**
# 
# \begin{equation}
# \lambda_\mathrm{peak}T = 2897.8\quad\mu\mathrm{m}\cdot\mathrm{K}
# \end{equation}
# 

# Esta relación permite entender el cambio de color de la fuente emisora con la tempertura. Sin embargo, **el color de un material no solo se define por la emisión de radiación, sino también por la forma en la que interactúa con la luz incidente**. Como revisamos en las unidades anteriores, esta interacción está condionada por las propiedades radiativas.

# ### Propiedades Radiativas
# 
# Definimos como **emisividad, $\epsilon$** a la *razón entre la radiación emitida por una superficie, $I_\lambda(\lambda,T,\Omega)$, y la radiación emitida por un cuerpo negro, ambas a temperatura $T$*:
# 
# \begin{equation}
# \epsilon(\lambda,\Omega) = \frac{I_\lambda(\lambda,T,\Omega)}{I_{\mathrm{bb},\lambda}(\lambda,T,\Omega)}
# \end{equation}
# 
# De esta forma, $\epsilon$ es una propiedad adimensional de superfice que varía entre $0 \le \epsilon \le 1$.

# La **ley de Kirchhoff**, establece que la abortividad, $\alpha$ y la emisividad están relacionadas por:
# 
# \begin{equation}
# \epsilon(\lambda,\Omega) = \alpha(\lambda,\Omega)
# \end{equation}
# 

# A partir de estas relacion podemos relacionar las propiedades de reflectividad, $R$ y transmisividad $T$ para determinar $\epsilon$.

# Debido a la naturaleza de la radiación térmica, la polarización de las ondas electromagnéticas es aleatoria. Así, $R$ y $T$ se calculan como:
# 
# \begin{equation}
# R = \frac{R_\mathrm{TM}+R_\mathrm{TE}}{2}\quad\quad
# T = \frac{T_\mathrm{TM}+T_\mathrm{TE}}{2}
# \end{equation}

# Cabe mencionar que en radiometría, la reflectividad y transmisividad se denominan, respectivamente, **reflectancia ($\rho$)**, **transmitancia ($\tau$).** Igualmente la absortividad se denomina **absortancia.** Ambos términos son equivalentes.

# Por la ley de conservación de energía, la reflectancia, transmitancia y absortancia se relacionan por:
# 
# \begin{equation}
# 1 = \alpha(\lambda,\Omega) + \rho(\lambda,\Omega) + \tau(\lambda,\Omega)
# \end{equation}

# Como ejemplo, analicemos el poder de emisión espectral direccional, $E_{\lambda,\Omega}(T)$ y la emisividad $\epsilon(\lambda,\Omega)$ de una capa de vidrio en función de la temperatura, espesor y dirección. En este caso: 
# 
# \begin{align*}
# E_{\lambda,\Omega}(T) &= \epsilon(\lambda,\Omega)I_{\mathrm{bb},\lambda}(\lambda,\Omega,T)\cos\theta \\
#  &= \left[1 - \rho(\lambda,\Omega) - \tau(\lambda,\Omega)\right]I_{\mathrm{bb},\lambda}(\lambda,\Omega,T)\cos\theta
# \end{align*}

# Comparamos $E_{\lambda,\Omega}(T)$ con el poder de emisión espectral direccional del cuerpo negro, $E_\mathrm{bb}(\lambda,\Omega,T)$

# In[1]:


import empylib.waveoptics as wv
import empylib.nklib as nk
import numpy as np
from numpy import log10, radians
import matplotlib.pyplot as plt
from empylib.ref_spectra import Bplanck

def plot_emisivity_glass(Temp,d,lam0,theta0):
    # parámetros de entrada
    
    lam = np.linspace(0.3,15,100)
    Nfront = 1.0                 # índice de refracción medio superior
    N1     = nk.SiO2(lam)        # índice de refracción capa intermedia
    Nback  = 4.3                 # índice de refracción medio inferior
    N = (Nfront, N1, Nback)      # indices de refracción (above, mid, below)

    # Reflectancia y transmitancia espectral en theta0
    Rs, Ts = wv.incoh_multilayer(lam,radians(theta0), N, d*1E3, pol='TM')
    Rp, Tp = wv.incoh_multilayer(lam,radians(theta0), N, d*1E3, pol='TM')
    
    R_lam = (Rs + Rp)/2
    T_lam = (Ts + Tp)/2
    A_lam = 1 - T_lam - R_lam
    
   # Reflectancia y transmitancia direccional en lam0
    theta = np.linspace(0,90,100)
    N = (Nfront, np.interp(lam0,lam,N1), Nback)      # indices de refracción (above, mid, below)
    A_theta = [] # lista vacía
    for theta_i in theta:
        Rs, Ts = wv.incoh_multilayer(lam0,radians(theta_i), N, d*1E3, pol='TM')
        Rp, Tp = wv.incoh_multilayer(lam0,radians(theta_i), N, d*1E3, pol='TM')
        R = (Rs + Rp)/2
        T = (Ts + Tp)/2
        A_theta.append(1 - T - R)
    A_theta = np.array(A_theta).flatten() # convertimos la lista a ndarray

    fig, ax = plt.subplots(1,3)
    fig.set_size_inches(18, 5)
    plt.rcParams['font.size'] = '18'
    
    # graficamos las propiedades radiativas espectrales
    ax[0].plot(lam,R_lam,'--r',label=r'$\rho$',linewidth=0.5)
    ax[0].plot(lam,T_lam,'--b',label=r'$\tau$',linewidth=0.5)
    ax[0].plot(lam,A_lam,'-k',label=r'$\alpha$',linewidth=2.0)  
    ax[0].plot(lam0,np.interp(lam0,lam,A_lam),'ok')   
    ax[0].set_xlabel('$\lambda$ ($\mu$m)')
    ax[0].set_ylabel(r'$\rho$, $\tau$ y $\alpha$')
    ax[0].set_ylim(0,1.05)
    ax[0].set_title(r'$\theta = $ %i°' % theta0)
    ax[0].legend()
    
    # graficamos la emisividad espectral en el ángulo
    ax[1].plot(theta,A_theta,'-k')  
    ax[1].plot(theta0,np.interp(theta0,theta,A_theta),'ok')   
    ax[1].set_xlabel(r'$\theta$ (deg)')
    ax[1].set_ylabel(r'$\epsilon(\lambda,\theta)$')
    ax[1].set_title(r'$\lambda = $ %.2f $\mu$m' % lam0)
    ax[1].set_ylim(0,1.05)
    
    # Graficamos la radiación espectral
    ax[2].plot(lam,A_lam*Bplanck(lam,Temp)*np.cos(np.radians(theta0)),'-k',label =r'$E_{\lambda,\Omega}$')
    ax[2].plot(lam,Bplanck(lam,Temp)*np.cos(np.radians(theta0)),'-r',label =r'$E_\mathrm{bb}$')
    ax[2].set_xlabel('Longitud de onda ($\mu$m)')
    ax[2].set_ylabel(r'E_{\lambda,\Omega}(T) (W/m$^2$-$\mu$m-sr)')
    ax[2].set_title(r'd = %.2f mm, $\theta$=%i°' % (d,theta0) )
    ax[2].set_ylim(0,max(Bplanck(lam,Temp))*1.05)
    ax[2].legend()
    
    plt.subplots_adjust(wspace=0.35)
    plt.show()


# In[2]:


from ipywidgets import interact

@interact(T=(300,1000,10), d=(0,10,0.01), lam0=(5,10,0.01), theta0=(0,90,1))
def g(T=300,d=1, lam0=10, theta0=0):
   return plot_emisivity_glass(T,d,lam0,theta0)


# Decimos que una superficie es **difusa** cuando sus propiedades radiativas no dependen de $\Omega$. Si la superficie es difusa, una buena aproximación es considerar el valor de la propiedad difusa como la propiedad radiativa de la superficie lisa en la dirección normal. Por ejemplo, para la emisividad: $\epsilon(\lambda,T) = \epsilon(\lambda,\Omega = 0, T)$

# Decimos que una superficie es **opaca** cuando $\tau = 0$. En este caso, 
# tenemos $\alpha + \rho = 1$

# Para gases, $\rho \approx 0$, así $\alpha + \tau = 1$

# ### Irradiancia (G) y Radiosidad (J)

# Definimos como **irradiación (G)** a la radiancia espectral incidente en una superficie.
# <img src="./images/irradiance.png" width="300px" align= center>

# Definimos como **radiosidad (J)** a la combinación de radiación emitida y reflejada por una superficie
# <img src="./images/radiosity.png" width="250px" align= center>

# ## Referencias
# - Çengel Y. A y Ghanjar A. J. **Capítulo 12 - Fundamentos de la radiación térmica** en *Transferencia de calor y masa*, 4ta Ed, McGraw Hill, 2011

# In[3]:


from IPython.display import YouTubeVideo
YouTubeVideo('FDmYCI_xYlA', width=600, height=400,  playsinline=0)

