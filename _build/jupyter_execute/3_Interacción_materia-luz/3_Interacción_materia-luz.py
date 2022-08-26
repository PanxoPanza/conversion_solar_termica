#!/usr/bin/env python
# coding: utf-8

#  <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # 3. Interacción materia-luz
# <br><br><br><br>
# Profesor: Francisco Ramírez CueSvas<br>
# Fecha: 26 de Agosto 2022

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
# \ddot{x} - \omega_n^2 x = 0 
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

# La solución homogénea $x_h(t)$, representa la oscilación libre del sistema. Debido al término $e^{-\zeta \omega_n t}$, esta componente decae en el tiempo y se le conoce como **respuesta transciente**. 
# 
# La solución particular $x_p(t)$, por otro lado, representa la vibración en estado estacionario.

# <img src="./images/forced_damped_motion.png" width="400px" align= center>

# Podemos repesentar la amplitud de $x_p = Ae^{i\omega t}$, como $A = |A|e^{i\phi}$, donde $\phi$ es la fase. Asi, la solución estacionaria queda de la forma:
# 
# \begin{equation*}
# x_p = |A|e^{i\left(\omega t + \phi\right)}
# \end{equation*}

# Cuando $\omega/\omega_n = 1$, el sistema entra en resonancia. Esta respuesta se manifiesta con la característica amplificación de $|A|$.
# 
# <img src="./images/resonance.png" width="600px" align= center>

# ## Interacción de luz con moléculas
# ### El oscilador armónico
# Consideremos la molecula de agua.

# <img src="./images/water_molecule.png" width="400px" align= center>

# Esta molécula es del tipo polar, es decir, posee una carga eléctrica neta positiva en un extremo y negativa en otro. Esto ocurre debido a que la densidad de electrónes es mayor en la región cercana al núcleo del oxígeno.

# El enlace entre el hidrógeno y el oxígeno es del tipo covalente. El siguiente modelo representa la energía potencial, $U$ en función de la separación entre los núcleos $r$:

# <img src="./images/covalent_model.png" width="400px" align= center>

# \begin{equation*}
# U(r) = \alpha_0e^{-r/\rho_0} - \frac{q_1q_2}{4\pi\varepsilon_0 r}
# \end{equation*}
# 
# donde $\alpha_0$ y $\rho_0$ son constantes de ajuste, y $q_1$ y $q_2$ son, respectivamente, la carga eléctrica neta negativa y positiva.

# En equilibrio, los núcleos pemanecen en la posición de equilibrio definida por $r_0$

# Se puede demostrar que para oscilaciones pequeñas:
# 
# \begin{equation*}
# U(r)\approx \frac{1}{2} k(r - r_0)^2
# \end{equation*}
# 
# donde $k = \frac{\partial^2 U}{\partial r^2}\big|_{r = r_0}$.

# En otras palabras, la vibración de la molécula de agua puede ser representada como un oscilador armónico, con una fuerza de restauración definida por:
# 
# \begin{equation*}
# F = -k(r - r_0)
# \end{equation*}

# ### Modelo de Lorentz
# Podemos representar la interacción de la molécula con una onda electromagnética como una vibración forzada amortiguada. 

# <img src="./images/molecule_spring_mass.png" width="200px" align= center>

# Para una onda electromagnética de la forma $E_0e^{-i\omega t}$, la fuerza sobre ejercida sobre cada polo es
# 
# \begin{equation*}
# F = qE_0e^{-i\omega t},
# \end{equation*}
# 
# donde $q$ es la carga eléctrica del polo positivo (o negativo). 
# 
# Por otro lado, la amortiguación del sistema surge a raíz de la colición entre los electrones y los nucleos, además de otras interacciónes electromagnéticas.

# Asumiendo un eje de referencia situado en el polo positivo, la ecuación de movimiento está dada por:
# 
# \begin{equation*}
# m\ddot{x} + m\Gamma \dot{x} +  k x = qE_0 e^{-i\omega t},
# \end{equation*}
# 
# donde $m$ es la masa del polo positivo, $k$ es la constante de rigidez del enlace entre los polos, y **$\Gamma$ es la taza de decaimiento** (se mide en unidades 1/s).

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

# Por ejemplo, para $\varepsilon_\infty = 2.0$, $\Gamma = 0.1\omega_n$, y $\omega_p = \omega_n$
# 
# <img src="./images/Lorentz_model.svg" width="800px" align= center>

# >**El modelo de Lorentz se utiliza como modelo de ajuste para representar la interacción de la luz con los modos vibratorios en la materia**

# Por ejemplo, la molécula de agua tiene 3 modos de vibración fundamentales en las longitudes de onda $\lambda = $ 2.98, 2.93 y 5.91 $\mu$m (3351, 3412 y 1691 cm$^{-1}$)

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('1uE2lvVkKW0', width=600, height=400,  playsinline=0)


# El índice de refracción del agua muestra dos oscilaciones de Lorentz. 

# <img src="./images/h2o_nk.svg" width="800px" align= center>

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
# - **Ailante**, donde las bandas de conducción y valencia están muy separadas. El umbral para excitar un electrón a la banda de conducción es demaciado grande y, por lo tanto, el material no es capaz de conducir corriente.

# La respuesta óptica de cada tipo de material está condicionada por sus propiedades electrónicas

# ### Aislantes (modelo de Lorentz)
# Debido a que los electrones en un aislante están fuertemente ligados al núcleo, la respuesta óptica de este material está condicionada por los modos de vibración de la red atómica. Así, la constante dieléctrica y el indice de refración siguen un comportamiento similar al modelo de Lorentz.

# Por ejemplo, el sílice (SiO$_2$)
# 
# <img src="./images/sio2_nk.svg" width="800px" align= center>

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

# En el siguiente ejemplo, $\varepsilon_\infty = 2.0$ y $\Gamma_e = 0.1\omega_p$
# 
# <img src="./images/drude_model.svg" width="800px" align= center>

# Una característica del modelo de Drude es que $\varepsilon' < 0$ para $\omega_p/\omega \gtrsim 1$. Esto se manifiesta en el índice de refracción como $\kappa > n$

# Cuando $\kappa > n$ la reflectividad aumenta significativamente. Así, los materiales conductores tienen alta reflectividad en ambas polarizaciones, cuando $\omega_p/\omega \gtrsim 1$
# 
# <img src="./images/reflectance_drude.svg" width="450px" align= center>

# En general, los metales pueden ser bien representados por el modelo de Drude. Por ejemplo, el aluminio:
# 
# <img src="./images/aluminium_nk.svg" width="800px" align= center>

# Notemos como para $\lambda \approx 0.8$ $\mu$m, la respuesta del material se desvía del modelo de Drude. Esta respuesta esta asociada a un modo de vibración (modelo de Lorentz).

# Además $\omega_p \lesssim 0.1$ $\mu$m, y por lo tanto, refleja todas las longitudes de onda del espectro visible ($\lambda \in [0.38,0.70]$ $\mu$m). Esto explica el efecto espejo del aluminio y otros metales

# ### Semiconductores (absorción interbanda)

# En este caso las interacciones con ondas electromagnéticas están dictadas por bandas de absorción asociadas a la excitación de electrones a la banda de conducción. 
# 
# Este fenómeno se conoce como absorpción interbanda, y ocurre cuando la energía del fotón $\hbar\omega$ ($\hbar = 6.58\times 10^16$ eV$\cdot$s) es superior al bandgap del material.

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
# <img src="./images/gold_color.svg" width="500px" align= center>
# 

# Otro ejemplo es el dioxido de titanio (TiO$_2$), el cual presenta absorción interbanda en el espectro ultravioleta, y oscilaciones de Lorentz en el infrarojo.
# 
# <img src="./images/tio2_nk.png" width="700px" align= center>

# Debido a la absorcion UV, TiO$_2$ es muy utilizado en cremas para protección solar.

# ## Espectro electromagnético

# Podemos clasificar la radiación electromagnética según su longitud de onda (o frecuencia).
# 
# <img src="./images/em_spectrum.png" width="600px" align= center>

# Para este curso, los espectros más importantes son:
# 
# |Espectro| Longitud de onda |Frecuecia | Energía|
# |:-:|:-:|:-:|:-:|
# |UIltravioleta (UV)|1 - 400 nm| 100 - 0.75 PHz|414 - 3.1 eV |
# |Visible (vis)|400 - 750 nm| 750 - 400 THz|3.1 - 1.65 eV |
# |Infrarrojo cercano (near-IR)|750 nm - 1.4 $\mu$m| 400 - 214 THz|3.1 - 1.65 eV |
# |Infrarrojo de onda corta (SWIR)|1.4 - 3 $\mu$m| 214 - 100 THz|885 - 414 meV |
# |Infrarrojo de onda media (MWIR)| 3 - 8 $\mu$m | 100 - 37 THz|414 - 153 meV |
# |Infrarrojo de onda larga (LWIR)| 8 - 15 $\mu$m | 37 -20 THz|153 eV - 82 meV |
# |Infrarrojo de lejano (far-IR)| 15 - 1000 $\mu$m | 20 -0.3 THz|82 - 1.24 meV |

# - 1 eV = $1.602\times 10^{−19}$ J es un **electron volt**. Representa la energía cinética de un electron bajo un potencial de 1 volt.

# El espectro SWIR + MWIR + LWIR se conoce también como **infrarrojo medio (mid-IR)**

# La siguiente tabla es útil para la conversión de unidades:
# 
# | -- |$\lambda$ (nm)|$\lambda$ ($\mu$m)| $\nu$ (Hz) | $\omega$ (rad/s)| $E_{\hbar\omega}$ (eV)|
# |:-:|:------------:|:---------------:|:----------:|:---------------:|:------------:| 
# |$\lambda$ (nm)|--|$$\lambda\cdot 10^{-3}$$|$$\frac{c_0}{\lambda}\cdot 10^9$$|$$\frac{2\pi c_0}{\lambda}\cdot 10^9$$|$$\frac{h c_0}{\lambda}\cdot 10^9$$|
# |$\lambda$ ($\mu$m)|$$\lambda\cdot 10^{3}$$|--|$$\frac{c_0}{\lambda}\cdot 10^6$$|$$\frac{2\pi c_0}{\lambda}\cdot 10^6$$|$$\frac{h c_0}{\lambda}\cdot 10^6$$|
# |$\nu$ (Hz)|$$\frac{c_0}{\nu}\cdot 10^{-9}$$|$$\frac{c_0}{\nu}\cdot 10^{-6}$$|--|$$2\pi\nu$$|$$h\nu $$|
# |$\omega$ (rad/s)|$$\frac{2\pi c_0}{\omega}\cdot 10^{-9}$$|$$\frac{2\pi c_0}{\omega}\cdot 10^{-6}$$|$$\frac{\omega}{2\pi}$$|--|$$\hbar\omega $$|
# |$E_{\hbar\omega}$ (eV)|$$\frac{2\pi\hbar c_0}{E_{\hbar\omega}}\cdot 10^{-9}$$|$$\frac{2\pi\hbar c_0}{E_{\hbar\omega}}\cdot 10^{-6}$$|$$\frac{E_{\hbar\omega}}{2\pi\hbar}$$|$$\frac{E_{\hbar\omega}}{\hbar}$$|--|

# - $h = 4.136\times 10^{−15}$ eV/Hz es la **constante de Planck**.
# - $\hbar = \frac{h}{2\pi} = 6.582\times10^{−16}$ eV/Hz es la **constante reducida de Planck o constante de Dirac**.

# El espectro electromagnético nos sirve como referencia para clasificar el tipo de interacción con la materia. Así, en base a nuestra clásificación de modos de vibración de la materia, en general tenemos:
# 
# - Absorción interbanda: espectro UV y vis
# - $\omega_p$ (modelo de Drude): espectro vis y near-IR
# - $\omega_n$ (modelo de Lorentz): mid-IR

# ## Referencias
# - Rao S. S. **Chapter 4 - Vibration Under General Forcing Conditions** in *Mechanical Vibrations*, 6th Ed, Pearson, 2018
# 
# - Griffths D., **Chapter 4.1 - Polarization** in *Introduction to Electrodynamics*, 4th Ed, Pearson, 2013
# 
# - Simmons J. and Potter K., **Chapter 2 and 3** in *Optical Materials*, 1st Ed, Academic Press, 2000
