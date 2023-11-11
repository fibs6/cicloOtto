from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure, curdoc
from bokeh.layouts import column
from numpy import linspace
import numpy as np

# Inicializamos los parámetros del ciclo Otto
V_min, V_max = 0.01, 0.1  # Cambia según tus necesidades
P_min, P_max = 80, 300    # Cambia según tus necesidades

# Creamos los sliders
V_slider = Slider(start=V_min, end=V_max, value=V_min, step=0.01, title="Volumen")
P_slider = Slider(start=P_min, end=P_max, value=P_min, step=10, title="Presión")

# Creamos la figura
source = ColumnDataSource(data=dict(x=[], y=[]))
plot = figure(title="Ciclo otto",x_axis_label='x',y_axis_label='y')
plot.line('x', 'y', source=source, line_width=2)

# Definimos la función para actualizar los datos
def update_data(attrname, old, new):
    V = np.linspace(V_min, V_max, 100)
    P = P_min * (V_min / V)**1.4  # Modelo simple para el ciclo Otto
    source.data = dict(x=V, y=P)

# Actualizamos los datos cuando cambian los sliders
V_slider.on_change('value', update_data)
P_slider.on_change('value', update_data)

# Organizamos la interfaz
layout = column(V_slider, P_slider, plot)
curdoc().add_root(layout)
