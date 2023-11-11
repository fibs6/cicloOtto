import numpy as np 

from bokeh.plotting import figure ,show

p_min = 2 * 10**5
p_max = 35 * 10**5
v_max = 0.5
radio_compresion = 5
gamma = 1.4

plot = figure(title="Ciclo otto",x_axis_label='x',y_axis_label='y')
#necesito crear un grafico interactivo con bokeh    https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html


#Proceso 1-2
p1 = p_min
v1 = v_max
v2 = v1 / radio_compresion
c1=p1*(v1**gamma)
va = np.linspace(10,50,100)
pa = c1/(va**gamma)
plot.line(va,(pa*1.160071),legend_label="Proceso 1-2 (adiabatico)",line_width=2,color="blue")

#Proceso 2-3
p3 = p_max
v3 = v2
p2 = c1/(v2**gamma)
pb=np.linspace(p2,p3,100)
vb=100*v3
plot.line(vb,(pb/1000),legend_label="Proceso 2-3 (isocorico)",line_width=2,color="red")

#Proceso 3-4
c2=p3*(v3**gamma)
v4 =v1
vc = np.linspace(10,50,100)
pc = c2/(vc**gamma)
plot.line(vc,(pc/2.889),legend_label="Proceso 3-4 (adiabatico)",line_width=2,color="green")

#Proceso 4-1
v4 = v1
p4 = c2/(v4**gamma)
pd=np.linspace(p1,p4,100)
vd=100*v1
plot.line(vd,pd/1000,legend_label="Proceso 4-1 (isocorico)",line_width=2,color="brown")





show(plot)