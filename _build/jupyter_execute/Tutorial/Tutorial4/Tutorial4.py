#!/usr/bin/env python
# coding: utf-8

# In[1]:


import importlib.util
if importlib.util.find_spec('pvlib') is None:
    get_ipython().system('pip install pvlib')


# 
# # Tutorial 4 - Modelación módulo PV
# 
# Este es un tutorial para estimar el desempeño de un módulo PV usando `pvlib`.

# In[2]:


import pvlib


# Acá utilizaremos 3 módulos de la librería.
# 
# - `pvlib.irradiance`: para estimación de ángulos de incidencia y niveles de irradiación efectivos sobre el módulo.
# - `pvlib.temperature`: para estimación de la temperatura de las celdas en condiciones de operación.
# - `pvlib.pvsystem`: para análisis de módulos pv y estimación de curvas IV.

# ## Selección de módulo pv (`pvsystem.retrieve_sam`)

# ### La biblioteca de módulos CEC (`'CECmod'`)
# 
# El *California Energy Commission Comisión* (CEC) contrató laboratorios de pruebas autorizados para medir en condiciones de medición estandar (*standard test conditions* o STC) corriente en corto circuito ($I_\mathrm{sc}$), voltaje en circuito abierto ($V_\mathrm{oc}$); voltaje, corriente y potencia en punto de potencia máxima o mpp ($V_\mathrm{mpp}$,  $I_\mathrm{mpp}$ y $P_\mathrm{mpp}$); coeficientes de temperatura de voltaje y corriente, dimensiones del módulo, número de celdas en serie ($N_s$), subcadenas paralelas ($N_p$), área del módulo en $\mathrm{m^2}$ ($A_c$) y más. Las tablas de los parámetros del módulo CEC están disponibles en las [Listas de equipos solares](https://solarequipment.energy.ca.gov/Home/PVModuleList).  Estas mediciones se han ajustado al modelo de diodo único (SDM, por sus siglas en inglés) mediante el modelo *System Advisor Model* (SAM) del *National Renewable Energy Laboratory* (NREL) y se han almacenado en un archivo CSV incluido con SAM.

# En `pvlib` podemos acceder a esta librería mediante la función `retrieve_sam` del módulo `pvlib.pvsystem`. Para acceder a la librería del CEC, indicamos el argumento `name = 'CECMod'`

# In[3]:


module_db = pvlib.pvsystem.retrieve_sam(name = 'CECMod')


# La información de esta librería está desplegada en formato *dataframe*, donde los modelos de paneles están en anexados por columnas.

# In[4]:


module_db.T.head() # Trasponemos la lista con ".T", para visualizar los paneles por filas


# Cada módulo CEC está caracterizado por los siguientes parámetros:
# 
# | parámetro    | tipo de variable | Unidades o descripción                                                                         |
# | :----------- | :--------: | :-------------------------------------------------------------------------------------------- |
# | `Technology` | string    | one of "Mono-c-Si", "Multi-c-Si", "Thin Film", "CdTe", or "CIGS" families of cells            |
# | `Bifacial`   | boolean   | is bifacial?                                                                                  |
# | `STC`        | float     | nameplate in W at STC                                                                         |
# | `PTC`        | float     | nameplate in W at PVUSA test conditions (1-sun, 20&deg; ambient temperature, 1-m/s windspeed) |
# | `A_c`        | float     | module area in m&sup2;                                                                        |
# | `Length`     | float     | module length in m;                                                                           |
# | `Width`      | float     | module width in m;                                                                            |
# | `N_s`        | int       | number of cells in series                                                                     |
# | `I_sc_ref`   | float     | short circuit current in A at reference condition                                             |
# | `V_oc_ref`   | float     | open circuit voltage in V at reference condition                                              |
# | `I_mp_ref`   | float     | max power current in A at reference condition                                                 |
# | `V_mp_ref`   | float     | max power voltage in V at reference condition                                                 |
# | `alpha_sc`   | float     | short circuit current temperature coefficient in A/&Delta;&deg;C                              |
# | `beta_oc`    | float     | open circuit voltage temperature coefficient in V/&Delta;&deg;C                               |
# | `T_NOCT`     | float     | normal operating cell temperature in &deg;C                                                   |
# | `a_ref`      | float     | diode ideality factor                                                                         |
# | `I_L_ref`    | float     | light or photogenerated current at reference condition in A                                   |
# | `I_o_ref`    | float     | diode saturation current at reference condition in A                                          |
# | `R_s`        | float     | series resistance in &Omega;                                                                  |
# | `R_sh_ref`   | float     | shunt resistance at reference condition in &Omega;                                            |
# | `Adjust`     | float     | adjustment to short circuit temperature coefficient in %                                      |
# | `gamma_r`    | float     | power temperature coefficient at reference condition in %/&Delta;&deg;C                       |
# | `BIPV`       | boolean   | is building integrated PV?                                                                    |

# ### Selección de modelo de panel

# Como vemos, en la biblioteca CEC, los módulos se nombran según el esquema 
# 
#     <nombre del fabricante><modelo>
# Los espacios en blanco, los guiones y otros caracteres no alfanuméricos se reemplazan por `_` en pvlib python. Por ejemplo, “Canadian Solar Inc. CS5M-220M” existe en la base de datos como: `Canadiense_Solar_Inc__CS5P_220M`

# Alternativamente, podemos usar el comando `.T.index.str.startswith` para buscar el modelo. Por ejemplo, para buscar e modelo [CS6X-300M de Canadian Solar Inc](./pv_datasheet/MaxPower_CS6X-M.pdf), buscamos todos los modelos cuyo nombre incluye `'Canadian_Solar_Inc__CS6X'`

# In[5]:


module_index = module_db.T.index.str.startswith('Canadian_Solar_Inc__CS6X')
module_db.T[module_index]


# De aquí identificamos que el modelo está bajo el nombre `Canadian_Solar_Inc__CS6X_300M`

# In[6]:


pv_model = module_db.Canadian_Solar_Inc__CS6X_300M


# Los parámetros CEC de este módulo son

# In[7]:


pv_model


# ## Simulación de curva IV

# Para simular la curva IV de un módulo debemos considerar los siguientes pasos:
# - Definir las condiciones de operación (niveles de irradiancia y condiciones climatológicas del sitio)
# - Determinar irradiación sobre el módulo
# - Determinar la temperatura de la celda
# - Determinar los [cinco parámetros del SDM](../../10_SolarFotovoltaica/10_SolarFotovoltaica.ipynb) para los niveles de irradiancia y temperatura de la celda.
# - Caracterizar la curva IV en las condiciones de operación.
# - Graficar curva IV según condiciones de operación.

# ### Definir condiciones de operación

# En este caso consideraremos un panel solar con ángulos de inclinación $\theta = 30°$ y $\phi = 90°$.

# In[8]:


module_zenith  = 30 # ángulo cenital
module_azimuth = 90 # ángulo acimutal


# Respecto a las condiciones climáticas y de irradiación, consideraremos la siguiente serie de datos.

# In[9]:


import pandas as pd

site_conditions = pd.DataFrame(data = {
            'ghi': [  450,   550,   950,  1050],  # Irradiación horizontal global (W/m2)
            'dni': [  170,   130,   950,   960],  # Irradiación normal directa (W/m2)
            'dhi': [  350,   430,   100,   100],  # Irradiación horizonal difusa (W/m2)
'apparent_zenith': [ 44.2,  33.1,  23.3,  17.4],  # ángulo cenital aparente (°)
        'azimuth': [ 97.4, 110.6, 131.3, 167.9],  # ángulo acimutal (°)
       'temp_air': [ 13.0,  13.5,  15.0,  16.5],  # temperatura del aire (°V)
     'wind_speed': [  6.5,   7.2,   7.6,  8.05]}) # Velocidad del viento (m/s)

site_conditions


# En este caso, agrupamos todos los datos en un *dataframe* `site_conditions` para facilitar la manipulación posterior. Sin embargo, esto no es obligatorio.

# ### Irradiación sobre el módulo (`pvlib.irradiance`)
# 
# La irradiación efectiva sobre la superficie del módulo ($G_\mathrm{eff}$), depende del **ángulo de incidencia ($\theta_i$)** y los **niveles de irradiación (GHI, DNI y DHI)**. En general, determinar esto requiere de modelos complejos. Acá, para simplificar, usaremos la relación:
# 
# \begin{equation*}
# G_\mathrm{eff} = G_\mathrm{DNI}\cos\theta_i + G_\mathrm{DHI}
# \end{equation*}
# 
# Para determinar el **ángulo de incidencia (*angle of incidence* o AOI)**, usamos la función `aoi` del módulo `pvlib.irradiance`. Tal como se discutió en la [unidad 7](../../07_Radiación_Solar/07_Radiación_Solar.ipynb), el ángulo de incidencia depende de los ángulos de inclinación del módulo y del sol. En la función `aoi`, estos parámetros son:
# 
# - `surface_tilt`: ángulo cenital del módulo
# - `surface_azimuth`: ángulo acimutal del módulo
# - `solar_zenith`: ángulo cenital solar
# - `solar_azimuth`: ángulo acimutal solar

# In[10]:


sun_zenith  = site_conditions['apparent_zenith'].values
sun_azimuth = site_conditions['azimuth'].values

aoi = pvlib.irradiance.aoi(
    surface_tilt    = module_zenith,
    surface_azimuth = module_azimuth,
    solar_zenith    = sun_zenith,
    solar_azimuth   = sun_azimuth)


# In[11]:


aoi # mostramos el ángulo de incidencia


# Con esto, determinamos la irradiación efectiva sobre el módulo.

# In[12]:


import numpy as np

# get irradiance
dni = site_conditions['dni'].values
ghi = site_conditions['ghi'].values
dhi = site_conditions['dhi'].values

# Determinamos irradiación effectiva sobre el módulo
Geff = dni*np.cos(np.radians(aoi)) + dhi

print('Irradiación efectiva:', Geff)


# ### Estimación de la temperatura de la celda (`pvlib.temperature`)
# 
# Existen distintos modelos para determinar la temperatura de la celda. En este curso usaremos el modelo de Faiman, D. (2008):
# \begin{equation*}
# T_\mathrm{cell} = T_a + \frac{\alpha E(1 -\eta_m )}{U_c + U_v V_\mathrm{wind}}\quad\quad(\mathrm{°C})
# \end{equation*}
# 
# donde $T_a$ es la temperatura del aire (°C), $\alpha$ es el coeficiente de absorción, $E$ es la irradiancia efectiva sobre el módulo ($\mathrm{W/m^2}$), $\eta_m$ es la eficiencia extena del módulo, $U_c$ y $U_c$ son los coeficientes de transferencia de calor  global y por el viento (en $\mathrm{W/m^2~K}$), respectivamente, y $V_\mathrm{wind}$ es la velocidad del viento (m/s).
# 
# Este modelo está implementado en la función `pvsyst_cell` del módulo `pvlib.temperature`. La función requiere de los siguientes parámetros:
# - `poa_cell`: Irradiación efectiva sobre el módulo
# - `temp_air`: Temperatura del aire
# - `wind_speed`: Velocidad del viento (`wind_speed=1.0`, por defecto)
# - `u_c`: Coeficiente global de transferencia de calor (`u_c=29.0`, por defecto)
# - `u_v`: Coeficiente de transferencia de calor asociado al viento (`u_v=0`, por defecto)
# - `module_efficiency`: Eficiencia externa del módulo (`module_efficiency=0.1`, por defecto)
# - `alpha_absorption`: Coeficiente de absorción (`alpha_absorption = 0.9`, por defecto)

# In[13]:


temp_air = site_conditions['temp_air'].values
temp_cell = pvlib.temperature.pvsyst_cell(
    poa_global = Geff, 
    temp_air = temp_air)

print('Temperatura de la celda: ', temp_cell)


# ### Parámetros SDM en operación (`pvlib.pvsystem.calcparams_cec`)

# [Como vimos en la unidad 10](../../10_SolarFotovoltaica/10_SolarFotovoltaica.ipynb), el modelo SDM está caracterizado por 5 parámetros:
# - Corriente fotoinducida, `IL` (análogo a $I_\mathrm{ph}$)
# - Corriente de saturación, `I0`.
# - Resistencia en derivación, `Rs`.
# - Resistencia en serie, `Rsh`.
# - Factor de idealidad del diodo, $n$.
# 
# Si bien estos parámetros están indicados en la biblioteca CEC, ellos están asociados a condiciones de operación estandar  (o STC). Así, debemos determinar el valor efectivo de estos parámetros en las condiciones de operación del módulo

# **En `pvlib` usamos la función `calcparams_cec` del módulo `pvlib.pvsystem` para derterminar `IL`, `I0`, `Rs`, `Rsh` y `nNsVth` en las condiciones de operación.** El último parámetro (`nNsVth`), corresponde al producto entre $n$, el número de celdas ($N_s$) y el voltaje térmico ($V_T$).

# Como parámetros de entrada, `pvsystem.calcparams_cec` requiere: 
# - Niveles de irradiancia (`effective_irradiance`)
# - Temperatura de la celda (`temp_cell`)
# - Parámetros CEC `alpha_sc`, `a_ref`, `I_L_ref`, `I_o_ref`, `R_sh_ref` y `Adjust`, asociados al módulo seleccionado.
# - Bandgap de la celda (`EgRef = 1.121` en todos los casos)
# - Variación del bandgap con la temperatura (`dEgdT = -0.0002677` en todos los casos)

# In[14]:


IL, I0, Rs, Rsh, nNsVth = pvlib.pvsystem.calcparams_cec(
        effective_irradiance = Geff,
        temp_cell = temp_cell,
        alpha_sc = pv_model.alpha_sc,
        a_ref    = pv_model.a_ref,
        I_L_ref  = pv_model.I_L_ref,
        I_o_ref  = pv_model.I_o_ref,
        R_sh_ref = pv_model.R_sh_ref,
        R_s      = pv_model.R_s,
        Adjust   = pv_model.Adjust,
        EgRef    = 1.121,
        dEgdT    = -0.0002677)


# El resultado de cada variable se almacena en un arreglo asociado a las condiciones de irradiación y temperatura.

# In[15]:


# Mostramos resultado en formato dataframe (solo para visualización)
column_values = ['Geff (W/m2)', 'Tcell (°C)', 'IL (A)', 'I0 (A)', 'Rs (Ohm)', 'Rsh (Ohm)', 'nNsVth (V)']

pd.DataFrame(data = np.vstack((Geff, temp_cell, IL, I0, Rs, Rsh, nNsVth)).T,  
            columns = column_values) 


# ### Caracterización curva IV (`pvlib.pvsystem.singlediode`)

# Una vez determinados los parámetros `IL`, `I0`, `Rs`, `Rsh` y `nNsVth` en las condiciones de operación, lo siguiente es resolver el SDM para caracterizar la curva IV del módulo en operación. Esto lo ejecutamos mediante la función `singlediode` del módulo `pvlib.pvystem`.
# 
# Los parámetros de entrada de `pvlib.pvsystem.singlediode` son:
# - `photocurrent`: corriente fotoinducida
# - `saturation_current`: corriente de saturación
# - `resistance_series`: resistencia en serie
# - `resistance_shunt`: Resistencia en derivación
# - `nNsVth`: producto $nN_sV_T$.

# In[16]:


curve_info = pvlib.pvsystem.singlediode(
    photocurrent      = IL,
    saturation_current= I0,
    resistance_series = Rs,
    resistance_shunt  = Rsh,
    nNsVth            = nNsVth)


# El *output* de la función es un *dataframe* con las características principales de la curva IV. Estos son:
# - `i_sc`: corriente de corto circuito (A)
# - `v_oc`: voltaje en circuito abierto (V)
# - `i_mp`: corriente en punto de potencia máxima, o mpp (A)
# - `v_mp`: voltaje en punto de potencia máxima, o mpp (V)
# - `p_mp`: potencia en punto de potencia máxima, o mpp (W)
# - `i_x`: corriente en `v = 0.5*v_oc` (A).
# - `i_xx`: corriente en `v = 0.5*(v_oc + v_mp)` (A).

# In[17]:


curve_info


# Suponiendo que el módulo opera en el punto mpp (utilizando un mpp tracker, por ejemplo), tenemos que entre la hora 0 y 3, el módulo entregará:

# In[18]:


print('Energía total entregada por el módulo: %.3f Wh' % np.sum(curve_info['p_mp']))


# ### Gráfico de curva IV (`pvlib.pvsystem.i_from_v`)

# Para graficar la curva IV podemos usar la función `i_from_v` del módulo `pvlib.pvsystem`. Esta función calcula la corriente para un voltaje `v` dado, en base al SDM. Los parámetros de entrada son:
# - `voltage`: voltaje efectivo.
# - `photocurrent`: corriente fotoinducida
# - `saturation_current`: corriente de saturación
# - `resistance_series`: resistencia en serie
# - `resistance_shunt`: Resistencia en derivación
# - `nNsVth`: producto $nN_sV_T$.

# Primero, generamos un arreglo `numpy` para el voltaje $v$ en el intervalo $V\in[0,V_\mathrm{oc}]$

# In[19]:


v = np.linspace(0., curve_info['v_oc'], 100)


# Luego determinamos la corriente en base al SDM y los parámetros de operación `IL`, `I0`, `Rs`, `Rsh` y `nNsVth`.

# In[20]:


i = pvlib.pvsystem.i_from_v(
    voltage           =v,
    photocurrent      = IL,
    saturation_current= I0,
    resistance_series = Rs,
    resistance_shunt  = Rsh,
    nNsVth            = nNsVth)


# Ahora graficamos las curvas IV para las 4 condicones de operación.

# In[21]:


import matplotlib.pyplot as plt

# plot the calculated curves:
plt.figure()
for idx in site_conditions.index:
    label = ('$G_{eff}=$ %.1f $W/m^2$\n' % Geff[idx] +
            '$T_{cell}=$ %.1f $\\degree C$' % temp_cell[idx])
    plt.plot(v[:,idx], i[:,idx], label=label)
    v_mp = curve_info['v_mp'][idx]
    i_mp = curve_info['i_mp'][idx]
    # mark the MPP
    plt.plot([v_mp], [i_mp], ls='', marker='o', c='k')

plt.xlabel('Voltaje [V]')
plt.ylabel('Corriente [A]')
plt.legend()
plt.title('Curva IV módulo %s' % pv_model.name)
plt.show()

