#!/usr/bin/env python
# coding: utf-8

# In[1]:


import importlib.util
if importlib.util.find_spec('empylib') is None:
    get_ipython().system('pip install git+https://github.com/PanxoPanza/empylib.git')


# ## Espectro electromagnético

# Podemos clasificar la radiación electromagnética según su longitud de onda (o frecuencia).
# 
# <img src="./images/em_spectrum.png" width="700px" align= center>

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
# |Infrarrojo lejano (far-IR)| 15 - 1000 $\mu$m | 20 -0.3 THz|82 - 1.24 meV |

# - 1 eV = $1.602\times 10^{−19}$ J es un **electron volt**. Representa la energía cinética de un electron bajo un potencial de 1 volt.

# El espectro SWIR + MWIR + LWIR se conoce también como **infrarrojo medio (mid-IR)**

# La siguiente tabla es útil para la conversión de unidades:
# 
# <img src="./images/conversion_table.png" width="600px" align= center>

# - $h = 4.136\times 10^{−15}$ eV/Hz es la **constante de Planck**.
# - $\hbar = \frac{h}{2\pi} = 6.582\times10^{−16}$ eV/Hz es la **constante reducida de Planck o constante de Dirac**.

# ## Referencias
# **Hetch E., *Óptica*, 5ta Ed, Pearson, 2017**
# - 3.6 Espectro electromagnético
