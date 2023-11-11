import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

import plotly.graph_objects as go

# Define the sine and cosine functions
def sine_function(x, freq):
    return np.sin(np.deg2rad(freq) * x)

def cosine_function(x, freq):
    return np.cos(np.deg2rad(freq) * x)

# Create figure
fig = go.Figure()

# Add traces, one for each slider step
for step in np.arange(0, 360, 10):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="Sine, 𝜈 = " + str(step) + "°",
            x=np.arange(0, 10, 0.01),
            y=sine_function(np.arange(0, 10, 0.01), step)))

    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#FFA500", width=6),
            name="Cosine, 𝜈 = " + str(step) + "°",
            x=np.arange(0, 10, 0.01),
            y=cosine_function(np.arange(0, 10, 0.01), step)))

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()