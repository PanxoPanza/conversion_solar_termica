#!/usr/bin/env python
# coding: utf-8

# <font size="6">MEC501 - Manejo y Conversión de Energía Solar Térmica</font>
# # Introducción al curso
# <br><br><br><br>
# Profesor: Francisco Ramírez Cuevas<br>
# Fecha: 1 de Agosto 2022

# <h1>Tabla de contenidos<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Situación-actual-del-sistema-energético" data-toc-modified-id="Situación-actual-del-sistema-energético-1">Situación actual del sistema energético</a></span></li><li><span><a href="#Problemas-medioambientales-asociados-al-sistema-energético-actual" data-toc-modified-id="Problemas-medioambientales-asociados-al-sistema-energético-actual-2">Problemas medioambientales asociados al sistema energético actual</a></span></li><li><span><a href="#Tecnologías-de-manejo-y-conversión-de-energía-solar" data-toc-modified-id="Tecnologías-de-manejo-y-conversión-de-energía-solar-3">Tecnologías de manejo y conversión de energía solar</a></span><ul class="toc-item"><li><span><a href="#Aspectos-generales-de-la-energía-solar" data-toc-modified-id="Aspectos-generales-de-la-energía-solar-3.1">Aspectos generales de la energía solar</a></span></li><li><span><a href="#Disponibilidad-de-energía-solar" data-toc-modified-id="Disponibilidad-de-energía-solar-3.2">Disponibilidad de energía solar</a></span></li><li><span><a href="#Descripción-de-tecnologías-para-energía-solar" data-toc-modified-id="Descripción-de-tecnologías-para-energía-solar-3.3">Descripción de tecnologías para energía solar</a></span></li><li><span><a href="#Tecnologías-en-base-a-energía-solar-en-Chile" data-toc-modified-id="Tecnologías-en-base-a-energía-solar-en-Chile-3.4">Tecnologías en base a energía solar en Chile</a></span></li></ul></li><li><span><a href="#Descripción-general-de-la-asignatura" data-toc-modified-id="Descripción-general-de-la-asignatura-4">Descripción general de la asignatura</a></span><ul class="toc-item"><li><span><a href="#Objetivos-generales" data-toc-modified-id="Objetivos-generales-4.1">Objetivos generales</a></span></li><li><span><a href="#Objetivos-específicos" data-toc-modified-id="Objetivos-específicos-4.2">Objetivos específicos</a></span></li></ul></li><li><span><a href="#Temario" data-toc-modified-id="Temario-5">Temario</a></span><ul class="toc-item"><li><span><a href="#Contenidos" data-toc-modified-id="Contenidos-5.1">Contenidos</a></span></li></ul></li><li><span><a href="#Evaluación-de-la-asignatura" data-toc-modified-id="Evaluación-de-la-asignatura-6">Evaluación de la asignatura</a></span></li></ul></div>

# ## Situación actual del sistema energético

# In[1]:


from IPython.display import display, HTML, IFrame
display(IFrame('https://ourworldindata.org/grapher/energy-consumption-by-source-and-region?stackMode=absolute', '900px', '600px'))


# **Datos relevantes**
# - El consumo mundial de combustibles fósiles (petróleo, gas y carbón) a aumentado en casi 65% desde el año 1990 hasta el año 2021.
# - El porcentaje de energía proveniente de combustibles fósiles, ha disminuido de casi un 87% en 1990 a 83% en el 2021 (en Chile, este porcentaje cayó desde 82% a 76.5%).
# - Actualmente en Chile, las energías renovables representan un 23.5%, donde un 6.25% proviene de energía solar.

# >Por otro lado, **la disponiblidad de combustilbes fósiles es limitada**. Segun estudios ´[las reservas de petroleo, gas y carbón se agotarán para los años 2052, 2060 y 2090, respectivamente.](https://earthbuddies.net/when-will-we-run-out-of-fossil-fuel/)
# 
# >Esto significa que los precios de los combustibles fósiles seguirán aumentando en las próximas décadas.

# ## Problemas medioambientales asociados al sistema energético actual
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


display(IFrame('https://globalsolaratlas.info/','100%','600px'))


# Chile es el país con mayores niveles de radiación en el mundo. 
# 
# Por ejemplo, en base al atlas solar del [World Bank Group](https://globalsolaratlas.info/map?c=11.523088,8.261719,3), si calculamos la energía generada por el área con mayores niveles de radiación considerando paneles con [potencia máxima de 500 Wp](https://solarity.cz/blog/500-wp-solar-modules-era/)

# In[3]:


A     = 250060.15 # Superficie total (km^2)
Pmax  = 500       # Potencia máxima por panel en condiciones estándard (Wp)
PVOUT = 6.0       # Potencía específica suministrada (kWh/Wp)

# Energía total suministrada (TWh)
Etot  = A*1E3**2*PVOUT*Pmax/1E12
print("Energía eléctrica suministrada: %.1f TWh (Energía consumida en Chile 444 TWh)" % Etot)


# > "*Para abastecer toda la energía que requiere Chile si tuviéramos almacenamiento suficiente necesitamos unos mil kilómetros cuadrados, algo menos que el 1% del desierto y equivalente más o menos a la superficie de la comuna de Melipilla.*"  [Rodrigo Palma, director de SERC, 2022](https://www.revistaei.cl/2019/09/04/con-todo-el-potencial-de-energia-solar-de-chile-se-podria-abastecer-60-veces-el-consumo-del-pais-y-el-20-del-mundo/#)

# ### Descripción de tecnologías para energía solar

# - Fotovoltaica
# <img src="./images/pv_cell.jpg" width="400">

# - Termosolar
# <img src="./images/thermo_solar_power_plant.jpg" width="400">

# - Termoregulación solar para edificaciones
# <img src="./images/smart_window.jpg" width="400">

# - Desalinización solar
# <img src="./images/solar_desalination.png" width="400">

# - Combustibles solares (ejemplos)

# Generación fotoelectroquímica
# 
# <img src="./images/artificial_photosynthesis.png" width="400">

# Generación termoquímica
# 
# <img src="./images/thermochemical_solar_reactor.png" width="400">

# ### Tecnologías en base a energía solar en Chile
# En Chile las principales tecnologías son la fotovoltaica y termosolar, [con una capacidad instalada de 4.6 GW](https://www.pv-magazine-latam.com/2021/04/13/chile-alcanza-46-gw-fotovoltaicos-de-potencia-instalada/). La mayor parte de este simunistro corresponde a plantas solares fotovoltaicas. Respecto al suministro de energía termosolar, se destacan dos proyectos:

# [Planta solar cerro dominador](https://laderasur.com/articulo/recorriendo-cerro-dominador-la-unica-planta-termosolar-que-funciona-en-medio-del-desierto-de-atacama/)
# 
# <img src="./images/cerro_dominador.jpg" width="400">

# [Concentrador solar parabolico en Valparaiso](https://energia.gob.cl/noticias/valparaiso/primer-concentrador-solar-termico-en-valparaiso)
# 
# <img src="./images/concentrador_solar_chile.jpg" width="400">

# ## Descripción general de la asignatura

# En este curso revisaremos los fundamentos y aplicaciones de tecnologías para el manejo y conversión de la energía solar. **La primera parte de este curso estará enfocada hacia los fundamentos de la radiación solar**. Analizaremos el fenómeno electromagnético de la radiación y su interacción con la materia para explicar los mecanismos detrás de la respuesta óptica en diversos escenarios.
# 
# En la segunda parte revisaremos las principales tecnologías de conversión y manejo de energía solar. **Comenzaremos analizando colectores solares aplicados a sistemas de agua caliente en sectores residenciales**. Debido a la simpleza en su diseño, el análisis de estos sistemas servirá como plataforma para aplicar y reforzar los conceptos aprendidos en la primera parte. Luego, revisaremos centrales termosolares, celdas fotovoltaicas,  manejo de la radiación solar en edificaciones, y otras tecnologías aún en desarrollo como desalinización y combustibles solares.

# ### Objetivos generales
# Aprender los fundamentos del manejo de la radiación térmica y solar, así como sobre las principales tecnologías de conversión y manejo de energía solar<br>

# ### Objetivos específicos
# - Entender la radiación como un fenómeno electromagnético
# - Entender la interacción materia-luz y su relación con la respuesta óptica de los materiales
# - Comprender los régimenes de análisis para el transporte radiativo en función de la longitud de escala.
# - Familiarizar al estudiante con las herramientas de modelación de transporte radiativo.
# - Comprender los fundamentos de la transferencia de calor por radiación.
# - Entender las principales características de la radiación solar.
# - Capacitar al estudiante en el diseño de sistemas de agua caliente domiciliarios basados en colectores solares.
# - Familiarizar al estudiante con las principales tecnologías de manejo y conversión de energía solar.
# - Familiarizar al estudiante con las tecnologías de manejo y conversión de energía solar emergentes, y el rol de la nanofotónica en el futuro de estas tecnologías.

# ## Temario

# ### Contenidos
# 
# 1. La radiación como un fenómeno electromagnético
# 2. Interacción materia-luz
# 3. Dispersión (scattering) de la luz y transporte radiativo
# 4. Fundamentos de la transferencia de calor por radiación
# 5. Radiación Solar
# 6. Colectores planos para sistemas de agua caliente termosolar
# 7. Plantas termosolares
# 8. Celdas fotovoltaicas
# 9. Tecnologías de termorregulación solar para edificaciones
# 10. Sistemas de desalinización Solar
# 11. Dispositivos de conversión de combustibles solares

# ## Evaluación de la asignatura
# - Tres (3) pruebas en formato de tareas (80% de nota de presentación)
# - Cuestionarios al comienzo de cada clase (20% de la nota de presentación)
# 
# \begin{equation}
# \mathrm{NP}  = 80\%\mathrm{Promedio Pruebas} + 20\%\mathrm{Promedio Cuestionarios}
# \end{equation}
# 
# >\*El promedio de cuestionarios considera 8 de las mejores notas.
# 
# Aquellos alumnos con $\mathrm{NP} \geq 5.0$ no requieren rendir examen. En caso de rendir el examen, **la calificación de este reemplaza la peor nota de las pruebas parciales (solo si la nota del exámen es superior a la peor nota).** La nota final se calcula mediante el promedio de las 3 mejores notas (incluido examen).
