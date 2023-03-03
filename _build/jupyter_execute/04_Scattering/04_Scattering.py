#!/usr/bin/env python
# coding: utf-8

#  <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # Scattering electromagnético
# <br><br><br><br>
# Profesor: Francisco Ramírez Cuevas<br>
# Fecha: 2 de Septiembre 2022

# ## Interacción de luz según el tamaño de un cuerpo
# Hasta el momento hemos analizado las ecuaciones de Maxwell y condiciones de borde en coordenadas cartesianas. Estas relaciones se aplican a interfaces rectas. 
# 

# En el caso de cuerpos curvos, los coeficientes de Fresnel y otras fórmulas relacionadas aún son aplicables, siembre y cuando el radio de curvartura del cuerpo $R \gg \lambda$ 
# 
# <img src="./images/fresnel_curvature.png" width="500px" align= center>

# ### Interacción de luz con cuerpos grandes

# A través de este principio podemos explicar la separación de colores en un arcoiris.

# Primero, es importante notar que el índice de refracción del agua en el espectro visible no es constante. Este índice tiene un pequeño grado de dispersión, y decae a medida que la longitud de onda crece. Así, a partir de la ley de Snell, el ángulo de transmisión de cada onda (o color), crece proporcional a la longitud de onda.
# 
# <img src="./images/rainbow_refraction.png" width="600px" align= center>

# Este fenómeno produce que las ondas se separen en el espacio en función de su longitud de onda. 
# 
# En una gota de agua, el efecto de separación de colores se magnifica a medida que la luz se refleja en el interior

# <img src="./images/rainbows.jpg" width="300px" align= center>

# ### Interacción de luz con cuerpos pequeños

# Cuándo las dimensiones del cuerpo, $D$, son comparables a la longitud de onda, el radio de curvatura se hace significativo y las soluciones de las ecuaciones de Maxwell para una interface plana no son aplicables

# En este caso, se produce el fenómeno de ***scattering* de luz** asociado a la disperción de luz en múltiples direcciones. Además del scattering, tenemos el fenómeno de **absorción de luz** asociada con la porción de la energía incidente absorbida por el objeto. Por último, llamamos **extinción de luz** a la suma de la energía de scattering y absorción.
# 
# <img src="./images/scattering_schematic.png" width="450px" align= center>

# ## Scattering en esferas (solución de Mie)

# Consideremos el modelo simple una onda electromagnética interactuando con una esfera de radio $R$ y diámetro $D$ tal que $D/\lambda \sim 1$
# <img src="./images/em_wave_sphere.png" width="300px" align= center>

# Llamaremos al índice de refracción de la esfera $N_p$, y al índice de refracción del exterior $N_h$. 
# 
# En este caso asumimos que el índice de refracción del exterior no tiene componente compleja, es decir $N_h = n_h$
# 
# El espacio está definido en coordenadas esféricas, donde:
# 
# - $\theta$: ángulo cenital
# - $\phi$: ángulo azimutal
# - $r$: posición radial

# La solución, propuesta por Gustav Mie, se basa una expansión en serie de ondas esféricas $\vec{M}_{lm}(r, \theta,\phi)$ y $\vec{N}_{lm}(r, \theta,\phi)$ (más información en las referencias).

# Por ejemplo, la componente del campo eléctrico correspondiente al scattering, $\vec{E}_\mathrm{sca}$ es:
# 
# \begin{equation*}
# \vec{E}_\mathrm{sca}(r, \theta,\phi) = \sum_{l=1}^\infty \mathrm{Im}\left[E_0\frac{2l+1}{l(l+1)}i^l\left(a_l \vec{N}_{l1}^{(3)} - b_l \vec{M}_{l1}^{(3)}\right)\right]
# \end{equation*}
# 
# donde los coeficientes $a_l$ y $b_l$ están dados por la funciones de Ricatti-Bessel, $\psi(x)$ y $\xi(x)$, en la forma:
# 
# \begin{equation*}
# a_l = \frac{p\psi_l(px)\psi'_l(x) - \psi_l(x)\psi'_l(px)}{p\psi_l(px)\xi'_l(x) - \xi_l(x)\psi'_l(px)},
# \quad\quad\quad
# b_l = \frac{\psi_l(px)\psi'_l(x) - p\psi_l(x)\psi'_l(px)}{\psi_l(px)\xi'_l(x) - p\xi_l(x)\psi'_l(px)},
# \end{equation*}
# 
# donde $x = n_hk_0R$, y $p = N_p/n_h$. 

# El campo magnético está dado por $\vec{H}_\mathrm{sca} = \frac{n_h}{Z_0} \left(\hat{k}\times\vec{E}_\mathrm{sca}\right)$.

# A partir de la solución de Mie, deducimos que la intensidad y distribución del scattering electromagnético depende de dos parámetros: 
# - $x = n_hk_0R\approx D/\lambda_h$, que representa la proporción entre el tamaño de la particula ($D$) y la longitud de onda en el medio circundante ($\lambda_h= \lambda_0/n_h$)
# 
# - $px = N_pk_0R\approx D/\lambda_p$ que representa la proporción entre el tamaño de la particula y la longitud de onda dentro de la partícula ($\lambda_p=\lambda_0/n_p$).

# ### Distribución del campo eléctrico
# A partir de esta solución, podemos visualizar la distribución del campo eléctrico durante el fenómeno de scattering.

# La siguiente figura representa el scattering electromagnético a partir de la solución de Mie. La dirección de la onda incidente es $\hat{k}_\mathrm{inc} = \hat{x}$, con el campo eléctrico polarizado en dirección $\hat{e}=\hat{z}$. En la figura de la izquierda mostramos la distribución del campo electrico total, es decir el campo eléctrico incidente ($\vec{E}_\mathrm{inc}$) y de scattering ($\vec{E}_\mathrm{sca}$). En la figura de la derecha, hemos removido $\vec{E}_\mathrm{inc}$ para poder visualizar $\vec{E}_\mathrm{sca}$
# 
# <img src="./images/scattering_distribution.png" width="600px" align= center>

# Utilizando la dirección de la onda incidente como referencia, podemos ver que la intensidad del scattering es mayor hacia adelante ($\theta = 0^o$) y decrece a medida de $\theta$ aumenta. Debido a la simetría axial, el scattering no varía en $\phi$.

# En general, la distribución del scattering depende del tamaño de la partícula en relación la longitud de onda.
# 
# <img src="./images/scattering_vs_size.png" width="550px" align= center>

# Particularmente, cuando $D/\lambda \ll 1$, se denomina Rayleight scattering. En este caso el campo scattering está distribuido uniformemente alrededor de la partícula

# ### Flujo de energía
# Al igual que con el estudio de reflexión y transmisión, la solución $\vec{E}_\mathrm{sca}$ nos permite determinar el el vector de Poyinting asociado a scattering, $\langle\vec{S_\mathrm{sca}}\rangle = \frac{1}{2}\mathrm{Re}\left(\vec{E}_\mathrm{sca}\times\vec{H}^*_\mathrm{sca}\right)~\mathrm{[W/m^2]}$.

# Notar que, en general, $\langle\vec{S_\mathrm{sca}}\rangle$ varía según $\theta$, $\phi$ y $r$.
# 
# <img src="./images/poynting_vector.png" width="300px" align= center>

# La potencia neta por scattering, $W_\mathrm{sca}$ se obtiene integrando $\langle\vec{S_\mathrm{sca}}\rangle$ sobre la superticie de la esfera:
# 
# \begin{align*}
# W_\mathrm{sca} &= \oint_{S} \langle\vec{S_\mathrm{sca}}\rangle\cdot\hat{r}dS 
# \\
# &= \int_0^{2\pi}\int_0^{\pi} \left[\langle\vec{S_\mathrm{sca}}\rangle \cdot \hat{r}\right]R^2 \sin\theta d\theta~d\phi
# \\
# &= \Phi_\mathrm{inc}~2\pi\int_0^{\pi}  P_\mathrm{sca}(\theta) \sin\theta d\theta
# \quad\mathrm{[W]}
# \end{align*}

# donde $\Phi_\mathrm{inc} = \frac{n_hE_0}{2Z_0}~\mathrm{[W/m^2]}$ es el flujo de energía o intensidad de la onda incidente, y $P_\mathrm{sca}(\theta)  = \frac{R^2}{\Phi_\mathrm{inc}}\left[\langle\vec{S_\mathrm{sca}}\rangle \cdot \hat{r}\right]$, es la **función de distribución de scattering** o **función de fase**.

# La función de fase se define como la **energía de scattering por unidad de ángulo sólido $d\Omega = \sin\theta d\theta d\phi$ relativo al flujo de energía de la onda incidente, $\Phi_\mathrm{inc}$**.

# En otras palabras, para una onda incidente con intensidad $\Phi_\mathrm{inc}$, la energía de scattering en dirección $\theta$ es $\Phi_\mathrm{inc} P_\mathrm{sca}(\theta)d\Omega$
# 
# <img src="./images/phase_function.png" width="300px" align= center>

# Mediante un proceso similar, podemos determinar la potencia extinguida, $W_\mathrm{ext}$, a partir del campo total $\vec{E}_\mathrm{tot} = \vec{E}_\mathrm{inc} + \vec{E}_\mathrm{sca}$

# Al igual que con los coeficientes de Fresnel, es común definir la energía relativa a $I_\mathrm{inc}$:
# 
# \begin{eqnarray*}
# C_\mathrm{sca} &=& \frac{W_\mathrm{sca}}{I_\mathrm{inc}} = \frac{2\pi}{k^2}\sum_{l=1}^\infty (2l+1)\left(|a_l|^2 + |b_l|^2\right)&\quad&\mathrm{[m^2]}
# \\[10pt]
# C_\mathrm{ext} &=& \frac{W_\mathrm{ext}}{I_\mathrm{inc}} = \frac{2\pi}{k^2}\sum_{l=1}^\infty (2l+1)\mathrm{Re}\left(a_l + b_l\right)&\quad&\mathrm{[m^2]}
# \end{eqnarray*}
# 
# debido a que $C_\mathrm{sca}$ y $C_\mathrm{ext}$ están definidos en unidades de área, se denominan **sección transversal de scattering y extinción, respectivamente**.

# Por conservación de energía, la sección transversal de absorción, $C_\mathrm{abs} = C_\mathrm{ext} - C_\mathrm{sca}$.

# ### Parámetro de asimetría
# El parámetro de asimetría, $\mu_\mathrm{sca} \in [-1,1]$, nos permite cuantificar la anisotropía en la distribución del scattering.
# 
# <img src="./images/asymmetry_parameter.png" width="550px" align= center>

# En el caso de esferas, se define por:
# 
# \begin{equation*}
# \mu_\mathrm{sca} = \frac{4\pi}{k^2C_\mathrm{sca}}\left[
# \sum_{l=1}^\infty \frac{l(l+2)}{l+1}\mathrm{Re}\left(a_la_{l+1}^* + b_lb_{l+1}^*\right) +
# \sum_{l=1}^\infty\frac{2l+1}{l(l+1)}\mathrm{Re}\left(a_lb_l^*\right)
# \right]
# \end{equation*}

# ## Analisis de scattering

# Los parámetros $C_\mathrm{sca}$, $C_\mathrm{abs}$ y $C_\mathrm{ext}$ permiten cuantificar la energía de scattering, absorción y extinción relativa a la intensidad de la fuente $I_\mathrm{inc}$, así como también su distribución en el espectro.

# ### Particulas con índice de refracción real (dieléctricos)

# Por ejemplo, analicemos el scattering de una esfera de agua ($N_p\approx 1.33$) en el aire ($n_h = 1.0$).
# 
# Notar que $N_p\approx 1.33$ implica $C_\mathrm{abs} = 0$

# In[1]:


get_ipython().run_cell_magic('capture', 'show_plot', "import empylib.miescattering as mie\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nlam = np.linspace(0.3,1.4,200)  # espectro de longitudes de onda\nnh = 1.0                        # índice de refracción del material circundante\nNp = 1.33                       # índice de refracción de la partícula\nD = [0.1, 0.3, 0.5, 0.7, 1.0]   # distribución de diámetros \n\nfig, ax = plt.subplots()                # creamos ejes para graficar\ncolors = plt.cm.jet(np.linspace(0,1,len(D))) # set de colores para las curvas\nfor i in range(len(D)):\n    Ac = np.pi*D[i]**2/4                # área transversal de la partícula\n    Qsca = mie.scatter_efficiency(lam,nh,Np,D[i])[1] # determinamos Csca/Ac\n    ax.plot(lam,Qsca*Ac,'-', color=colors[i], label=('%i' % (D[i]*1E3))) # grafico Csca\n\n# etiquetas de ejes y formateo de la figura\nfig.set_size_inches(6, 4)         # tamaño de figura\nplt.rcParams['font.size'] = '14'   # tamaño de fuente\nax.set_xlabel(r'Longitud de onda, $\\lambda$ ($\\mu$m)', fontsize=16)\nax.set_title('scattering partícula de agua')\nax.set_ylabel(r'$C_\\mathrm{sca}$ ($\\mu$m$^2$)', fontsize=16)\nax.legend(frameon=False, title=r'$D$ ($\\mu$m)')\nplt.show()\n")


# In[2]:


show_plot()


# A partir de este gráfico podemos identificar algunos patrones comúnes en scattering:
# - La energía de scattering aumenta con el tamaño de la partícula
# 
# - A medida que el tamaño aumenta, la longitud de onda para scattering máximo crece (*red-shifting*)

# Esta es una característica general del scattering de partículas dieléctricas.

# A partir de este gráfico podemos entender muchas situaciones de la vida cotidiana.

# Por ejemplo, en la niebla las partículas de agua tienen un tamaño microscópico ($D\sim 1\mu$m) y, por lo tanto, dispersan la mayor parte de la luz visible.
# 
# <img src="./images/difuse_and_specular.png" width="600px" align= center>

# Para un haz de luz incidente en un medio con partículas, llamamos **componente difusa** a la porción de la luz dispersada por scattering, y como **componente especular** a la porción no dispersada.

# En el cielo, en cambio, las moleculas del aire son mucho más pequeñas, y el scattering es más intenso para ondas en el espectro del color azul y violeta ($\lambda < 450$ nm)
# 
# <img src="./images/sky_scattering.png" width="600px" align= center>

# La componente difusa, así, corresponde a los colores azul y violeta. La componente especular, corresponde al resto de los colores del espectro visible. El fenómeno expica el color azul del cielo durante el día.

# ### Parículas metálicas

# El naturaleza del scattering es diferente para los metales. En este caso, el movimiento libre de los electrones genera acumulación de carga en la superficie de la partícula. Como resultado, la partícula se polariza generando fenómenos de resonancia en determinadas longitudes de onda.
# 
# <img src="./images/surface_plasmon.png" width="350px" align= center>

# En la siguiente figura, graficamos $C_\mathrm{sca}$ y $C_\mathrm{abs}$ para partículas de distinto diámetro. Ambas variables son normalizadas por al área transversal de la esfera $\pi R^2$, para mejor comparación entre esferas de distintas dimensiones.

# In[3]:


get_ipython().run_cell_magic('capture', 'show_plot', "import empylib.miescattering as mie\nimport empylib.nklib as nk\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nlam = np.linspace(0.2,0.8,200)     # espectro de longitudes de onda\nnh = 1.0                           # índice de refracción del material circundante\nNp = nk.silver(lam)                # índice de refracción de la partícula\nD = [0.01, 0.02, 0.05, 0.08, 0.1]  # distribución de diámetros \n\nfig, ax = plt.subplots(1,2)        # creamos ejes para graficar\ncolors = plt.cm.jet(np.linspace(0,1,len(D))) # set de colores para las curvas\nfor i in range(len(D)):\n    Qext, Qsca = mie.scatter_efficiency(lam,nh,Np,D[i])[0:2] # determinamos Cext/Ac y Csca/Ac\n    Qabs = Qext - Qsca\n    ax[0].plot(lam,Qsca,'-', color=colors[i], label=('%i' % (D[i]*1E3))) # grafico Csca/Ac\n    ax[1].plot(lam,Qabs,'-', color=colors[i], label=('%i' % (D[i]*1E3))) # grafico Cabs/Ac\n\n# etiquetas de ejes y formateo de la figura\nfig.set_size_inches(13, 5)         # tamaño de figura\nplt.rcParams['font.size'] = '14'   # tamaño de fuente\n\nfor i in range(2):\n    ax[i].set_xlabel(r'Longitud de onda, $\\lambda$ ($\\mu$m)', fontsize=16)\n    ax[i].set_ylim(0,6.2)\n\nax[0].set_title('Scattering partícula de plata', fontsize=16)\nax[1].set_title('Absorción partícula de plata', fontsize=16)\nax[0].set_ylabel(r'$C_\\mathrm{sca} / \\pi R^2$', fontsize=16)\nax[1].set_ylabel(r'$C_\\mathrm{abs} / \\pi R^2$', fontsize=16)\nax[1].legend(frameon=False, title=r'D (nm)')\nplt.show()\n")


# In[4]:


show_plot()


# - Para $D < 20$ nm, $C_\mathrm{sca}$ es despreciable en comparación con $C_\mathrm{abs}$. El peak en $C_\mathrm{abs}$ es el resultado de la resonancia del sistema, similar al modelo de Lorentz.
# 
# - Para $D > 50$ nm, $C_\mathrm{sca}$ crece significativamente, superando $C_\mathrm{abs}$ para $D > 80$ nm.
# 
# 

# Este fenómeno se repite en otros metales, aunque con distintas magnitudes y frecuencias de resonancia.

# El efecto de de scattering en nanopartículas metálicas permite explicar el cambio en los colores en la copa de Lycurgus.
# 
# <img src="./images/LycurgusCup.jpg" width="300px" align= center>

# Esta copa del periodo romano, esta compuesta de vidrio con nanopartícula de oro y plata en forma de coloides. 

# ## Referencias
# - Bohren C. and Huffman D. **Chapter 4 - Absorption and Scattering by a Sphere** in *Absorption and Scattering of Light by Small Particles*, 1st Ed, John Wiley & Sons, 1983
# 
# - Jackson. J. D., **Chapter 10 - Scattering and Diffraction** in *Classical Electrodynamics*, 3th Ed, John Wiley & Sons, 1999
