#!/usr/bin/env python
# coding: utf-8

# # Introducción al curso

# ## Situación actual del sistema energético

# In[1]:


from IPython.display import display, HTML, IFrame
IFrame('https://ourworldindata.org/grapher/energy-consumption-by-source-and-region?stackMode=absolute', '100%', '600px')


# **Datos relevantes**
# - El consumo mundial de combustibles fósiles (petróleo, gas y carbón) a aumentado en casi 65% desde el año 1990 hasta el año 2021.
# - El porcentaje de energía proveniente de combustibles fósiles, ha disminuido de casi un 87% en 1990 a 83% en el 2021 (en Chile, este porcentaje cayó desde 82% a 76.5%).
# - Actualmente en Chile, las energías renovables representan un 23.5%, donde un 6.25% proviene de energía solar.

# >Por otro lado, **la disponiblidad de combustilbes fósiles es limitada**. Segun estudios ´[las reservas de petroleo, gas y carbón se agotarán para los años 2052, 2060 y 2090, respectivamente.](https://earthbuddies.net/when-will-we-run-out-of-fossil-fuel/)
# 
# >Esto significa que los precios de los combustibles fósiles seguirán aumentando en las próximas décadas.

# ## Problemas ambientales asociados al sistema energético actual
# Como vimos, aunque el consumo de energías renovables ha ido en aumento, la quema de combustibles fósiles sigue siendo la principal fuente de energía en el mundo.

# Además de los problemas asociados a la disponibilidad limitada y aumento de precio de los combustibles fósiles, existen consecuencias medioambientales que tienen asociado un costo indirecto, tales como:
# - Lluvia ácida asociada a la emisión de SO$_2$ y NO$_x$
# - Disminución de la capa de ozono por emisión de CFC y NO$_x$. (*Aunque se han tomado una serie de medidas para reducir las emisiones de CFC, se estima que el daño en zonas como la Antartica seguirá presenta hasta, al menos, el año 2075.*)
# - Cambio climático producto del aumento de gases de efecto invernadero

# ## Tecnologías de manejo y conversión de energía solar

# ### Aspectos generales de la energía solar
# - El sol es la única fuente externa de energía en la tierra
# - Todas la formas de energía disponibles tiene origen solar (combustibles fósiles, mareomotríz, eólica, etc)

# ### Disponibilidad de energía solar
# 

# In[2]:


IFrame('https://globalsolaratlas.info/map','100%','600px')


# Chile es el país con mayores niveles de radiación en el mundo. 
# 
# Por ejemplo, en base al atlas solar del [World Bank Group](https://globalsolaratlas.info/map?c=11.523088,8.261719,3), si calculamos la energía generada por el área con mayores niveles de radiación considerando paneles con [potencia máxima de 500 Wp](https://solarity.cz/blog/500-wp-solar-modules-era/)

# In[3]:


A     = 304707.40 # Superficie total (km^2)
Pmax  = 500       # Potencia máxima por panel en condiciones estándard (Wp)
PVOUT = 6.0       # Potencía específica suministrada (kWh/Wp)

# Energía total suministrada (TWh)
Etot  = A*1E3**2*PVOUT*Pmax/1E12
print("Energía eléctrica suministrada: %.1f TWh (Energía consumida en Chile 444 TWh)" % Etot)


# > "*Para abastecer toda la energía que requiere Chile si tuviéramos almacenamiento suficiente necesitamos unos mil kilómetros cuadrados, algo menos que el 1% del desierto y equivalente más o menos a la superficie de la comuna de Melipilla.*"  [Rodrigo Palma, director de SERC, 2022](https://www.revistaei.cl/2019/09/04/con-todo-el-potencial-de-energia-solar-de-chile-se-podria-abastecer-60-veces-el-consumo-del-pais-y-el-20-del-mundo/#)

# ### Principales de tecnologías para conversión y manejo  de energía solar

# **Tecnologías conversionales**
# 
# <img src="./images/fotovoltaica_termosolar.png" width="600" align= center>

# **Tecnologías emergentes**
# 
# <img src="./images/emerging_solar_energy_conversion.png" width="600" align= center>

# **Combustibles solares**
# 
# <img src="./images/solar_fuels.png" width="600" align= center>

# ### La energía solar en Chile
# En Chile las principales tecnologías son la fotovoltaica y termosolar, [con una capacidad instalada total de 4.6 GW](https://www.pv-magazine-latam.com/2021/04/13/chile-alcanza-46-gw-fotovoltaicos-de-potencia-instalada/). Con excepción de la planta termosolar Cerro Dominador, la mayoría de este simunistro corresponde a plantas solares fotovoltaicas, de las cuales la más grande es El Romero Solar.

# <img src="./images/planta_fotovoltaica_ElRomero_chile.jpg" width="500" align= center>
# 
# <center><a href="https://www.acciona.cl/proyectos/planta-fotovoltaica-romero-solar/">Planta fotovoltaica El Romero Solar (196 MW)</a></center>

# <img src="./images/cerro_dominador.jpg" width="500" align= center>
# 
# <center><a href="https://laderasur.com/articulo/recorriendo-cerro-dominador-la-unica-planta-termosolar-que-funciona-en-medio-del-desierto-de-atacama/">Planta termosolar cerro dominador (110 MW)</a></center>

# ### Estado del arte de las tecnologías de conversión y manejo de energía solar
# Las actuales tecnologias basadas en energía solar (principalmente fotovoltaica y termosolar) presentan una serie de deseventajas:

# - **Baja eficiencia.** *Hoy en día la eficiencia de un panel fotovoltaico es cercana al 30%. En el caso de una central termosolar, la eficiencia es menor al 20%.* 

# 
# 
# - **Almacenamiento de energía limitado.** *Esto particularmente en centrales fotovoltaicas. Si bien, las centrales termosolares puede almacenar energía hasta por 24 horas, el costo nivelado de esta energía es superior a la energía por combustibles fósiles. Similar con el costo de almacenamiento por hidrógeno.* 

# - **Limitada capacidad de reutilización.** *Los paneles fotovoltaicos, la principal tecnología de conversión solar, tienen una vida útil promedio de 25 años. Luego de esto, la recuperación de los componentes es aún compleja y costosa.*

# - **Manejo infeciente de la energía.** *Además de fuentes de energía renovables, un desarrollo sustentable también requiere un manejo eficiente de la energía. Particularmente en hogares y oficinas, el control de las ganancias y pérdidas de calor por radiación es aún deficiente.*

# ## Manejo de la radiación solar
# 
# El control de la radiación solar es clave en aspectos, tales como, mejorar la captura de energía solar o reducir el consumo de energía para enfriamiento y calefacción

# ### Espectros de energía radiativa
# 
# El sol y, en general, todos los cuerpos a temperaturas sobre 0K emiten radiación, la cual está compuesta de ondas electromagnéticas con un amplio espectro de longitudes de onda.
# <img src="./images/thermal_radiation_spectra.png" width="450" align= center>

# Cada región del espectro genera una respuesta particular en los materiales. El adecuado manejo de este espectro es, así, fundamental para el aprovechamiento eficiente de la energía solar.

# ### Nanotecnología para el control de la radiación

# El desarrollo de la manufactura de nanomateriales ha prograsado significativamente en las últimas décadas. Hoy en día, es común encontrar nanoestructuras en dispositivos electrónicos, productos cosméticos, entre otros.
# 
# <img src="./images/transistor_evolution.png" width="500" align= center>

# Esta manipulación de estructuras a escala nanométrica, deriva en materiales articiales con propiedades ópticas que permiten optimizar el intercambio de energía por radiación.
# 
# <img src="./images/photonic_nanostructures.png" width="500" align= center>
