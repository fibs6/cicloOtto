import numpy as np 

from bokeh.io import curdoc
from bokeh.plotting import figure ,show
from bokeh.models import  Slider
from bokeh.layouts import column, row

p_min = 2 * 10**5
p_max = 35 * 10**5
v_max = 0.5
radio_compresion = 5
gamma = 1.4

plot = figure(title="Ciclo otto",x_axis_label='x',y_axis_label='y')



presion_max = Slider(title="Presion máxima (kPa)", value=35*10**5 , start=35*10**5, end=50*10**5, step=10*10**4)
presion_min = Slider(title="Presion mínima (kPa)", value=2*10**5, start=2*10**5, end=10*10**5, step=10*10**4)
volumen = Slider(title="Volumen $m^3$", value=1.0, start=-5.0, end=5.0, step=0.1)


def actualizar_grafico(attrname, old, new):
    # Clear the plot
    plot.renderers = []

    #Proceso 1-2
    p1 = presion_min.value
    v1 = volumen.value

    v2 = v1 / radio_compresion
    c1=p1*(v1**gamma)
    va = np.linspace(10,50,100)
    pa = c1/(va**gamma)
    plot.line(va,(pa*1.160071),legend_label="Proceso 1-2 (adiabatico)",line_width=2,color="blue")

    #Proceso 2-3
    p3 = presion_max.value
    v3 = v2
    p2 = c1/(v2**gamma)
    pb=np.linspace(p2,p3,100)
    vb=100*v3
    plot.line(vb,(pb/1000),legend_label="Proceso 2-3 (isocorico)",line_width=2,color="red")

    #Proceso 3-4
    c2=p3*(v3**gamma) #=139337.5097
    v4 =v1
    vc = np.linspace(10,50,100)
    pc = c2/(vc**gamma) #5547.126174
    plot.line(vc,(pc/2.9137),legend_label="Proceso 3-4 (adiabatico)",line_width=2,color="green")

    #Proceso 4-1
    v4 = v1
    p4 = c2/(v4**gamma)
    pd=np.linspace(p1,p4,100)
    vd=100*v1
    plot.line(vd,pd/1000,legend_label="Proceso 4-1 (isocorico)",line_width=2,color="brown")


for w in [presion_max, presion_min, volumen]:
    w.on_change('value', actualizar_grafico)

inputs = column(presion_max, presion_min, volumen)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Ciclo Otto"
