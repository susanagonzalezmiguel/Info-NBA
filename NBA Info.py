# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:36:36 2023

@author: USUARIO
"""

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import streamlit as st

st.write(f"""Estadísticas sobre los resultados de Tiger Woods""")

#PANDAS AS .HTML
tabla=pd.read_html('https://www.foxsports.com/golf/tiger-woods-player-stats?category=shots&groupId=1')
print(tabla)

#PANDAS AS .CSV
"""df = pd.read_clipboard()
df.to_excel("ShotsStats_TigerWoods.xlsx")
df.to_csv("ShotsStats_TigerWoods.csv")"""

datos = pd.read_csv("ShotsStats_TigerWoods.csv")
datos.describe()
datos.head()

datos[["EV", "AVG", "DR", "AVGDR", "ACC", "PUTT/H", "BIRD/R", "H/EAG"]].plot(kind="bar", subplots=True, title="Estadísticas para Tiger Woods")
plt.savefig("Grafica1.png")
datos[["EV", "AVG", "DR", "AVGDR", "ACC", "PUTT/H", "BIRD/R", "H/EAG"]].plot(kind="bar", title="Estadísticas para Tiger Woods")
plt.savefig("Grafica2.png")
plt.show()

st.dataframe(datos.iloc[:,[1,2,3,4,5,6,7,8,9]])

from PIL import Image
image1 = Image.open("Grafica1.png")
image2 = Image.open("Grafica2.png")
st.image(image1, caption="Fuente: https://www.foxsports.com/golf/tiger-woods-player-stats?category=shots&groupId=1")
st.image(image2, caption="Fuente: https://www.foxsports.com/golf/tiger-woods-player-stats?category=shots&groupId=1")

st.write(f"""Estadísticas por temporada""")

option = st.selectbox('Selecciona una temporada para ver los resultados', ('2017/18', '2018/19', '2019/20', '2020/21'))
if option == "2017/18":
    #seleccion = tabla["EV"]
    i = 1
    #st.dataframe(datos.iloc[0:i])
elif option == "2018/19":
    #seleccion = tabla["EV"]
    i = 2
elif option == "2019/20":
    #seleccion = tabla["EV"]
    i = 3
elif option == "2020/21":
    #seleccion = tabla["EV"]
    i = 4

seleccion = datos.iloc[i-1:i, [1,2,3,4,5,6,7,8,9]]
st.dataframe(seleccion)

fila = datos[datos['SEASON '] == '2017/18']

#seleccion_ = seleccion.to_numpy()
#st.bar_chart(seleccion_)
st.pyplot(fila)

#st.write(f"""Los mejores resultados respecto a cada una de las categorías han sido:""")
#datos.min("EV")
#datos.min("AVG")
#datos.min("DR")
#datos.min("EV")
#datos.min("EV")
#datos.min("EV")

#st.bar_chart(datos)
#st.pyplot(datos)