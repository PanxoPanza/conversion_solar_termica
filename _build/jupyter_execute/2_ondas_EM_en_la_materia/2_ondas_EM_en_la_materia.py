#!/usr/bin/env python
# coding: utf-8

#  <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # 2. Ondas electromagnéticas en la materia
# <br><br><br><br>
# Profesor: Francisco Ramírez CueSvas<br>
# Fecha: 19 de Agosto 2022

# <h1>Tabla de contenidos<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Ecuaciones-de-Maxwell-en-un-medio" data-toc-modified-id="Ecuaciones-de-Maxwell-en-un-medio-1">Ecuaciones de Maxwell en un medio</a></span><ul class="toc-item"><li><span><a href="#Vector-de-Poynting" data-toc-modified-id="Vector-de-Poynting-1.1">Vector de Poynting</a></span></li></ul></li><li><span><a href="#Referencias" data-toc-modified-id="Referencias-2">Referencias</a></span></li></ul></div>

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
# \begin{equation}
# \langle\vec{S}\rangle = \frac{1}{2}\mathrm{Re}\left(\vec{E}\times\vec{H}^*\right),
# \end{equation}
# 
# donde $\langle\cdots\rangle$ reprensenta el promedio en un periodo, y $^*$ reprenta el complejo conjugado.

# Consideremos, por ejemplo, el vector de Poynting para una onda plana que se propaga en un material con índice de refracción $N = n+i\kappa$:
# 
# \begin{align*}
# \langle\vec{S}\rangle &= \frac{1}{2}\mathrm{Re}\left(\vec{E}\times\vec{H}^*\right) \\
# &=\frac{1}{2}\mathrm{Re}\left[E_0 e^{i\left(\vec{k}\cdot\vec{r} - \omega t\right)}H_0^* e^{-i\left(\vec{k}^*\cdot\vec{r} - \omega t\right)}\right] \left(\hat{e}\times\hat{h}\right) \\
# &=\frac{1}{2}\mathrm{Re}\left[\frac{E_0^2}{Z_0Z_r^*} e^{i\left(k_0N\hat{k}\cdot\vec{r} - \omega t\right)}e^{-i\left(k_0N^*\hat{k}\cdot\vec{r} - \omega t\right)}\right] \hat{k} \\
# &=\frac{1}{2}\mathrm{Re}\left(\frac{E_0^2}{Z_0Z_r^*} \right)e^{-2k_0\kappa\left(\hat{k}\cdot\vec{r}\right)} \hat{k} \\
# &=\frac{1}{2}\frac{nE_0^2}{Z_0}e^{-\alpha\left(\hat{k}\cdot\vec{r}\right)} \hat{k}
# \end{align*}

# El término $\alpha = \frac{4\pi\kappa}{\lambda}$ es el **coeficiente de absorpción**. El inverso, $\delta = 1/\alpha$, se denomina **profundidad superficial** y representa la profundidad de penetración de la onda electromagnética en un material. 

# Como referencia, $\delta\sim 1000$ m en fibras ópticas a $\lambda = 1.55$ $\mu$m, que es la onda utilizada en comunicaciónes óptica. Por otro lado, en metales como la plata, oro o aluminio, $\delta\sim 10$ nm para $\lambda \sim 500$ nm (espectro de luz visible)

# Ahora con los conceptos de ondas electromagnéticas y vector de Poynting, pasemos a revisar este video explicativo de como fluye la energía en las redes eléctricas

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('bHIhgxav9LY', width=600, height=400,  playsinline=0, start=42)


# ## Referencias
# Griffths D., *Introduction to Electrodynamics*, 4th Ed, Pearson, 2013
# - 1.2 Diferential Calculus
# - 7.2 Electromagnetic Induction
# - 7.3 Maxwell's Equations (excepto 7.36)
# - 8.1 Charge and Energy
# - 9 Electromagnetic Waves (hasta 9.4)

# In[ ]:




