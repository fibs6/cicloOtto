import numpy as np 
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import  Slider
from bokeh.layouts import column, row
from bokeh.models.annotations.labels import Label


plot = figure(title="Ciclo otto",x_axis_label='Volumen $$(m^3)$$',y_axis_label='Presión (kPa)')


presion_max = Slider(title="Presion máxima (Pa)", value=3*10**6 , start=3*10**6, end=3.5*10**6, step=10*10**3)
presion_min = Slider(title="Presion mínima (Pa)", value=2.5*10**6, start=2*10**6, end=3.5*10**6, step=10*10**3)
volumen = Slider(title="Volumen $$m^3$$", value=1.0, start=0, end=10, step=0.1)
radio_compresion = Slider(title="Radio de compresión", value=8.5, start=8, end=10, step=0.1)
gamma = 1.4


def actualizar_grafico(attrname, old, new):
    # Limpiar el grafico
    plot.renderers = []

    #Proceso 1-2
    p1 = presion_min.value
    v1 = volumen.value
    radio = radio_compresion.value

    v2 = v1 / radio
    c1=p1*(v1**gamma)
    va = np.linspace(v2,v1,100)
    pa = c1/(va**gamma)
    plot.line(va,(pa/1000),legend_label="Proceso 1-2 (adiabatico)",line_width=2,color="blue")

    #Proceso 2-3
    p3 = presion_max.value
    v3 = v2
    p2 = c1/(v2**gamma)
    pb=np.linspace(p2,p3,100)
    vb=100*[v3]
    plot.line(vb,(pb/1000),legend_label="Proceso 2-3 (isocorico)",line_width=2,color="red")

    #Proceso 3-4
    c2=p3*(v3**gamma)
    v4 =v1
    vc = np.linspace(v3,v4,100)
    pc = c2/(vc**gamma)
    plot.line(vc,(pc/1000),legend_label="Proceso 3-4 (adiabatico)",line_width=2,color="green")

    #Proceso 4-1
    v4 = v1
    p4 = c2/(v4**gamma)
    pd=np.linspace(p1,p4,100)
    vd=100*[v1]
    plot.line(vd,pd/1000,legend_label="Proceso 4-1 (isocorico)",line_width=2,color="brown")



    # Calcular eta
    mostrar_eta = 1 - (1 / radio_compresion.value ** (gamma - 1))


    plot.title.text = "Ciclo Otto - $$\eta =$$  " + str(mostrar_eta)



    



#Inicializar grafico con valores por defecto
presion_max.value = 35*10**6
presion_min.value = 2*10**6
volumen.value = 1.0
radio_compresion.value = 5.0
actualizar_grafico(None, None, None)



for w in [presion_max, presion_min, volumen, radio_compresion]:
    w.on_change('value', actualizar_grafico)

inputs = column(presion_max, presion_min, volumen, radio_compresion)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Ciclo Otto"
