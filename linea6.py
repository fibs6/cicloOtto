import numpy as np 
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import  Slider
from bokeh.layouts import column, row
from bokeh.models.annotations.labels import Label

plot = figure(title="Ciclo otto",x_axis_label='Volumen $$(m^3)$$',y_axis_label='Presión (kPa)')

presion_max = Slider(title="Presion mínima (kPa)", value=2600 , start=2400, end=2500, step=10)
presion_min = Slider(title="Presion máxima (kPa)", value=2800, start=2800, end=3000, step=10)
volumen = Slider(title="Volumen $$m^3$$", value=1.0, start=0.1, end=10, step=0.1)
relacion_compresion = Slider(title="Radio de compresión", value=8.5, start=1.5, end=10, step=0.5)
gamma = 1.4

def actualizar_grafico(attrname, old, new):
    # Limpiar el grafico
    plot.renderers = []

    #Proceso 1-2
    p1 = (presion_min.value)*10**2
    v1 = volumen.value
    relacion = relacion_compresion.value

    v2 = v1 / relacion
    c1=p1*v1**gamma
    va = np.linspace(v2,v1,100)
    pa = c1/(va**gamma)
    plot.line(va,(pa/1000),legend_label="Combustión (adiabatico)",line_width=2,color="blue")

    #Proceso 2-3
    p3 = (presion_max.value)*10**2
    v3 = v2
    p2 = c1/(v2**gamma)
    pb=np.linspace(p2,p3,100)
    vb=100*[v3]
    plot.line(vb,(pb/1000),legend_label="Compresión (isocorico)",line_width=2,color="red")

    #Proceso 1-2
    c2=p3*(v3**gamma)
    v4 =v1
    vc = np.linspace(v3,v4,100)
    pc = c2/(vc**gamma)
    plot.line(vc,(pc/1000),legend_label="Admisión (adiabatico)",line_width=2,color="green")

    #Proceso 4-1
    v4 = v1
    p4 = c2/(v4**gamma)
    pd=np.linspace(p1,p4,100)
    vd=100*[v1]
    plot.line(vd,pd/1000,legend_label="Escape (isocorico)",line_width=2,color="brown")

    # Calcular eta
    mostrar_eta = 1 - (1 / relacion_compresion.value ** (gamma - 1))
    plot.title.text = "Ciclo Otto - $$\eta =$$ {:.2f}".format(mostrar_eta)

#Inicializar grafico con valores por defecto
presion_max.value = 2000
presion_min.value = 3500
volumen.value = 0.5
relacion_compresion.value = 5.0
actualizar_grafico(None, None, None)

for w in [presion_min, presion_max, volumen, relacion_compresion]:
    w.on_change('value', actualizar_grafico)

inputs = column(presion_min, presion_max, volumen, relacion_compresion)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Ciclo Otto"