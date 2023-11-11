
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

# Define the initial data
x = list(range(-10, 11))
y = [i**3 for i in x]
source = ColumnDataSource(data=dict(x=x, y=y))

# Create the plot
plot = figure(title="Interactive Graph of x^3", x_axis_label="x", y_axis_label="y")
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# Define the callback function for the sliders
def update_data(attrname, old, new):
    # Get the current slider values
    a = slider_a.value
    b = slider_b.value
    c = slider_c.value
    
    # Generate the new data
    x = list(range(-10, 11))
    y = [a*i**3 + b*i**2 + c*i for i in x]
    new_data = dict(x=x, y=y)
    
    # Update the data source
    source.data = new_data

# Create the sliders
slider_a = Slider(title="a", value=1, start=-10, end=10, step=0.1)
slider_b = Slider(title="b", value=0, start=-10, end=10, step=0.1)
slider_c = Slider(title="c", value=0, start=-10, end=10, step=0.1)

# Attach the callback function to the sliders
for slider in [slider_a, slider_b, slider_c]:
    slider.on_change('value', update_data)

# Create the layout
layout = column(plot, slider_a, slider_b, slider_c)

# Add the layout to the current document
curdoc().add_root(layout)
