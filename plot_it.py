from bokeh import plotting
from bokeh.models import HoverTool, PanTool, ResetTool, WheelZoomTool
from bokeh.plotting import ColumnDataSource
from calculations import hist, edges, x_loc, sample_score, sample_score_perc
from bokeh.transform import linear_cmap

low = 1.9
high = 4.1

mapper = linear_cmap(field_name='left',
                     low=low, high=high, palette=['#222222'],
                     low_color='#2453bf', high_color='#154f1e')


TOOLTIPS = [
    # ("(x,y)", "($x, $y)"),
    ('Popis', '@Popis'),
    ('Tvé skóre zbytečnosti', sample_score_perc),
]

source = ColumnDataSource(data=dict(
    x=x_loc,
    Skore_zbytecnosti=sample_score,
    Popis=['Tvé skóre_zbytečnosti']
))

hover_tool = HoverTool(tooltips=TOOLTIPS, renderers=[])
tools = [hover_tool, WheelZoomTool(), PanTool(), ResetTool()]

plot = plotting.figure(plot_width=800, plot_height=400, tooltips=TOOLTIPS,
                       tools=tools,
                       title='Distribuce zbytečnosti v populaci')

# distribution
plot.quad(top=hist, bottom=0.00, left=edges[:-1], right=edges[1:],
          color=mapper, alpha=0.5)

point = plot.circle('x', 'Skore_zbytecnosti', size=10, source=source,
                    fill_color='red', legend='Tvá pozice')

hover_tool.renderers.append(point)

plot.title.text_font = 'Raleway'
plot.xgrid.visible = False
plot.ygrid.visible = False
plot.xaxis.visible = False
plot.toolbar_location = None
plot.yaxis.axis_label = 'Skóre_zbytečnosti'
plot.legend.location = 'top_left'
plot.legend.click_policy = 'hide'
