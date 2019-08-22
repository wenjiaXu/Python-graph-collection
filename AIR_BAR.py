# 2.6-2 应用案例
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot
plot_local = py.offline.plot_mpl
# Traces
xlabel = ["Alexnet", "Resnet18", "Resnet50", "PnasNet5", "DFL"]
y1 = [85.43, 89.10, 91.64, 92.16, 92.05]
y2 = [86.57, 89.87, 92.27, 93.04, 92.94]
y3 = [86.96, 90.18, 92.58, 93.23, 93.01]
trace_1 = go.Bar(
            x=xlabel,
            y=y1,
            name="Ordinary Category Prediction",
            marker_color='lightslategrey'
    )

trace_2 = go.Bar(
            x=xlabel,
            y=y2,
            name="Attribute Prediction",
            marker_color='lightsalmon'
)

trace_3 = go.Bar(
            x=xlabel,
            y=y3,
            name="Intergrated Classification",
            marker_color='indianred'
    )

trace = [trace_1, trace_2, trace_3]
# Layout
layout = go.Layout(
            title='Classification Accuracy for Aircraft-17',
            yaxis=dict(range=[80, 96]),
            legend_orientation="h"
    )

# Figure
figure = go.Figure(data=trace, layout=layout)

# Plot
pyplt(figure, image='png', filename='air')
plot_local(figure, image='png', filename='air')