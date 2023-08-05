#!/usr/bin/env python
# coding: utf-8

# In[1]:


import importlib.util
if importlib.util.find_spec('empylib') is None:
    get_ipython().system('pip install git+https://github.com/PanxoPanza/empylib.git')


# # Introducción al curso

# ## Utilización del recurso solar
# 
# El sol es la única fuente de energía externa disponible.
# <img src="./images/solar-earth_energy-balance.png" width="800" align= center>

# Si realizamos un balance de energía en la tierra tenemos que, necesariamente, **toda la energía absorbida por el sol ($\dot{E}_\mathrm{sun}$) debe ser rechazada hacia el universo ($\dot{E}_\mathrm{universe}$).** *El efecto del cambio climático es, por consecuencia, el resultado de un desbalance ocacionado por la incapacidad de la tierra de disipar esta energía.*

# \begin{equation*}
# \frac{d}{dt}E_\mathrm{earth} = \dot{E}_\mathrm{sun} - \dot{E}_\mathrm{universe} = 0
# \end{equation*}

# Cuando utilizamos una fuente de energía distina a la solar estamos, entonces, utilizando parte de las reservas acumuladas. **Reservas que también tiene su origen en la energía solar**.

# ## Situación actual del sistema energético

# ### Generación de energía
# 
# A nivel mundial, el consumo de combustibles fósiles sigue en aumento. El siguiente reporte considera el consumo de energía, incluyendo consumo domiciliario, industrial y transporte (aereo, marítimo, etc). Los valores indicados en este gráfico, representan la cantidad de energía equivalente en combustible fósil considerando la [generación por una central termoeléctrica con eficiencia 38.8% - 45%](https://www.energyinst.org/statistical-review/about).

# In[2]:


from IPython.display import display, HTML, IFrame
IFrame('https://ourworldindata.org/grapher/energy-consumption-by-source-and-region?stackMode=absolute', '100%', '600px')


# Respecto a la generación de energía, en Chile se generaron 83 TWh durante el 2022, de los cuales un 55.7% fue generado por fuentes renovables.
# 
# **Participación relativa por fuente de generación (%).** (Fuente: [Generadoras de Chile](http://generadoras.cl/))

# In[3]:


from IPython.display import display, HTML, IFrame
IFrame('https://docs.google.com/spreadsheets/d/e/2PACX-1vSupsaku1SZ9F-OqbhRnZQ7FFAZ4yDnj2FGe8ACY00UCOXgga5PA5Z5Z2Y_wXH-EkLEkcAHTNXmgelW/pubchart?oid=1101314265&amp;format=interactive', '100%', '450px')


# La demanda de combustibles fósiles se ha reducido. Sin embargo, el porcentage de reducción es pequeño.
# 
# **Volumen de energía generada por fuente (GWh).** (Fuente: [Generadoras de Chile](http://generadoras.cl/))
# 
# 

# In[4]:


from IPython.display import display, HTML, IFrame
IFrame('https://docs.google.com/spreadsheets/d/e/2PACX-1vSupsaku1SZ9F-OqbhRnZQ7FFAZ4yDnj2FGe8ACY00UCOXgga5PA5Z5Z2Y_wXH-EkLEkcAHTNXmgelW/pubchart?oid=1025565804&amp;format=interactive', '100%', '450px')


# ### Consumo de reservas
# 
# Como revisabamos en la sección anterior, seguimos utilizando gran parte de las reservas disponibles. Esto, según la *Global Footprint Network*, a una tasa mayor que nuestra capacidad para generarlas. Por ejemplo, **las reservas regeneradas proyectadas para el 2023 se agotaron el 2 de agosto**. Esta fecha, denominada Día de la Sobrecarga de la Tierra o [*Earth overshoot day*](https://www.overshootday.org/) se hace cada año más corta.

# In[5]:


from IPython.display import display, HTML, IFrame
IFrame('https://data.footprintnetwork.org/#/', '100%', '600px')


# ### Manejo de ganancias y pérdidas energéticas
# 
# Por otro lado, tenemos un uso ineficiente de esta energía, principalmente en los sistemas de enfriamiento y calefacción. Según la *international energy agency*, [el consumo de energía para enfriamiento de espacios representa un 10% del consumo global, y puede alcanzar hasta el 50% durante el verano en regiones con temperaturas altas](https://www.iea.org/commentaries/keeping-cool-in-a-hotter-world-is-using-more-energy-making-efficiency-more-important-than-ever). 
# 
# **Consumo eléctrico diario en acondicionamiento de aire versus temperatura en India (mayo y junio, 2019 y 2023)**
# 
# <img src="./images/daily-electricity-load-versus-temperature-in-india-may-and-june-2019-and-2023.png" width="800" align= center>

# En sintesis, podemos deducir que el desarrollo sustentable en la tierra dependerá de nuestra capacidad de:
# 
# - Generar energía directa del sol y otras fuentes renovables
# - Producir reservas con fuentes limpias
# - Manejar el balance entre las ganancias ($\dot{E}_\mathrm{sun}$) y pérdidas ($\dot{E}_\mathrm{universe}$) de energía radiativa.

# ## Tecnologías de manejo y conversión de energía solar

# ### El recurso solar en Chile y el mundo

# Chile es el país con mayores niveles de radiación en el mundo. Por ejemplo, en base al atlas solar del [World Bank Group](https://globalsolaratlas.info/map?c=11.523088,8.261719,3), si calculamos la energía generada por el área con mayores niveles de radiación considerando paneles con [potencia máxima de 500 Wp](https://solarity.cz/blog/500-wp-solar-modules-era/)

# In[6]:


A     = 304707.40 # Superficie total (km^2)
Pmax  = 500       # Potencia máxima por panel en condiciones estándard (Wp)
PVOUT = 6.0       # Potencía específica suministrada (kWh/Wp)

# Energía total suministrada (TWh)
Etot  = A*1E3**2*PVOUT*Pmax/1E12
print("Energía eléctrica suministrada: %.1f TWh (Energía consumida en Chile 444 TWh)" % Etot)


# > "*Para abastecer toda la energía que requiere Chile si tuviéramos almacenamiento suficiente necesitamos unos mil kilómetros cuadrados, algo menos que el 1% del desierto y equivalente más o menos a la superficie de la comuna de Melipilla.*"  [Rodrigo Palma, director de SERC, 2022](https://www.revistaei.cl/2019/09/04/con-todo-el-potencial-de-energia-solar-de-chile-se-podria-abastecer-60-veces-el-consumo-del-pais-y-el-20-del-mundo/#)

# Sin embargo, como revisamos anteriormente, estos áltos niveles de radiación implican un calentamiento excesivo en hogares durante el verano.

# ### Tecnologías convencionales
# Las principales tecnologías son la fotovoltaica y termosolar. En Chile, [la capacidad instalada total es de 4.6 GW](https://www.pv-magazine-latam.com/2021/04/13/chile-alcanza-46-gw-fotovoltaicos-de-potencia-instalada/). Con excepción de la planta termosolar Cerro Dominador, la mayor parte de este simunistro corresponde a plantas solares fotovoltaicas.

# <img src="./images/planta_fotovoltaica_ElRomero_chile.jpg" width="500" align= center>
# 
# <center><a href="https://www.acciona.cl/proyectos/planta-fotovoltaica-romero-solar/">Planta fotovoltaica El Romero Solar (196 MW)</a></center>

# <img src="./images/cerro_dominador.jpg" width="500" align= center>
# 
# <center><a href="https://laderasur.com/articulo/recorriendo-cerro-dominador-la-unica-planta-termosolar-que-funciona-en-medio-del-desierto-de-atacama/">Planta termosolar cerro dominador (110 MW)</a></center>

# ### Estado del arte de las tecnologías convecionales
# Las actuales tecnologias basadas en energía solar (principalmente fotovoltaica y termosolar) presentan una serie de deseventajas, tales como:

# - **Baja eficiencia.** Hoy en día la eficiencia de un panel fotovoltaico es cercana al 30%. En el caso de una central termosolar, la eficiencia es menor al 20%.
# 
# - **Almacenamiento de energía limitado.** Esto particularmente en centrales fotovoltaicas. Si bien, las centrales termosolares pueden almacenar energía hasta por 24 horas, el costo nivelado de esta energía es superior a la energía por combustibles fósiles. Similar con el costo de almacenamiento por hidrógeno.
# 
# - **Limitada capacidad de reutilización.** Los paneles fotovoltaicos, la principal tecnología de conversión solar, tienen una vida útil promedio de 25 años. Luego de esto, la recuperación de los componentes es aún compleja y costosa.
# 
# - **Manejo ineficiente de la energía.** En hogares y oficinas, el control de las ganancias y pérdidas de calor por radiación es aún deficiente.([El consumo de aire acondicionado en edificios representa el 20% del consumo total](https://www.iea.org/reports/the-future-of-cooling))

# ### Tecnologías emergentes
# 
# La investigación en tecnologías de conversión y manejo del recurso solar ha avanzado en diversas direcciones. Algunos ejemplos relevantes son:

# 
# <img src="./images/emerging_solar_energy_conversion.png" width="600" align= center>

# <img src="./images/solar_fuels.png" width="600" align= center>

# ## Nanotecnología para el control de la radiación
# 
# El control de la radiación solar es clave en aspectos, tales como, mejorar la captura de energía solar o reducir el consumo de energía para enfriamiento y calefacción

# El desarrollo de la manufactura de nanomateriales ha prograsado significativamente en las últimas décadas. Hoy en día, es común encontrar nanoestructuras en dispositivos electrónicos, productos cosméticos, entre otros.
# 
# <img src="./images/transistor_evolution.png" width="800" align= center>

# Esta manipulación de estructuras a escala nanométrica, deriva en materiales articiales con propiedades ópticas que permiten optimizar el intercambio de energía por radiación.
# 
# <img src="./images/photonic_nanostructures.png" width="800" align= center>
