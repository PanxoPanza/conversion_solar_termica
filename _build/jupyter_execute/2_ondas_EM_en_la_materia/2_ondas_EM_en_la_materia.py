#!/usr/bin/env python
# coding: utf-8

#  <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # 2. Ondas electromagnéticas en la materia
# <br><br><br><br>
# Profesor: Francisco Ramírez CueSvas<br>
# Fecha: 19 de Agosto 2022

# <h1>Tabla de contenidos<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Ecuaciones-de-Maxwell-en-un-medio" data-toc-modified-id="Ecuaciones-de-Maxwell-en-un-medio-1">Ecuaciones de Maxwell en un medio</a></span><ul class="toc-item"><li><span><a href="#Vector-de-Poynting" data-toc-modified-id="Vector-de-Poynting-1.1">Vector de Poynting</a></span></li><li><span><a href="#Condiciones-de-borde" data-toc-modified-id="Condiciones-de-borde-1.2">Condiciones de borde</a></span></li></ul></li><li><span><a href="#Reflección-y-transmissión-de-ondas-electromagnéticas-en-una-interface" data-toc-modified-id="Reflección-y-transmissión-de-ondas-electromagnéticas-en-una-interface-2">Reflección y transmissión de ondas electromagnéticas en una interface</a></span><ul class="toc-item"><li><span><a href="#Coeficientes-de-Fresnel" data-toc-modified-id="Coeficientes-de-Fresnel-2.1">Coeficientes de Fresnel</a></span></li><li><span><a href="#Reflectividad-($R$)-y-transmisividad-($T$)" data-toc-modified-id="Reflectividad-($R$)-y-transmisividad-($T$)-2.2">Reflectividad ($R$) y transmisividad ($T$)</a></span></li><li><span><a href="#Casos-particulares" data-toc-modified-id="Casos-particulares-2.3">Casos particulares</a></span></li></ul></li><li><span><a href="#Reflección-y-transmissión-en-películas-delgadas" data-toc-modified-id="Reflección-y-transmissión-en-películas-delgadas-3">Reflección y transmissión en películas delgadas</a></span></li><li><span><a href="#Referencias" data-toc-modified-id="Referencias-4">Referencias</a></span></li></ul></div>

# ## Ecuaciones de Maxwell en un medio

# La materia esta compuesta por cargas (electrónes, átomos, moléculas). Por lo tanto, a diferencia del vacío, la densidad de carga ($\rho$) y de corriente ($\vec{J}$) eléctricas están presentes en las ecuaciones de Maxwell:
# 
# \begin{align*}
# \nabla\cdot\vec{E} &= \frac{\rho}{\varepsilon_0} \\
# \nabla\cdot\vec{B} &= 0 \\
# \nabla\times\vec{E} &= -\mu_0\frac{\partial \vec{H}}{\partial t} \\
# \nabla\times\vec{H} &= \vec{J} + \varepsilon_0\frac{\partial \vec{E}}{\partial t}
# \end{align*}

# > En general, existe un tercer término asociado con la polarización magnética del material. Sin embargo, en este curso veremos solo materiales paramagnéticos y, por lo tanto, este término será ignorado. 

# Asumiendo un medio homogéneo, y mediante la relación:
# 
# \begin{equation}
# \vec{D} = \varepsilon_0\varepsilon\vec{E}
# \end{equation}
# 
# donde $\vec{D}$ es el desplazamiento eléctrico, y $\varepsilon = \varepsilon' + i\varepsilon''$, es la **constante dieléctrica** compleja; 
# 
# podemos demostrar que las ecuaciones de Maxwell se pueden reescribir en la forma:
# 
# \begin{align*}
# \nabla\cdot\vec{E} &= 0 \\
# \nabla\cdot\vec{H} &= 0 \\
# \nabla\times\vec{E} &= -\mu_0\frac{\partial \vec{H}}{\partial t} \\
# \nabla\times\vec{H} &= \varepsilon_0 \varepsilon\frac{\partial\vec{E}}{\partial t}
# \end{align*}

# Estas ecuaciones tiene la misma forma que las ecuaciones de Maxwell en el vacío, y por lo tanto todas las conclusiones anteriores aplican a este caso.

# La gran diferencia está en la relación de dispersión. En este caso:
# 
# \begin{equation}
# k = N \frac{\omega}{c_0}
# \end{equation}
# 
# donde $N = \sqrt{\varepsilon} = n +i\kappa$, es el **índice de refracción complejo**. En general $n$ se conoce como el **índice de refracción**, y $\kappa$ como **extinsión**.

# > Notar que la velocidad de la onda también cambia a $c = c_0/n$

# Igualmente la relación entre $H_0$ y $E_0$, es de la forma 
# 
# $$H_0 = \frac{E_0}{Z_0Z_r},$$
# 
# donde $Z_r = \sqrt{\frac{1}{\varepsilon}}$ es la **impedancia relativa**.

# >Notar que para materiales paramagnéticos, 
# >
# > \begin{equation*}Z_r = \sqrt{\frac{1}{\varepsilon}} = \frac{1}{N}\end{equation*}

# **¿Qué representa la constante dielectrica compleja?**

# Los materiales están compuestos de átomos, con un núcleo positivo y electrones negativos. Estos electrones interactúan con los átomos de distintas formas; algunos orbitan alrededor del núcleo mientras que otros se mueven libremente por el material. Así, podemos separar las cargas eléctricas en dos tipos: **cargas ligadas**, y **cargas libres**.
# 
# <img src="./images/atomic_lattice.png" width="400px" align= center>

# La interacción de las onda electromagnéticas con las cargas ligadas induce **polarización**, es decir, el nucleo y el electrón se polarizan, oscilando en sincronía con el campo externo. Esta respuesta está representada por la parte real de la constante dielectrica ($\varepsilon'$).

# <img src="./images/constante_dielectrica.png" width="550px" align= center>

# Las ondas electromagnéticas aceleran las cargas libres, generando **corrientes eléctricas inducidas**. Algunas cargas libres móbiles colicionan con otros electrónes o núcleos, disipando energía. Esta respuesta está representada por la parte imaginaria de la constante dieléctrica ($\varepsilon''$).

# Esta discipación de energía está representada por la resistencia eléctrica, y es la reponsable de la generación de calor en metaeles. 
# 
# De hecho, la conductividad eléctrica $\sigma$ en la ley de Ohm, $\vec{J} = \sigma\vec{E}$, está relacionada con la parte imaginaria de la constante dielectrica por:
# \begin{equation}
# \sigma = \varepsilon_0\omega\varepsilon''
# \end{equation}

# <img src="./images/light_bulb.jpg" width="300px" align= center>

# **¿Que significa que el vector de onda sea complejo?**

# Analicemos la solución general de la ecuación de onda:
# 
# \begin{align*}
# \vec{E} &= E_0 e^{i\left(\vec{k}\cdot\vec{r} - \omega t\right)} \hat{e} \\
# &= E_0 e^{i\left(Nk_0\hat{k}\cdot\vec{r} - \omega t\right)} \hat{e} \\
# &= E_0 e^{i\left(nk_0\hat{k}\cdot\vec{r} - \omega t\right)}e^{-\kappa k_0\left(\hat{k}\cdot\vec{r}\right)} \hat{e}
# \end{align*}

# <img src="./images/decaying_wave.png" width="300px" align= center>
# 
# Lo que notamos es, mientas que el índice de refracción $n$ representa el **cambio en la oscilación espacial de la onda**, la extinsión $\kappa$ indica un **decaimiento en la amplitud**.

# En resumen, en materiales paramagnéticos:
# 1. $\vec{E}$ y $\vec{H}$ se comportan como ondas trasversales de la forma $\propto e^{ i\left(\vec{k}\cdot\vec{r} - \omega t\right)}$.
# 
# 2. La relación de dispersión esta dada por $k = N\frac{\omega}{c_0},$ 
# donde $N = n + i\kappa$ es el índice de refracción complejo.
# 
# 4. $N =\sqrt{\varepsilon} =\sqrt{\varepsilon'+i\varepsilon''}$, donde $\varepsilon$ es la constante dieléctrica
# 
# 3. $\vec{E}$ y $\vec{H}$ se propagan a una velocidad constante $c = c_0/n$
# 
# 4. $\kappa$ representa la extinsión de la onda en el espacio.
# 
# 5. $\vec{E}$, $\vec{H}$ y $\vec{k}$ son mutuamente perpendiculares. 
# 
# 6. Las amplitudes de $\vec{E}$ y $\vec{H}$ están asociadas por la relación ${H}_0 = \frac{E_0}{Z_0Z_r}$, donde $Z_r = \frac{1}{\sqrt{\varepsilon}}$.

# <img src="./images/em_wave_decaying.jpg" width="400px" align= center>
# 
# <center> Esquema de una onda electromagnética en un material</center>

# ### Vector de Poynting
# El vector de Poynting, $\vec{S}$, representa el flujo de energía electromagnética por unidad de área. Está dado por la relación:
# 
# \begin{equation}
# \langle\vec{S}\rangle = \frac{1}{2}\mathrm{Re}\left(\vec{E}\times\vec{H}^*\right),
# \end{equation}
# 
# donde $\langle\cdots\rangle$ reprensenta el promedio en un periodo, y $^*$ reprenta el complejo conjugado.

# Consideremos, por ejemplo, el vector de Poynting para una onda plana que se propaga en un material con índice de refracción $N = n+i\kappa$:
# 
# \begin{align*}
# \langle\vec{S}\rangle &= \frac{1}{2}\mathrm{Re}\left[\vec{E}\times\vec{H}^*\right] \\
# &=\frac{1}{2}\mathrm{Re}\left[E_0 e^{i\left(\vec{k}\cdot\vec{r} - \omega t\right)}H_0^* e^{-i\left(\vec{k}^*\cdot\vec{r} - \omega t\right)}\left(\hat{e}\times\hat{h}\right)\right] \\
# &=\frac{1}{2}\mathrm{Re}\left[\frac{E_0^2}{Z_0Z_r^*} e^{i\left(k_0N\hat{k}\cdot\vec{r} - \omega t\right)}e^{-i\left(k_0N^*\hat{k}\cdot\vec{r} - \omega t\right)} \hat{k}\right] \\
# &=\frac{1}{2}\mathrm{Re}\left[\frac{E_0^2}{Z_0Z_r^*}  \hat{k}\right]e^{-2k_0\kappa\left(\hat{k}\cdot\vec{r}\right)} \\
# &=\mathrm{Re}\left[N^*\hat{k}\right]\frac{E_0^2}{2Z_0}e^{-\alpha\left(\hat{k}\cdot\vec{r}\right)}
# \end{align*}

# El término $\alpha = \frac{4\pi\kappa}{\lambda}$ es el **coeficiente de absorpción**. El inverso, $\delta = 1/\alpha$, se denomina **profundidad superficial** y representa la profundidad de penetración de la onda electromagnética en un material. 

# Como referencia, $\delta\sim 1000$ m en fibras ópticas a $\lambda = 1.55$ $\mu$m, que es la longitud de onda utilizada en comunicación óptica. Por otro lado, en metales como la plata, oro o aluminio, $\delta\sim 10$ nm para $\lambda \sim 500$ nm (espectro de luz visible)

# ### Condiciones de borde

# Hasta ahora hemos revisado las ecuaciones de Maxwell en un medio homogeneo, y como estas dan lugar a la solución en forma de ondas electromagnéticas.
# 
# > Recordemos que para un medio con índice de refracción $N$, la solución general es:
# >
# >\begin{align*}
# \vec{E} &= E_0 e^{i\left(Nk_0\hat{k}\cdot\vec{r} - \omega t\right)} \hat{e} \\
# \vec{H} &= \frac{NE_0}{Z_0} e^{i\left(Nk_0\hat{k}\cdot\vec{r} - \omega t\right)} \hat{k}\times\hat{e}
# \end{align*}

# **¿Que sucede cuando una onda electromagnética encuentra la frontera entre dos medios distintos?**

# Como toda ecuación diferencial, la solución particular de las ecuaciones de Maxwell está definida por las condiciones de borde. Estas condiciones de borde surgen al aplicar las ecuaciones de Maxwell en una frontera (cuya derivación no revisaremos aqui). En general son 4 condiciones de borde. Sin embargo, para los problemas que veremos en este curso solo se necesitan dos:
# 
# \begin{align}
# E^{\parallel}_1 - E^{\parallel}_2 &= 0 \\
# H^{\parallel}_1 - H^{\parallel}_2 &= 0
# \end{align}
# 
# donde $1$ y $2$ son dos medios distintos, y el símbolo $\parallel$ representa la componente paralela a la interface entre los medios $1$ y $2$

# >**En la interface entre dos medios $1$ y $2$ las componentes de $\vec{E}$ y $\vec{H}$ paralelas a la interface, se conservan.**

# ## Reflección y transmissión de ondas electromagnéticas en una interface

# ### Coeficientes de Fresnel

# Consideremos el fenómeno de reflección y transmissión de una onda electromagnetética en dirección $\hat{k}_i$ que incide sobre la interface entre dos medios 1 y 2, con índices de refracción reales $n_1$ y $n_2$, respectivamente
# 
# Definimos como $\hat{n}$ al vector normal al plano de interface entre los dos medios, y como **plano de incidencia,** al plano formado por los vectores $\hat{k}_i$ y $\hat{n}$.
# 
# La dirección de la onda reflejada y transmitida está definida por los vectores $\hat{k}_r$ y $\hat{k}_t$, respectivamente.

# <img src="./images/plano_incidencia.png" width="350px" align= center>

# Como ejemplo, consideremos una onda electromagnética donde el campo magnético está **polarizado** en dirección perpendicular al plano de incidencia. Este tipo de onda se define como **onda transversal magnética (TM)**
# 
# <img src="./images/em_reflection.png" width="350px" align= center>

# A través de las ecuaciones de Maxwell, podemos establecer la solución general para cada onda electromagnética:
# 
# \begin{align*}
# \vec{E}_i &= E_i e^{ i\left(k_0n_1\hat{k}_i\cdot\vec{r} - \omega t\right)} \hat{e}_i\quad\quad \mathrm{onda~incidente}
#  \\
# \vec{E}_r &= E_r e^{ i\left(k_0n_1\hat{k}_r\cdot\vec{r} - \omega t\right)} \hat{e}_r\quad\quad \mathrm{onda~reflejada}
# \\
# \vec{E}_t &= E_t e^{ i\left(k_0n_2\hat{k}_t\cdot\vec{r} - \omega t\right)} \hat{e}_t\quad\quad 
# \mathrm{onda~transmitida}
# \end{align*}
# 
# donde:
# 
# \begin{eqnarray*}
# \hat{k}_i &=& \hat{x}\sin\theta_i + \hat{z}\cos\theta_i 
# &\quad\mathrm{y}\quad& 
# \hat{e}_i &=& \hat{x}\cos\theta_i - \hat{z}\sin\theta_i
# \\
# \hat{k}_r &=& \hat{x}\sin\theta_r - \hat{z}\cos\theta_r
# &\quad\mathrm{y}\quad& 
# \hat{e}_r &=& \hat{x}\cos\theta_r + \hat{z}\sin\theta_r
# \\
# \hat{k}_t &=& \hat{x}\sin\theta_t + \hat{z}\cos\theta_t
# &\quad\mathrm{y}\quad& 
# \hat{e}_t &=& \hat{x}\cos\theta_t - \hat{z}\sin\theta_t
# \end{eqnarray*}

# Reemplazando en las soluciones generales,
# 
# \begin{eqnarray*}
# \vec{E}_i &=& E_i e^{ ik_0n_1\left(z\cos\theta_i + x\sin\theta_i\right)}e^{-i\omega t} \left(\hat{x}\cos\theta_i -\hat{z}\sin\theta_i\right)\quad\quad &&\mathrm{onda~incidente}
#  \\
# \vec{E}_r &=& E_r e^{ ik_0n_1\left(-z\cos\theta_r + x\sin\theta_r\right)}e^{-i\omega t} \left(\hat{x}\cos\theta_r +\hat{z}\sin\theta_r\right)\quad\quad &&\mathrm{onda~reflejada}
# \\
# \vec{E}_t &=& E_t e^{ ik_0n_2\left(z\cos\theta_t + x\sin\theta_t\right)}e^{-i\omega t} \left(\hat{x}\cos\theta_t -\hat{z}\sin\theta_t\right)\quad\quad 
# &&\mathrm{onda~transmitida}
# \end{eqnarray*}

# De igual forma, a partir de la relación $\vec{H} = \frac{E}{Z_0Z_r}\left(\hat{k}\times\hat{e}\right)$,
# 
# \begin{eqnarray*}
# \vec{H}_i &=& \frac{n_1E_i}{Z_0}e^{ ik_0n_1\left(z\cos\theta_i + x\sin\theta_i\right)}e^{-i\omega t}\left(\hat{y}\right)\quad\quad &&\mathrm{onda~incidente}
#  \\
# \vec{H}_r &=& \frac{n_1E_r}{Z_0} e^{ ik_0n_1\left(-z\cos\theta_r + x\sin\theta_r\right)}e^{-i\omega t} \left(-\hat{y}\right)\quad\quad &&\mathrm{onda~reflejada}
# \\
# \vec{H}_t &=& \frac{n_2E_t}{Z_0} e^{ ik_0n_2\left(z\cos\theta_t + x\sin\theta_t\right)}e^{-i\omega t} \left(\hat{y}\right)\quad\quad 
# &&\mathrm{onda~transmitida}
# \end{eqnarray*}

# A partir de la condición de borde en la interface $z =0$:
# 
# $$E^{\parallel}_1|_{z=0} - E^{\parallel}_2|_{z=0} = 0$$

# Tenemos:
# 
# \begin{equation*}
# E_i\cos\theta_i e^{ ik_0n_1x\sin\theta_i}+E_r\cos\theta_r e^{ ik_0n_1x\sin\theta_r} - E_t\cos\theta_t e^{ ik_0n_1x\sin\theta_t} = 0
# \end{equation*}

# Dado que esta ecuación se debe satisfacer para cualquier punto $x$, los exponentes debe ser iguales:
# 
# \begin{equation*}
# n_1\sin\theta_i = n_1\sin\theta_r = n_2\sin\theta_t
# \end{equation*}

# Esto nos lleva a las leyes de Snell, para reflección y transmissión:
# 
# \begin{equation*}
# \theta_i = \theta_r\quad\quad\mathrm{y}\quad\quad n_1\sin\theta_i = n_2\sin\theta_t
# \end{equation*}

# Finalmente, la condición de borde del campo eléctrico queda:
# 
# \begin{equation}\label{eq:boundaryE}
# E_i\cos\theta_i +E_r\cos\theta_r  - E_t\cos\theta_t = 0
# \end{equation}

# De igual forma, de la condición de borde $H^{\parallel}_1 - H^{\parallel}_2 = 0$, deducimos:
# 
# \begin{equation}
# n_1E_i - n_1E_r  - n_2E_t = 0 \label{eq:boundaryH}
# \end{equation}

# A partir de las ecuaciones (\ref{eq:boundaryE}) y (\ref{eq:boundaryH}), determinamos los coeficientes de Fresnel de reflección ($r_\mathrm{TM}$) y transmissión ($t_\mathrm{TM}$) para una onda TM:
# 
# \begin{align}
# r_\mathrm{TM} &= \frac{E_r^\mathrm{TM}}{E_i^\mathrm{TM}} = \frac{n_1\cos\theta_t-n_2\cos\theta_i}
# {n_1\cos\theta_t+n_2\cos\theta_i}
# \\[10pt]
# t_\mathrm{TM} &= \frac{E_t^\mathrm{TM}}{E_i^\mathrm{TM}} =\frac{2n_1\cos\theta_t}
# {n_1\cos\theta_t+n_2\cos\theta_i}
# \end{align}

# Similarmente, para una onda transversal eléctrica (TE), los coeficientes de Fresnel son:
# 
# \begin{align}
# r_\mathrm{TE} &= \frac{E_r^\mathrm{TE}}{E_i^\mathrm{TE}} = \frac{n_1\cos\theta_i -n_2\cos\theta_t}
# {n_1\cos\theta_i+n_2\cos\theta_t}
# \\[10pt]
# t_\mathrm{TE} &= \frac{E_t^\mathrm{TE}}{E_i^\mathrm{TE}} = \frac{2n_1\cos\theta_i}
# {n_1\cos\theta_i+n_2\cos\theta_t}
# \end{align}

# >Las relaciones para los coeficientes de Fresnel se mantienen para índices de refracción complejos. En este caso, solo debemos reemplazar $n_1$ por $N_1$, y $n_2$ por $N_2$

# ### Reflectividad ($R$) y transmisividad ($T$)

# Los coeficientes de Fresnel permiten determinar la magnitud del campo eléctrico (y magnético) reflejado y transmitido por una interface. Para determinar el flujo de energía a través de la interface, utilizamos el vector de Poynting. En el caso de la onda $\mathrm{TM}$, y considerando indices de refracción complejos en los medios 1 y 2:
# 
# \begin{eqnarray*}
# \biggl\langle{\vec{S}_i^\mathrm{TM}}\biggl\rangle &=& \frac{1}{2}\mathrm{Re}\left[\vec{E}_i\times\vec{H}_i^*\right] &=& \mathrm{Re}\left[N_1^* \hat{k}_i\right]\frac{{\left(E_i^\mathrm{TM}\right)}^2}{2Z_0}
# \\
# \biggl\langle{\vec{S}_r^\mathrm{TM}}\biggl\rangle &=& \frac{1}{2}\mathrm{Re}\left[\vec{E}_r\times\vec{H}_r^*\right] &=& \mathrm{Re}\left[N_1^* \hat{k}_r\right]\frac{{\left(E_r^\mathrm{TM}\right)}^2}{2Z_0}
# \\
# \biggl\langle{\vec{S}_t^\mathrm{TM}}\biggl\rangle &=& \frac{1}{2}\mathrm{Re}\left[\vec{E}_t\times\vec{H}_t^*\right] &=& \mathrm{Re}\left[N_2^* \hat{k}_t\right]\frac{{\left(E_t^\mathrm{TM}\right)}^2}{2Z_0}
# \end{eqnarray*}

# La **reflectividad ($R$)** y **transmissivitdad ($T$)** se definen, repectivamente, como **el flujo de energía reflejada y transmitida relativa al flujo de energía incidente, y en dirección normal a la interface.** 

# Así, considerando la componente del vector de Poynting normal a $\hat{n}$ (notar que $\hat{n} = - \hat{z}$ en nuestro ejemplo), tenemos:
# 
# \begin{eqnarray}
# R_\mathrm{TM} &=& \frac{S_{r,z}^\mathrm{TM}}{S_{i,z}^\mathrm{TM}} &=& \lvert r_\mathrm{TM}\rvert^2
# \\[10pt]
# T_\mathrm{TM} &=& \frac{S_{t,z}^\mathrm{TM}}{S_{i,z}^\mathrm{TM}} &=& \frac{\mathrm{Re}\left(N_2^*\cos\theta_t\right)}{\mathrm{Re}\left(N_1^*\cos\theta_i\right)}\lvert t_\mathrm{TM}\rvert^2
# \end{eqnarray}

# De igual forma, para una onda TE, tenemos
# 
# \begin{eqnarray}
# R_\mathrm{TE} &=& \lvert r_\mathrm{TE}\rvert^2
# \\[10pt]
# T_\mathrm{TE} &=& \frac{\mathrm{Re}\left(N_2\cos\theta_t\right)}{\mathrm{Re}\left(N_1\cos\theta_i\right)}\lvert t_\mathrm{TE}\rvert^2
# \end{eqnarray}

# Notar que por conservación de energía:
# \begin{equation}
# R + T = 1
# \end{equation}

# ### Casos particulares

# Asumiendo dos medios 1 y 2, con índice de refracción real, analicemos la reflectancia en función del ángulo de incidencia:
# - caso 1, $n_1 < n_2$
# - caso 1, $n_1 > n_2$

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from empylib.fresnel import interface

theta = np.linspace(0,90,100) # Ángulo de incidencia
# Reflectividad en una interface
Rp = lambda n1,n2 : interface(theta,n1,n2)[0]
Rs = lambda n1,n2 : interface(theta,n1,n2)[4]

# preparamos el ploteo
def plot_R_interface(n1,n2):
    fig, ax = plt.subplots()
    fig.set_size_inches(9, 6)
    plt.rcParams['font.size'] = '16'
    ax.plot(theta,Rp(n1,n2), label='$R_\mathrm{TM}$', color='red')
    ax.plot(theta,Rs(n1,n2), label='$R_\mathrm{TE}$',color='blue')
    ax.set_xlim([0,90])
    ax.set_ylim([0,1.0])
    ax.set_xlabel('Ángulo de incidencia (°)')
    ax.set_ylabel('Reflectividad')
    ax.legend(frameon=False)


# In[2]:


from ipywidgets import interact

@interact(n1=(1,5, 0.1), n2=(1,5, 0.1))
def g(n1=1, n2=2.0):
    return plot_R_interface(n1,n2)


# Cuando $n_1 < n_2$ vemos que $R_\mathrm{TM} = 0$ en un cierto ángulo. Este ángulo se denomina **ángulo de Brewster.** En este ángulo solo la componente TE es reflejada. 

# Los lentes polarizados toman ventaja del ángulo de Brewster. Estos lentes están diseñados para bloquear las ondas TE, y de esta forma reducir el brillo enceguecedor generado por la reflección de la luz solar

# <img src="./images/polarized_glasses.jpg" width="350px" align= center>

# Así, si giramos los lentes en posición vertical (asumiento lentes con alto nivel de polarización), el efecto se invierte. Es decir, las ondas TE se transmiten y las TM no.

# Por otro lado, cuando $n_1 > n_2$, vemos que $R_\mathrm{TM} = R_\mathrm{TE} = 0$ sobre cierto ángulo. Este ángulo se denomina **ángulo crítico ($\theta_c$).** Para deterinar el ángulo crítico usamos la ley de Snell.

# El ángulo máximo para la onda transmitida es $\theta_t = 90^o$, la ley de Snell nos indica que existe un ángulo crítico. Sobre este valor, no existe solución real.
# 
# \begin{equation}
# n_1\sin\theta_c = n_2\sin90^o \Rightarrow \theta_c = \arcsin\left(n_2/n_1\right)
# \end{equation}
# 
# **Para $\theta_i > \theta_c$, $R_\mathrm{TE} = R_\mathrm{TM} = 1$.**

# Este mecanismo se llama **reflección interna total** y es la base para el funcionamiento de fibras ópticas y lasers
# <img src="./images/optical_fiber.png" width="450px" align= center>

# ## Reflección y transmissión en películas delgadas
# En el caso materiales de película delgada, las ondas electromagnéticas se reflejan y transmiten múltiples veces.
# 
# <img src="./images/reflectance_thinfilm.png" width="600px" align= center>

# Considerando los medios 1,2 y 3, ordenados consecutivamente en dirección de la onda incidente, se puede demostrar que en este caso los coeficientes de Fresnel, para indices de refracción reales son:
# 
# \begin{align}
# r &= \frac{r_{12}+r_{23}e^{2i\varphi_2}}
#           {1+r_{12}r_{23}e^{2i\varphi_2}}
# \\[10pt]
# t &= \frac{t_{12}t_{23}e^{i\varphi_2}}
#           {1+r_{12}r_{23}e^{2i\varphi_2}}
# \end{align}
# 
# donde $\varphi_2 = N_2k_0\cos\theta_i$; $r_{12}$, $r_{23}$ y $t_{12}$, $t_{23}$ son, respectivamente, los coeficientes de Fresnel desde el medio 1 al medio 2, y desde el medio 2 al medio 3. Estas fórmulas son válidas tanto para ondas TE como para ondas TM.

# Basado en estas expresiones, podemos calcular la reflectividad y tranmissividad de la película:
# 
# \begin{align}
# R = {\lvert r\rvert}^2 &= \frac{r_{12}^2+r_{23}^2+2r_{12}r_{23}\cos 2\varphi_2}
#                               {1 + 2r_{12}r_{23}\cos 2\varphi_2 + r_{12}^2r_{23}^2}
# \\[10pt]
# T = \frac{n_3\cos\theta_t}{n_1\cos\theta_i}{\lvert t\rvert}^2 &= 
# \frac{\left(1 - r_{12}^2\right)\left(1 - r_{23}^2\right)}
#      {1 + 2r_{12}r_{23}\cos 2\varphi_2 + r_{12}^2r_{23}^2}
# \end{align}

# Analicemos como se comportan estas ecuaciones en un caso real. 
# 
# Como ejemplo, consideremos la reflectividad de una película delgada de sílice (SiO$_2$) sobre un sustrato de silicio. Esta capa se genera naturalmente debido a la oxidación del silicio
# 
# <img src="./images/sio2_coating.png" width="600px" align= center>
# 
# Para simplificar, consideremos:
# - índice de refracción del aire: 1.0
# - índice de refracción de sílice: 1.5
# - índice de refracción del silicio: 4.3
# - espectro de longitudes de onda: 300 - 800 nm (visible)
# - espesor del sílice, $d$: variable
# - ángulo de incidencia $\theta_i$: variable

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
from empylib.fresnel import multilayer

# Reflectividad en capa delgada
lam = np.linspace(0.3,0.8,100)          # longitud de onda (en um)
n_layers = (1.0,1.5,4.3)         # índices de refracción n1, n2, n3
Rp = lambda tt,d : multilayer(lam, tt,n_layers, (d,), 'p')[0]
Rs = lambda tt,d : multilayer(lam, tt,n_layers, (d,), 's')[0]

# preparamos el ploteo
def plot_R_multi(theta,d):
    fig, ax = plt.subplots()
    fig.set_size_inches(9, 6)
    plt.rcParams['font.size'] = '16'
    ax.plot(lam,Rp(theta,d), label='$R_\mathrm{TM}$', color='red')
    ax.plot(lam,Rs(theta,d), label='$R_\mathrm{TE}$',color='blue')
    ax.set_xlim([min(lam),max(lam)])
    ax.set_ylim([0,1.0])
    ax.set_xlabel('Longitud de onda ($\mu$m)')
    ax.set_ylabel('Reflectividad')
    ax.legend(frameon=False)


# In[4]:


from ipywidgets import interact

@interact(theta=(0,89,10), d=(0,0.5,0.01))
def g(theta=30, d=0.3):
    return plot_R_multi(theta,d)


# Esta oscilaciones en la reflectancia al variar $\theta_i$ y $d$ son el resultado de la interferencia entre las ondas reflejadas en la parte inferior y superior de la película de silicio.
# 
# <img src="./images/interference.png" width="350px" align= center>

# En palabras simples, este fenómeno ocurre por qué la onda reflejada en la parte inferior de la película debe recorre un camino más largo. Esto produce un desface con las ondas reflejadas en la parte superior que deriva en interferencia constructiva (alta reflectividad) y destructiva (baja reflectividad)

# Este fenómeno se manifiesta en forma de color ya que nuestros ojos son sensibles a los cambios de radiación en este espectro.

# Analicemos como se manifiesta este fenómeno en forma de color:

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from empylib.fresnel import multilayer
from empylib.ref_spectra import AM15
from empylib.ref_spectra import color_system as cs
cs = cs.hdtv

# Reflectividad en capa delgada
lam = np.linspace(0.3,0.8,81)   # longitud de onda (en um)
n_layers = (1.0,1.5,4.3)         # índices de refracción n1, n2, n3
Rp = lambda tt,d : multilayer(lam, tt,n_layers, (d,), 'p')[0]
Rs = lambda tt,d : multilayer(lam, tt,n_layers, (d,), 's')[0]

def color_R_film(d):
    # formateamos la figura
    fig, ax = plt.subplots()
    fig.set_size_inches(9, 5)
    plt.rcParams['font.size'] = '16'
    
    AM15_spectra = AM15(lam)
    theta = np.linspace(0,90,100) # angulo de incidencia
    for i in range(len(theta)): 
        R = 0.5*Rp(theta[i],d) + 0.5*Rs(theta[i],d)
        Irad = R*AM15_spectra
        html_rgb = cs.spec_to_rgb(Irad, out_fmt='html')
        ax.axvline(theta[i], color=html_rgb, linewidth=6) 
    ax.set_xlim([min(theta),max(theta)])
    ax.set_ylim([0,1.0])
    ax.axes.yaxis.set_visible(False)
    ax.set_xlabel('Ángulo de incidencia (deg)')


# In[6]:


from ipywidgets import interact

@interact(d=(0,0.5,0.001))
def g(d=0.28):
    return color_R_film(d)


# ## Referencias
# Griffths D., *Introduction to Electrodynamics*, 4th Ed, Pearson, 2013
# - 7.3 Maxwell's Equations (7.36)
# - 9 Electromagnetic Waves (9.3 y 9.4)
