
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models.widgets import Slider
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc

# Define the range of x values
x = np.linspace(0, 10, 1000)

# Define the initial parameter values for the four functions
a1, b1, c1, d1 = 1, 1, 1, 1
a2, b2, c2, d2 = 1, 1, 1, 1
a3, b3, c3, d3 = 1, 1, 1, 1
a4, b4, c4, d4 = 1, 1, 1, 1

# Define the four functions using the initial parameter values
y1 = a1 * np.sin(b1 * x + c1) + d1
y2 = a2 * np.cos(b2 * x + c2) + d2
y3 = a3 * np.tan(b3 * x + c3) + d3
y4 = a4 * np.exp(b4 * x + c4) + d4

# Create four sliders, one for each parameter
#what are the parameters? a1, b1, c1, d1
#what do they mean? a1 is the amplitude, b1 is the frequency, c1 is the phase, d1 is the vertical shift
slider_a1 = Slider(title="a1", value=a1, start=0, end=10, step=0.1)
slider_b1 = Slider(title="b1", value=b1, start=0, end=10, step=0.1)
slider_c1 = Slider(title="c1", value=c1, start=0, end=10, step=0.1)
slider_d1 = Slider(title="d1", value=d1, start=0, end=10, step=0.1)

slider_a2 = Slider(title="a2", value=a2, start=0, end=10, step=0.1)
slider_b2 = Slider(title="b2", value=b2, start=0, end=10, step=0.1)
slider_c2 = Slider(title="c2", value=c2, start=0, end=10, step=0.1)
slider_d2 = Slider(title="d2", value=d2, start=0, end=10, step=0.1)

slider_a3 = Slider(title="a3", value=a3, start=0, end=10, step=0.1)
slider_b3 = Slider(title="b3", value=b3, start=0, end=10, step=0.1)
slider_c3 = Slider(title="c3", value=c3, start=0, end=10, step=0.1)
slider_d3 = Slider(title="d3", value=d3, start=0, end=10, step=0.1)

slider_a4 = Slider(title="a4", value=a4, start=0, end=10, step=0.1)
slider_b4 = Slider(title="b4", value=b4, start=0, end=10, step=0.1)
slider_c4 = Slider(title="c4", value=c4, start=0, end=10, step=0.1)
slider_d4 = Slider(title="d4", value=d4, start=0, end=10, step=0.1)

# Define a callback function that updates the y values of the four functions whenever a slider value changes
def update_data(attrname, old, new):
    # Get the current slider values
    a1 = slider_a1.value
    b1 = slider_b1.value
    c1 = slider_c1.value
    d1 = slider_d1.value
    
    a2 = slider_a2.value
    b2 = slider_b2.value
    c2 = slider_c2.value
    d2 = slider_d2.value
    
    a3 = slider_a3.value
    b3 = slider_b3.value
    c3 = slider_c3.value
    d3 = slider_d3.value
    
    a4 = slider_a4.value
    b4 = slider_b4.value
    c4 = slider_c4.value
    d4 = slider_d4.value
    
    # Update the y values of the four functions
    source.data['y1'] = a1 * np.sin(b1 * x + c1) + d1
    source.data['y2'] = a2 * np.cos(b2 * x + c2) + d2
    source.data['y3'] = a3 * np.tan(b3 * x + c3) + d3
    source.data['y4'] = a4 * np.exp(b4 * x + c4) + d4

# Create a ColumnDataSource object that contains the x values and the y values of the four functions
source = ColumnDataSource(data=dict(x=x, y1=y1, y2=y2, y3=y3, y4=y4))

# Create a figure object
fig = figure(title="Four Functions")

# Add four line glyphs to the figure, one for each function
fig.line('x', 'y1', source=source, line_width=2, line_color='blue', legend_label='y1')
fig.line('x', 'y2', source=source, line_width=2, line_color='red', legend_label='y2')
fig.line('x', 'y3', source=source, line_width=2, line_color='green', legend_label='y3')
fig.line('x', 'y4', source=source, line_width=2, line_color='orange', legend_label='y4')

# Add the four sliders to the figure
sliders1 = row(slider_a1, slider_b1, slider_c1, slider_d1)
sliders2 = row(slider_a2, slider_b2, slider_c2, slider_d2)
sliders3 = row(slider_a3, slider_b3, slider_c3, slider_d3)
sliders4 = row(slider_a4, slider_b4, slider_c4, slider_d4)

# Define the layout of the figure and the sliders
layout = column(fig, sliders1, sliders2, sliders3, sliders4)

# Add the callback function to the sliders
slider_a1.on_change('value', update_data)
slider_b1.on_change('value', update_data)
slider_c1.on_change('value', update_data)
slider_d1.on_change('value', update_data)

slider_a2.on_change('value', update_data)
slider_b2.on_change('value', update_data)
slider_c2.on_change('value', update_data)
slider_d2.on_change('value', update_data)

slider_a3.on_change('value', update_data)
slider_b3.on_change('value', update_data)
slider_c3.on_change('value', update_data)
slider_d3.on_change('value', update_data)

slider_a4.on_change('value', update_data)
slider_b4.on_change('value', update_data)
slider_c4.on_change('value', update_data)
slider_d4.on_change('value', update_data)

# Show the figure
show(layout)
# Add the layout to the current document
curdoc().add_root(layout)
