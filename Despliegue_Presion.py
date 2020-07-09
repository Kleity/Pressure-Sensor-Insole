# -*- coding: utf-8 -*-
"""
Credatosted on Thu May 28 12:17:54 2020

@author: Kleity
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Inicializar DataFrame
df = pd.read_excel('IFTTT_Maker_Webhooks_Events.xlsx')
columnas = ['Fecha', 'Tipo', 'Valor']
df.iloc[0] = columnas
datos = df.iloc[1:,2]

#Formacion de matriz de presion
matrixpress = np.asarray(datos).reshape((20,7))
matrixpress[10:12,0:1]= 300
matrixpress[16:18,6:7]= 300
matrixpress[19:20,5:7]= 300
matrixpress[(19,0)]= 300
matrixpress[0:10,0:2]= 300
matrixpress[(0,2)] = 300
matrixpress[(0,6)] = 300
matrixpress[18:19,5:7]= 300

#Despliegue de datos
plt.figure()
plt.imshow(matrixpress)
