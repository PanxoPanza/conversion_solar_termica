#!/usr/bin/env python
# coding: utf-8

# # Tutoriales `empylib`

# En esta sección veremos algunos tutoriales para el uso de la librería `empylib`
# 
# * [**Tutorial 1**](./Tutorial1/Tutorial1.ipynb)
# * [**Tutorial 2**](./Tutorial2/Tutorial2.ipynb)

# ## Instrucciones de instalación
# Antes de ejecutar los tutoriales, instalar los siguiente paquetes:
# 
# - ```empylib```: paquete principal del curso. Esta disponible desde github ejecutando la siguiente sentencia en una celda de este notebook:
# ```python
# !git clone https://github.com/PanxoPanza/empylib.git
# ```
# Esto descargará una carpeta "empylib" con todos los módulos necesarios. **Ejecutar solo una vez para descargar la carpeta** Posteriormente, no es necesario volver a ejecutar esta línea.
# 
# >**Nota.** El código debe ser ejecutado en la misma carpeta donde se descargó el paquete `empylib`
# 
# 
# 
# - ```iadpython```: paquete para simulaciones de transferencia radiativa de energía. Debe ser instalada desde pip, ejecutando el siguiente script en una celda de este notebook
# ```python
# import sys
# !{sys.executable} -m pip install iadpython
# ```
# >**Nota.** Esta instancia debe ser ejecutada solo una vez.
