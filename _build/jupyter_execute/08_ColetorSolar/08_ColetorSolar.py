#!/usr/bin/env python
# coding: utf-8

# # Colectores solares estacionarios
# 

# In[ ]:





# ## Introducción
# 
# Los colectores solares son un tipo especial de intercambiador de calor que absorbe la radiación solar, la convierte en calor y la transfiere a un fluido (usualmente agua, aire, o aceite). que fluye a través del colector.

# Podemos clasificar a los colectores solares en dos tipos:
# - **Colectores estacionarios.** Corresponde a colectores de eje fijo.
# 
# - **Colectores con concentración solar.** Se caracterizan por poseer superficies convacavas para interceptar la luz solar y concentrarla en un área de absorción de menor tamaño. Estos colectores son equipados con un sistema de rastreo solar (eje móvil), para maximizar la captura de radiación solar.

# Los colectores sin concentración son generalmente utilizados en aplicaciones que requieren calentar un fluido a temperaturas menores al punto de ebullición, ya sea para consumo domiciliario o calefacción. Los colectores con concentración, en cambio, permiten conseguir altas temperaturas, y se utilizan en plantas de generación de energía a través de un ciclo térmico.

# En la siguiente tabla, presentamos una lista de los colectores solares más comúnes clasificados por el tipo de movimiento del eje. Esto es: 
# - Estacionario
# - Rastreo solar por un eje (un grado de libertad)
# - Rastreo solar por dos ejes (dos grados de libertad)

# <img src="./images/solar_collector_types.png" width="600" align= center>

# En esta unidad revisaremos los aspectos generales de los colectores estacionarios.

# Los más comunes son:
# - Colector solar de placa plana (*Flat-plate collector* o FPC)
# - Colector parabólico compuesto (*Compound parabolic collector* o CPC)
# - Colector de tubo evacuado (*Evacuated tube collector* o ETC)

# ### Colectores de placa plana (FPC)

# <img src="./images/flat_plate_collector_parts.png" width="900" align= center>
# 
# Los colectores de placa plana se componen de un **absorbedor (*absorbing blackplate*)** para capturar la radiación solar. La energía absorbida es transferida a un fluido que circula por pequeños **tubos ascendentes (*riser pipes*)** en contacto directo con el absorbedor. Las entradas y salidas del fluido son capturadas por **tubos de cabecera (*header pipes*)** en la parte inferior y superior, respectivamente. Las partes laterales e inferior del colector están recubiertas con **aislante térmico** para reducir las pérdidas de calor. En la parte superior se utiliza una **cubierta transparente (*glazing sheet*)** para reducir las pérdidas por convección y radiación.

# Los FPC son los colectores más comunes en el mercado debido a su bajo costo. Permiten capturar las componentes especular y difusa de la radiación solar, y logran temperaturas de operación entre 30 y 80° C

# ### Colector parabólico compuesto (CPC)

# <img src="./images/compound_parabollic_collector.png" width="900" align= center>
# 
# El Colector Parabólico Compuesto (CPC) está constituido de 2 superficies parabólicas que reflejan los rayos solares hacia una superficie absorvedora. Los CPC permiten una tolerancia de ángulos de incidencia relativamente amplia. Aunque la concentración de luz es mayor que los colectores de placa plana, el rango de ángulos de incidencia es menor adimisibles es menor.

# El absorbedor puede estar dispuesto en distintas configuraciones, tales como: plano, bifacial, en forma me cuña o cilíndrico. 
# <img src="./images/CPC_configuration.png" width="700" align= center>

# El absorbedor también puede estar dispuesto de forma asimétrica, ocupando un punto superior en la geometría del colector.
# <img src="./images/CPC_asymmetric.png" width="600" align= center>

# ### Colector de tubo evacuado (ETC)
# 
# Los colectores de tubo evacuados, consisten en una serie de **tubos trasparentes sellados al vacío**, cada uno con un **absorbedor de radiación** conectado a un **tubo central** que transporta el fluido. El vacío actúa como asilante térmico frente a las pérdidas de calor por convección y conducción, permitiendo operar a mayores temperaturas que los FPC. Cada tubo evacuado contiene un fluido con cambio de fase líquido-vapor. En la parte superior, se ubica un condensador, a través del cual se produce la transferencia de calor hacia el fluido a calentar.

# <img src="./images/evacuated_tube_collectors.png" width="1000" align= center>

# Al igual que los FPC los ETC permiten capturar la componente especular y difusa de la radiación solar. Sin embargo, la eficiencia de los ETC es mayor en ángulos de incidencia bajos. Así, los ETC son preferibles en climas caracterizados por alta nuvosidad y viento

# <img src="./images/ETC_vs_FPC.png" width="800" align= center>

# ## Componentes de un colector de placa plana

# ### Cubierta de transparente
# La **cubierta transparente** generalmente está compuesta de vídrio (sílice) con bajo contenido de óxido de hierro (Fe$_2$O$_3$). El vídrio común utilizado en ventanas tiene altos niveles de Fe$_2$O$_3$ que reducen la tranparencia en el infrarojo medio y parte del visible.

# <img src="./images/transmitance_glass.png" width="450" align= center>

# Esta cubierta se ubica cerca del absorbedor para generar una pequeña capa de aire estancado, el cual actúa como aislante térmico ante la convección de calor del exterior.

# Por otro lado, materiales como el sílice, poseen alta emisividad en el infrarojo medio (mid-IR). Al igual que con el efecto invernadero, esta propiedad permite capturar la radiación emitida por el absorbedor caliente, minimizando las pérdidas de calor por radiación.

# Algunos diseños consideran más de una cubierta transparente para reducir aún más las pérdidas de calor.

# ### Placa absorbedora
# 
# El **absorbedor** debe cumplir con dos requerimientos. Por un lado, debe absorber la mayor cantidad de radiación solar posible ($\alpha \approx 1$ en el espectro visible e infrarojo medio). Por el otro, debe minimizar las pérdidas de calor por radiación ($\varepsilon \approx 0$ en el espectro infrarojo medio) 

# En otras palabras, el absorbedor debe operar como un ***absorbedor selectivo***, con una absorptancia variable en el espectro.
# 
# <img src="./images/selective_absorber.png" width="500" align= center>

# Comúnmente, estas superficies están compuestas de una pequeña capa superior con alta absorptancia en el espectro visible y near-IR, pero relativamente transparente en el espetro mid-IR, depositada sobre un substrato metálico con alta reflectancia en el espectro visible y mid-IR.

#  Un ejemplo es el absorbedor compuesto por cromo negro depositado sobre una superficie de niquel.

# ### Integración de componentes

# Los **tubos ascendentes** deben estar integrados en el absorbedor, o bien, unidos mediante soldaduras o sujetadores. En último caso es importante que la unión minimice la resistencia térmica en el contacto entre los tubos y el absorbedor.

# ## Análisis térmico de colectores de placa plana

# ### Absorción de radiación solar
# 
# Utilizando el modelo de cielo isotrópico, la radiación solar absorbida por un colector, $S$, puede aproximarse por:

# \begin{equation}
# S = G_\mathrm{GHI}R_\mathrm{B}(\tau \alpha)_\mathrm{B}+G_\mathrm{DIF}(\tau \alpha)_\mathrm{D}\left[\frac{1+\cos\beta}{2}\right]+\rho_\mathrm{G}(G_\mathrm{GHI} + G_\mathrm{DIF})(\tau \alpha)_\mathrm{G}\left[\frac{1-\cos\beta}{2}\right]
# \end{equation}
# 
# Donde:
# - $G_\mathrm{GHI}$: Irradiación global horizontal (GHI) del sol (W/m$^2$)
# - $G_\mathrm{DIF}$: Irradiación horizontal difusa (DIF) del sol (W/m$^2$)
# - $R_\mathrm{B} = \frac{\cos\theta_i}{\cos\theta_s}$: Factor de inclinación de radiación directa.
# - $\beta$: Ángulo cenital de inclinación del colector.
# - $\rho_\mathrm{G}$ reflectancia del suelo
# - $(\tau\alpha)$: Fracción de la radiación absorbida por el colector. Los subíndices $\mathrm{B}$, $\mathrm{D}$ y $\mathrm{G}$, indican el valor correspondiente a la componente directa (*beam*), difusa y del suelo (*ground*).

# >El parámetro $(\tau\alpha)$ debe ser considerado com una propiedad de la combinación *conbertura - absorbedor*, y no como el producto de la transmitancia y absortancia.

# El valor de $(\tau\alpha)$ considera las múltiples reflecciones y absorciones ocurridas entre la covertura transparente y el absorbedor del colector.

# 
# <img src="./images/FPC_internal_reflection.png" width="500" align= center>

# La componente normal de este parámetro está dada por:
# 
# \begin{equation}
# (\tau\alpha)_n=\tau\alpha\sum_{n=1}^\infty \left[(1-\alpha)\rho_\mathrm{D}\right]^n = \frac{\tau\alpha}{1 - (1 - \alpha)\rho_\mathrm{D}}
# \end{equation}
# 
# donde:
# - $\tau$ transmitancia de la cubierta transparente
# - $\alpha$ absortancia de la placa absorbedora
# - $ \rho_D$ es la reflectancia difusa de la cubierta transparente. En genral, $\rho_D \sim 0.11 - 0.15$

# Valores típicos para $(\tau\alpha)$ son 0.7 - 0-75 en vidrio para ventanas, y 0.85-0.9 en vidrio con bajo contenido de Fe$_2$O$_3$

# Para determinar $(\tau \alpha)_\mathrm{B}$, $(\tau \alpha)_\mathrm{D}$ y $(\tau \alpha)_\mathrm{G}$ utilizamos el siguiente gráfico que permite relacionar $(\tau \alpha)_n$ respecto al ángulo de incidencia $\theta_i$

# <img src="./images/Incident_angle_correction.png" width="500" align= center>

# En el caso de  $(\tau \alpha)_\mathrm{D}$ y $(\tau \alpha)_\mathrm{G}$, utilizamos las siguientes fórmulas para determinar el ángulo equivalente de la componente difusa, $\theta_\mathrm{e,D} $, y global, $\theta_\mathrm{e,G}$:
# 
# \begin{align}
# \theta_\mathrm{e,D} &= 59.68 - 0.1388\beta+0.001497\beta^2 \\
# \theta_\mathrm{e,G} &= 90 - 0.5788\beta+0.002693\beta^2
# \end{align}

# ### Pérdidas de energía
# Las pérdidas de energía, $Q_\mathrm{loss}$, están asociadas a las perdidas por convección, conducción y radiación desde la placa absorbedora hacia el medio exterior

# Matemáticamente:
# \begin{equation*}
# Q_\mathrm{loss} = S - Q_u
# \end{equation*}
# 
# donde $Q_u$ es el calor transferido al fluido.

# Para determinar $Q_\mathrm{loss}$ analicamos la red de resistencias considerando los diferentes componentes del colector

# <img src="./images/collector_energy_losses.png" width="350" align= center>

# Donde $h_\mathrm{c,~i-j}$ es el coeficiente convectivo entre dos superficies $i$ y $j$, y
# 
# \begin{equation*}
# h_\mathrm{r,~i-j} = \frac{\sigma(T_i - T_j)(T_i^2 + T_j^2)}{1/\varepsilon_i + 1/\varepsilon_j - 1},
# \end{equation*}
# 
# es el coeficiente equivalente de transferencia de calor por radiación.

# Notar que $h_\mathrm{r,~i-j}$ depende de la temperatura de los elementos participantes, aún cuando el resto de las propiedades permanezcan constantes.

# En la práctica las pérdidas de calor se asocian a un coeficiente global de transferencia de calor, $U_L$, de la forma:

# \begin{equation}
# Q_\mathrm{loss} = U_L A_c(T_p - T_a)
# \end{equation}
# 
# donde, $T_p$ y $T_a$ corresponden, respectivamente, a la temperaturas de la placa absorbedora y el ambiente, y $A_c$ es la superficie superior(inferior) del colector.

# <img src="./images/collector_energy_losses_eqcircuit.png" width="150" align= center>

# El coeficiente global $U_L$ depende mayormente del diseño del colector.

# Los valores de $U_L$ son determinados por el fabricante.

# ## Rendimiento de colectores de placa plana

# ### Factor de remoción de calor
# 
# En la práctica $T_p$ es dificil de determinar, así la ecuación de $Q_\mathrm{loss}$ planteada anteriormente no es de uso práctico

# Definimos el factor de remoción de calor, $F_R$, como la razón entre el calor real transferido al fluído de trabajo ($Q_u$), y la energía transferida por el colector cuando la temperatura de la placa absorbedora es igual a la temperatura de entrada del fluído de trabajo, $T_\mathrm{f,i}$.

# Matemáticamente:
# 
# \begin{equation}
# F_R = \frac{\dot{m}C_p(T_\mathrm{f,o} - T_\mathrm{f,i})}{A_c[S - U_L(T_\mathrm{f,i} - T_a)]}
# \end{equation}

# donde $C_p$, $\dot{m}$ y $T_\mathrm{f,o}$ son, respectivamente, el calor específico, el flujo másico y la temperatura de salida del fluido de trabajo.

# **El parámetro $F_R$ depende del diseño del colector, el tipo de fluido, y el flujo a través del colector.** Puede ser determinado de forma teórica o experimental.

# Conceptualmente, el factor de remoción de calor es similar a la efectividad de un intercambiador de calor, el cual considera el calor transferido respecto al máximo calor transferible por el intercambiador.

# En el caso del colector, a menor temperatura de la placa absorbedora, menor las pérdidas asociadas a $U_L(T_p - T_a)$

# La mínima temperatura posible para la placa absorbedora es $T_\mathrm{f,i}$, y por lo tanto $A_c[S - U_L(T_\mathrm{f,i} - T_a)]$ representa el máximo calor que puede ser transferido por el colector.

# A partir de este parámetro podemos determinar el calor efectivo transferido a un fluido como:
# 
# \begin{equation}
# Q_u = A_cF_R\left[S - U_L\left(T_\mathrm{f,i} - T_a\right)\right]
# \end{equation}

# ### Eficiencia térmica
# La eficiencia térmica de un colector corresponde al calor trasferido al fluido divido por la irradiación total, $G_t$, sobre la superficie del colector, $A_c$:
# 
# \begin{equation}
# \eta = F_R\left[\frac{S - U_L(T_\mathrm{f,i} - T_a)}{G_t}\right]
# \end{equation}
# 
# 

# ### Curvas de rendimiento
# $F_R$, y por consecuencia $\eta$, son dependientes de muchos factores, como las condiciones del flujo, el tipo de fluido, el tipo de colector y la irradiancia solar. Debido a esto, es común que los fabricantes realicen ensayos de desempeño del colector para una serie de casos. 

# Existen diversos estandares para evaluar el rendimiento de un colector. Los más comunes son la [ISO 9806](https://www.iso.org/standard/67978.html) y la [ASNI/ASHRAE 93](https://webstore.ansi.org/Standards/ASHRAE/ansiashraestandard932010).

# En cualquiera de los dos casos, el objetivo de estos es medir el rendimiento de un colector en condiciones estacionarias, radiación normal a la superficie del colector, y en función de la temperatura de entrada del fluido de trabajo ($T_i$)

# Bajo estas condiciones de trabajo, los parámetros $F_RS/G_t$  y $F_RU_L$ permanecen constantes.

# Más aún, para radiación solar normal a la superficie del colector, $S = (\tau\alpha)_nG_t$. Así, la eficiencia térmica forma una recta de la forma:

# \begin{equation*}
# \eta = F_R(\tau\alpha)_n - F_RU_L\frac{\Delta T}{G_t}
# \end{equation*}
# 
# donde $\Delta T= (T_\mathrm{f,i} - T_a)$

# <img src="./images/eficiency_curve_flatplate_collector.png" width="250" align= center>

# A través de estas curvas podemos determinar el valor de $F_R(\tau\alpha)_n$ y $F_R U_L$.

# El valor espéctifico de $U_L$, $F_R$ y $(\tau\alpha)_n$, se puede determinar con la información de uno de los tres parámetros. 

# En la práctica, el coeficiente de pérdida de calor $U_L$ no es constante, sino que depende de $\Delta T$ de la forma, $U_L = c_1 + c_2\Delta T$.

# Esto implica que el comportamiento de las curvas de eficiencia no es exáctamente una recta.

# En el siguiente ejemplo mostramos una curva de eficiencia de un colector de placa plana del fabricante Schüco

# <img src="./images/real_flat_plate_collector.png" width="600" align= center>

# Las curvas de eficiencia varían para distintos colectores, y sirven como método de pre-selección según la aplicación requerida. La mejor forma es identificar el parametro $\Delta T/G$ asociado a las condiciones locales y la demanda, y luego evaluar seleccionar el sistema mas adecuado, como se indica en la figura.

# <img src="./images/collector_selection.png" width="500" align= center>

# Sin embargo, la selección final depende de un estudio más exhaustivo, que considere la operación del sistema completo en función de las condiciones climáticas y consumo a lo largo de un año. Para esto existen heramientas especializadas, tales como [TRNSYS](https://www.trnsys.com/).

# ### Corrector de ángulo de incidencia
# Las curvas de rendimiento son generadas mediante un ensallo con radiación solar normal al plano de incidencia. En la realidad, esto nunca sucede debido que el colector solar está en posición estacionaria.

# Así, en la práctica, necesitamos un factor de correción que nos permita identificar el rendimiento del colector respecto al ángulo de incidencia de la radiación solar, $\theta_i$. Este corrector se conoce como el **modificador del ángulo de incidencia, $K_\theta$**.
# 
# \begin{equation}
# K_\theta = \frac{(\tau\alpha)}{(\tau\alpha)_n}=1 - b_0\left[\frac{1}{\cos\theta_i} - 1\right]
# \end{equation}
# 
# donde $b_0\sim 0.1  - 0.15$.

# Considerando el factor $K_\theta$, la curva de eficiencia corregida es:
# 
# \begin{equation}
# \eta = F_R(\tau\alpha)_n K_\theta(\theta_i) - F_RU_L\frac{\Delta T}{G_t}
# \end{equation}

# ## Sistemas de calentamiento de agua solar
# 
# Una de las aplicaciones más común en colectores solares es el calentamiento de agua para uso doméstico.

# Un sistema de calentamiento de agua solar se compone de un arreglo de colectores, un sistema de transferencia de energía térmica y un tanque de almacenamiento

# Debido a que estos sistemas están mayormente expuestos al ambiente, deben estar protegidos contra el congelamiento en el invierno, o sobrecalentamiento durante el verano en periodos cuando la demanda de agua caliente es baja.

# Podemos clasificar estos sistemas en dos tipos:
# 
# - **Sistemas de circuito abierto**, donde el agua potable es directamente calentada por el colector
# 
# - **Sistemas de circuito cerrado**, donde el agua potable es calentada indirectamente a través de un intercambiador de calor por donde circula el fluido de trabajo calentado por el colector solar.

# También podemos clasificar los sistemas respecto a la forma en que se mueve el fluido de trabajo. En esta clasificación tenemos:
# 
# - **Sistemas pasivos,** donde el fluido de trabajo es impulsado por convección natural, a través del efecto termosifón.
# 
# - **Sistemas activos** donde el fluido de trabajo es impulsado sistemas de bombeo.

# 
# ### Sistemas pasivos

# El sistema más utilizado es el colector solar con sistema termosifón. El sistema esta basado en un colector solar y un estanque de almacenamiento sobre el colector.
# 
# <img src="./images/passive_water_heating.png" width="800" align= center>

# El efecto termosifón ocurre debido a la disminución de la densidad del fluido de trabajo a medida que se calienta. Esto produce que el fluido caliente ascienda por los tubos hacia el estanque de reserva. Por otro lado, el fluido más frio asciende por diferencia de preciones ocupando el espacio disponible en el colector.

# Debido a que estos sistemas no necesitan bombeo, son menos costosos y tienen una vida util mayor que los sistemas activos, ya que requieren menos mantención.

# La principal desventaja es su diseño bultoso, que ocupa mucho espacio y no es esteticamente agradable. Además, debido a que no es posible controlar el flujo en el colector, estos sistemas tienen a ser menos eficientes que los sitemas activos.

# Las configuraciones más comunes consideran colectores del tipo FPC o ETC.

# El sistema puede operar en circuito abierto, o cerrado.

# ### Sistemas activos
# 
# Los sistemas activos son, en general, de mayor costo que los sistemas pasivos. Además requieren de más espacio para el sistema de bombeo.

# Sus principales ventajas están asociadas al mejor control del caudal, lo que permite maximizar la eficiencia del colector. Además está el aspecto estético, ya que el tanque de almacenamiento puede ser instalado en un lugar separado del colector.

# El sistema puede operar en circuito abierto o cerrado. En ambos casos, una bomba, controlada por un termostato, es activada cada vez que la temperatura del agua a la salida del colector es mayor a la temperatura del estanque de almacenamiento. El estanque de almacenamiento comúnmente incluye un calefactor auxiliar para evitar caidas abrutas de la temperatura del agua.

# La siguiente figura muestra un sistema activo de tipo abierto.
# 
# <img src="./images/active_direct.png" width="600" align= center>

# ## Referencias
# Kalogirou S. A. ***Solar Energy Engineering Processes and Systems***, 2nd Ed, Academic Press, 2014
#  - Chapter 3 Solar energy collectors
#  - Chapter 4 Performance of solar collectors
#  - Chapter 5 Solar water-heating systems
# 
# Duffie J. A., Beckman W. A. and Blair N. ***Solar Engineering of Thermal Processes***, 5th Ed, Jhon Wiley and Sons, 2020
#  - Chapter 4. Radiation characteristi of opaque materials
#  - Chapter 5. Radiation transmission through glazing: Absorbed radiation
#  - Chapter 6. Flat-plate collectors
#  - Chapter 12. Solar water-heating: active and passive
