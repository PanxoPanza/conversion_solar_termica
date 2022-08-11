#!/usr/bin/env python
# coding: utf-8

#  <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # 1. La radiación como un fenómeno electromagnético
# <br><br><br><br>
# Profesor: Francisco Ramírez CueSvas<br>
# Fecha: 12 de Agosto 2022

# <h1>Tabla de contenidos<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Repaso-de-cálculo-vectorial" data-toc-modified-id="Repaso-de-cálculo-vectorial-1">Repaso de cálculo vectorial</a></span><ul class="toc-item"><li><span><a href="#Campo-escalar-y-vectorial" data-toc-modified-id="Campo-escalar-y-vectorial-1.1">Campo escalar y vectorial</a></span></li><li><span><a href="#Operadores-diferenciales" data-toc-modified-id="Operadores-diferenciales-1.2">Operadores diferenciales</a></span></li><li><span><a href="#Ejemplos-de-uso-de-operadores-diferenciales" data-toc-modified-id="Ejemplos-de-uso-de-operadores-diferenciales-1.3">Ejemplos de uso de operadores diferenciales</a></span></li></ul></li><li><span><a href="#Ecuaciones-de-Maxwell" data-toc-modified-id="Ecuaciones-de-Maxwell-2">Ecuaciones de Maxwell</a></span><ul class="toc-item"><li><span><a href="#Ley-de-Gauss" data-toc-modified-id="Ley-de-Gauss-2.1">Ley de Gauss</a></span></li><li><span><a href="#Ley-de-continuidad-del-campo-magnético" data-toc-modified-id="Ley-de-continuidad-del-campo-magnético-2.2">Ley de continuidad del campo magnético</a></span></li><li><span><a href="#Ley-de-Faraday" data-toc-modified-id="Ley-de-Faraday-2.3">Ley de Faraday</a></span></li><li><span><a href="#Ley-de-Ampere" data-toc-modified-id="Ley-de-Ampere-2.4">Ley de Ampere</a></span></li><li><span><a href="#Corrección-de-la-ley-de-Ampere" data-toc-modified-id="Corrección-de-la-ley-de-Ampere-2.5">Corrección de la ley de Ampere</a></span></li></ul></li><li><span><a href="#Ondas-electromagnéticas" data-toc-modified-id="Ondas-electromagnéticas-3">Ondas electromagnéticas</a></span><ul class="toc-item"><li><span><a href="#Ondas-electromagnéticas-en-el-vacío" data-toc-modified-id="Ondas-electromagnéticas-en-el-vacío-3.1">Ondas electromagnéticas en el vacío</a></span></li><li><span><a href="#Ondas-electromagnéticas-en-la-materia" data-toc-modified-id="Ondas-electromagnéticas-en-la-materia-3.2">Ondas electromagnéticas en la materia</a></span></li><li><span><a href="#Vector-de-Poynting" data-toc-modified-id="Vector-de-Poynting-3.3">Vector de Poynting</a></span></li></ul></li><li><span><a href="#Referencias" data-toc-modified-id="Referencias-4">Referencias</a></span></li></ul></div>

# ## Repaso de cálculo vectorial

# ### Campo escalar y vectorial
# - Un campo escalar representa la distribución espacial de una magnitud. Por ejemplo, distribución de densidad, temperatura o presión. En coordenadas cartesianes: $f = f(x,y,z)$, donde $f$ es un campo escalar.
# 
# - Un campo vectorial representa la distribución espacial de una magnitud vectorial. Por ejemplo, distribución de velocidades, campo eléctrico o magnético. En coordenadas cartesianas: $\vec{f} = \vec{f}(x,y,z)$, donde $\vec{f}$ es un campo escalar.

# Por ejemplo, consideremos la siguiente modelación de convección natural en cavidad cuadrada:

# <img src="./images/natural_convection.png" width="500px" align= center>

# Aquí podemos visualizar la distribución espacial de temperaturas y velocidades de un fluido sometido a las condiciones indicadas en la figura. 
# 
# De esta figura podemos identificar:
# - Campo escalar: Distribución de temperaturas
# 
# - Campo vectorial: Distribución de velocidades

# ### Operadores diferenciales

# **Operador Del.** 
# 
# Definimos el operador $\nabla$ o "del", como:
# 
# \begin{equation}
# \nabla= \left( \hat{x}\frac{\partial }{\partial x} + \hat{y}\frac{\partial }{\partial y} + \hat{z}\frac{\partial }{\partial z} \right)
# \end{equation}

# **Operador Gradiente.** 
# 
# Es equivalente a la derivada de una función, pero en múltiples dimenciones. Permite identificar zonas de crecimiento o decrecimiento de un campo escalar o vectorial. Se define como el operador Del multiplicado por el campo escalar.
# 
# \begin{equation}
# \nabla f= \frac{\partial f}{\partial x}\hat{x} + \frac{\partial f}{\partial y}\hat{y}+ \frac{\partial f}{\partial z}\hat{z}
# \end{equation}
# 
# > El gradiente de un campo escalar $f$, es un vector

# **Operador Divergente.**
# 
# Se aplica a campos vectoriales. Es una medida de cuanto un campo vectorial diverge o converge respecto de un punto en cuestión. Se define como el producto punto entre el operador Del y un campo vectorial:
# 
# \begin{equation}
# \nabla \cdot \vec{f}= \frac{\partial f_x}{\partial x} + \frac{\partial f_y}{\partial y} + \frac{\partial f_z}{\partial z}
# \end{equation}

# Por ejemplo:
# 
# <img src="./images/divergence.jpg" width="70%" align= center>
# 
# (a) $\nabla\cdot\vec{f} \gt 0$
# 
# (b) $\nabla\cdot\vec{f} = 0$
# 
# (c) $\nabla\cdot\vec{f} \gt 0$

# **Operador Rotacional.** 
# 
# Se aplica a campos vectoriales. Es una medida de cuanto un campo vectorial rota respecto de un punto en cuestión. Se define como el producto cruz entre el operador Del y un campo vectorial:
# 
# \begin{equation}
# \nabla \times \vec{f}= \left(\frac{\partial f_z}{\partial y}- \frac{\partial f_y}{\partial z}\right)\hat{x}+\left(\frac{\partial f_x}{\partial z}- \frac{\partial f_z}{\partial x}\right)\hat{y}+\left(\frac{\partial f_y}{\partial x}- \frac{\partial f_x}{\partial y}\right)\hat{z}
# \end{equation}

# Por ejemplo:
# 
# <img src="./images/curl.jpg" width="600"  align= center>
# 
# (a) $\nabla\times\vec{f} \gt 0$
# 
# (b) $\nabla\times\vec{f} \gt 0$
# 
# >En la figura anterior (divergente), $\nabla\times\vec{f} = 0$ en todos los casos.

# ### Ejemplos de uso de operadores diferenciales
# Los operadores diferenciales permiten una descripción más compacta en de las formuals basadas en ecuaciones diferenciales parciales.

# <img src="./images/mass_conservation.png" width="500" align= center>

# Un ejemplo conocido es el caso de la ecuación de conservación de masa en su forma diferencial.
# 
# $$\frac{\partial \rho}{\partial t}+\frac{\partial (\rho u)}{\partial x} +\frac{\partial (\rho v)}{\partial y}+\frac{\partial (\rho w)}{\partial z}=0.$$
# 
# Usando el operador Del,
# 
# $$\frac{\partial \rho}{\partial t} + \nabla\cdot\left(\rho\vec{V}\right)
# =0,$$
# 
# o bien:
# 
# $$\frac{\partial \rho}{\partial t} + \vec{V}\cdot\nabla\rho+ \rho\left(\nabla\cdot\vec{V}\right)
# =0.$$

# ## Ecuaciones de Maxwell

# ### Ley de Gauss
# *El flujo de campo electrico a través de una superficie cerrada es proporcional a la carga eléctrica, $\rho$, contenida dentro de esta superficie.*

# En su forma diferencial:
# 
# \begin{equation}
# \nabla\cdot\left(\varepsilon_0\vec{E}\right) = \rho
# \end{equation}

# Donde:
#  - $\vec{E}$, es el **campo eléctrico** (se mide en unidades de $\mathrm{V/m}$).
# 
#  - $\varepsilon_0 = 8.854\times10^{-12}$ $\mathrm{F/m}$, es la **permitividad** en el vacío. 

# >Un campo eléctrico diveregente(convergente) es el resultado de una carga eléctrica positiva(negativa) que actúa como fuente(sumidero)

# ### Ley de continuidad del campo magnético
# *No existen cargas magnéticas que den lugar a un campo magnético*

# En su forma diferencial:
# 
# \begin{equation}
# \nabla\cdot\left(\mu_0\vec{H}\right) = 0
# \end{equation}

# Donde:
# 
#  - $\vec{H}$, es la **intensidad de campo magnetico** (se mide en unidades de $\mathrm{A/m}$).
#  - $\mu_0 = 4\pi\times10^{-7}$ $\mathrm{N/A^2}$, es la **permeabilidad** magnética en el vacío.

# >A diferencia del campo eléctrico, el campo magnético es continuo. Es decir no tiene fuentes ni sumideros

# Es común en los textos de física ver las ecuaciones de campo magnético respresentadas en base al **vector campo magnético** $\vec{B}$ y no a $\vec{H}$ Esto, porque $\vec{B}$ representa la componente "experimentalmente medible" del campo magnético y la que efectivamente afecta a las cargas en movimiento. Ambas variables se relaciona mediante $\vec{B} =\mu_0\vec{H}$.
# 
# De igual manera, el análogo del campo eléctrico se denomina **desplazamiento eléctrico**, y se relaciona con el campo eléctrico mediante $\vec{D}=\varepsilon_0\vec{E}$. En este caso, la componente "experimentalmente medible" es $\vec{E}$ y, por ende, es formalmente utilizada en los textos de física.
# 

# ### Ley de Faraday
# *Un campo magnético variable en el tiempo induce un campo eléctrico rotacional*

# \begin{equation}
# \nabla\times\vec{E} = -\mu_0\frac{\partial \vec{H}}{\partial t}
# \end{equation}

# - Notar que el campo magnético debe ser variable en el tiempo para poder inducir una corriente.

# ### Ley de Ampere
# *Una corriente eléctrica induce un campo magnético rotacional alrededor de ella*

# \begin{equation}
# \nabla\times\vec{H} = \vec{J}
# \end{equation}

# Donde:
# 
#  - $\vec{J}$, es la **densidad de corriente**  eléctrica (se mide en unidades de $\mathrm{A/m^2}$).

# La ley de Ampere y de Faraday son la base del funcionamiento de motores de inducción, motores DC, transformadores, etc.

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('CWulQ1ZSE3c', width=600, height=400,  playsinline=0, start=42)


# ### Corrección de la ley de Ampere
# Es posible demostrar que, para un campo vectorial $\vec{f}$, se cumple la siguiente identidad  
# 
# $$\nabla\cdot\nabla\times\vec{f} = 0,$$

# Analicemos el divergente en la ley de Faraday
# 
# \begin{equation*}
# \nabla\cdot \nabla\times\vec{E} = -\nabla\cdot\mu_0\frac{\partial \vec{H}}{\partial t} \Rightarrow -\frac{\partial }{\partial t}\left(\nabla\cdot\mu_0\vec{H}\right) =0
# \end{equation*}
# 
# La relación se cumple por la ley de continuidad del campo magnético

# Por otro lado, el divergente en la ley de Ampere:
# 
# \begin{equation*}
# \nabla\cdot \nabla\times\vec{H} = \nabla\cdot\vec{J} \Rightarrow \nabla\cdot\vec{J} = 0.
# \end{equation*}
# 
# Sin embargo, por la ley de conservación de masa:
# 
# \begin{equation*}
# \nabla\cdot\vec{J} = - \frac{\partial \rho}{\partial t}
# \end{equation*}

# Claramente, la ecuación de Ampere no está completa. La corrección, fue propuesta por James Maxwell
# 
# \begin{equation}
# \nabla\times\vec{H} = \vec{J} + \varepsilon_0\frac{\partial\vec{E}}{\partial t}
# \end{equation}
# 
# El último término es conocido como la *corriente de desplazamiento de Maxwell.*

# >A través de esta contribución James C. Maxwell logra unificar las teorías de electricidad, magnetismo y la luz en un solo fenómeno, **las ondas electromagnéticas**.

# ## Ondas electromagnéticas

# ### Ondas electromagnéticas en el vacío

# En el vacío, no existen cargas eléctricas ($\rho=0$) ni corrientes eléctricas ($\vec{J} = 0$), y por lo tanto las ecuaciones de Maxwell son:
# 
# \begin{align*}
# \nabla\cdot\vec{E} &= 0 \\
# \nabla\cdot\vec{H} &= 0 \\
# \nabla\times\vec{E} &= -\mu_0\frac{\partial \vec{H}}{\partial t} \\
# \nabla\times\vec{H} &= \varepsilon_0\frac{\partial \vec{E}}{\partial t}
# \end{align*}

# Analicemos el rotacional sobre la ley de faraday
# 
# \begin{equation*}
# \nabla\times\nabla\times\vec{E} = -\mu_0\frac{\partial}{\partial t}\left(\nabla\times \vec{H}\right)
# \end{equation*}

# Mediante la identidad,
# 
# $$\nabla\times\nabla\times\vec{E} = \nabla\left(\nabla\cdot\vec{E}\right) - \nabla\cdot\nabla\vec{E},$$

# y la ley de Gauss $\nabla\cdot\vec{E} = 0$, podemos demostrar:
# 
# \begin{equation*}
# \nabla^2\vec{E} = \mu_0\frac{\partial}{\partial t}\left(\nabla\times \vec{H}\right)
# \end{equation*}

# Finalmente, mediante la ley de Ampere modificada, determinamos:
# 
# \begin{equation*}
# \nabla^2\vec{E} - \varepsilon_0\mu_0\frac{\partial^2\vec{E}}{\partial t^2} = 0
# \end{equation*}

# Esta es la ecuación de onda en su forma tridimensional, la cual acepta soluciones del tipo:
# 
# $$E_0 e^{i\left(\vec{k}\cdot\vec{r} - \omega t\right)} \hat{e},$$ 
# 
# donde: 
# - $\vec{k}$ es el vector de onda
# - $\vec{r}$ es un vector de posición 
# - $\omega$ es la frecuencia angular (rad/s) 
# - $E_0$ es la amplitud
# - $\hat{e}$ es la dirección de oscilación de la onda.

# Reemplazando esta solución en la ecuación de onda, determinamos la **relación de dispersión** entre la **magnitud del vector de onda en el vacío**, $k_0 = |\vec{k}|$, y la frecuencia angular:
# 
# \begin{equation}
# k_0 = \frac{\omega}{c_0},
# \end{equation}
# 
# donde
# 
# $$c_0 = \frac{1}{\sqrt{\varepsilon_0\mu_0}} \approx 3.00\times10^8~\mathrm{m/s,}$$ 
# 
# es la velocidad de la luz.

# En general, estamos más familizarizados con los conceptos de **longitud de onda $\lambda$** y **frecuencia $\nu$**, para caracterizar ondas electromagnéticas. Estas variables se relacionan con el vector de onda y la frecuencia mediante:
# 
# \begin{equation}
# k_0 = \frac{2\pi}{\lambda}, ~~ \omega = 2\pi\nu
# \end{equation}

# De igual forma, mediante la relación de dispersión, podemos establecer la siguiente relación entre la longitud de onda y la frecuencia:
# 
# \begin{equation}
# \lambda\nu = c_0
# \end{equation}

# > Esto quiere decir, que un punto $\vec{r}$ arbitrario de la onda, viaja en el vacío a una velocidad constante $c_0$, **independendiente de su frecuencia**.

# **El vector de onda representa la dirección de propagación de la onda**. A partir de la ley de Gauss, podemos demostrar:
# 
# \begin{equation}
# \vec{k} \cdot\hat{e} = 0
# \end{equation}
# 
# Es decir, el campo eléctrico oscila en dirección perpendicular a la dirección de propagación.

# > En otras palabras, el campo electrico representa una **onda transversal.**
# 
# <img src="./images/onda_transversal.png" width="400px" align= center>
# <center> Esquema de una onda transversal </center>

# En general, tenemos dos tipos de ondas, transversales, y longitudinales

# In[2]:


from IPython.display import IFrame, display
display(IFrame('https://www.geogebra.org/material/iframe/id/auyft2pd/width/640/height/480/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/false/ctl/false','700px', '450px'))


# Debido a que el campo eléctrico toma la forma $\vec{E} = E_0 e^{i\left(\vec{k}\cdot\vec{r} - \omega t\right)} \hat{e},$$  decimos que se comporta como una **onda plana**, debido a que el campo es constante sobre un plano perpendicular a la dirección de propagación

# <img src="./images/planewave.png" width="400px" align= center>

# De igual forma, podemos demostrar que la intensidad de campo magnético en el vacío también satisface la ecuación de onda:
# 
# \begin{equation*}
# \nabla^2\vec{H} - \varepsilon_0\mu_0\frac{\partial^2\vec{H}}{\partial t^2} = 0
# \end{equation*}

# Utilizando un tratamiento similar al de $\vec{E}$, concluiremos que $\vec{H}$:
# - Se comporta como una onda de la forma $H_0 e^{ i\left(\vec{k}\cdot\vec{r} - \omega t\right)} \hat{h}$
# 
# - Se mueve en el vacio a una velocidad constante $c_0 \approx 3.00\times10^8~\mathrm{m/s}$.
# 
# - Es una onda transversal ($\vec{k}\cdot\hat{h} = 0$ por la ley de continuidad).

# Finalmente, mediante la ley de Faraday (o Ampere), deducimos:
# 
# \begin{equation*}
# \hat{h}{H}_0 = \frac{E_0}{k_0Z_0}\left(\hat{k}\times\hat{e}\right),
# \end{equation*}
# 
# donde $Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}}$, es la **impedancia del vacío** (se mide en $\Omega$).

# De esta relación concluímos:
# 1. El campo eléctrico magnético y el vector de onda son mutuamente perpendiculares ($H\perp E\perp k$)
# 2. La amplitud de la intensidad de campo magnético y del campo eléctrico, estan relacionadas por: ${H}_0 = \frac{E_0}{k_0Z_0}$

# En resumen:
# 1. En el vacío, $\vec{E}$ y $\vec{H}$ se comportan como ondas trasversales de la forma $\propto e^{ i\left(\vec{k}\cdot\vec{r} - \omega t\right)}$.
# 
# 2. El vector de onda $\vec{k}$ representa la dirección de propagación de $\vec{E}$ y $\vec{H}$. 
# 
# 3. $\vec{E}$ y $\vec{H}$ se propagan a una velocidad constante $c_0 = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3.00\times10^8$ m/s.
# 
# 4. La magnitud del vector de onda en el vacío, $k_0$, y la frecuencia angular, $\omega$, están relacionadas por $k_0 = \omega/c_0$
# 
# 5. $\vec{E}$, $\vec{H}$ y $\vec{k}$ son mutuamente perpendiculares. 
# 
# 6. Las amplitudes de $\vec{E}$ y $\vec{H}$ están asociadas por la relación ${H}_0 = \frac{E_0}{k_0Z_0}$, donde $Z_0 = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$.

# <img src="./images/EM-Wave.gif" width="400px" align= center>
# 
# <center> Esquema de una onda electromagnética </center>

# ### Ondas electromagnéticas en la materia

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
# |k| = N \frac{\omega}{c_0}
# \end{equation}
# 
# donde $N = \sqrt{\varepsilon} = n +i\kappa$, es el **índice de refracción complejo**. En general $n$ se conoce como el **índice de refracción**, y $\kappa$ como **extinsión**.

# > Notar que la velocidad de la onda también cambia a $c = c_0/n$

# Igualmente la relación entre $H_0$ y $E_0$, es de la forma 
# 
# $$H_0 = \frac{E_0}{k_0 Z_0Z_r},$$
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
# 6. Las amplitudes de $\vec{E}$ y $\vec{H}$ están asociadas por la relación ${H}_0 = \frac{E_0}{k_0Z_0Z_r}$, donde $Z_r = \frac{1}{\sqrt{\varepsilon}}$.

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
# &=\frac{1}{2}\mathrm{Re}\left[\frac{E_0^2}{k_0Z_0Z_r^*} e^{i\left(k_0N\hat{k}\cdot\vec{r} - \omega t\right)}e^{-i\left(k_0N^*\hat{k}\cdot\vec{r} - \omega t\right)}\right] \hat{k} \\
# &=\frac{1}{2}\mathrm{Re}\left(\frac{E_0^2}{k_0Z_0Z_r^*} \right)e^{-2k_0\kappa\left(\hat{k}\cdot\vec{r}\right)} \hat{k} \\
# &=\frac{1}{2}\frac{nE_0^2}{k_0Z_0}e^{-\alpha\left(\hat{k}\cdot\vec{r}\right)} \hat{k}
# \end{align*}

# El término $\alpha = \frac{4\pi\kappa}{\lambda}$ es el **coeficiente de absorpción**. El inverso, $\delta = 1/\alpha$, se denomina **profundidad superficial** y representa la profundidad de penetración de la onda electromagnética en un material. 

# Como referencia, $\delta\sim 1000$ m en fibras ópticas a $\lambda = 1.55$ $\mu$m, que es la onda utilizada en comunicaciónes óptica. Por otro lado, en metales como la plata, oro o aluminio, $\delta\sim 10$ nm para $\lambda \sim 500$ nm (espectro de luz visible)

# Ahora con los conceptos de ondas electromagnéticas y vector de Poynting, pasemos a revisar este video explicativo de como fluye la energía en las redes eléctricas

# In[3]:


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




