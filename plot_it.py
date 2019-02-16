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
    ('Description', '@Description'),
    ('Uselessness score', sample_score_perc),
]

source = ColumnDataSource(data=dict(
    x=x_loc,
    Uselessness_score=sample_score,
    Description=['Your uselessness score']
))

hover_tool = HoverTool(tooltips=TOOLTIPS, renderers=[])
tools = [hover_tool, WheelZoomTool(), PanTool(), ResetTool()]

plot = plotting.figure(plot_width=800, plot_height=400, tooltips=TOOLTIPS,
                       tools=tools,
                       title='Uselessness distribution in population')

# distribution
plot.quad(top=hist, bottom=0.00, left=edges[:-1], right=edges[1:],
          color=mapper, alpha=0.5)

point = plot.circle('x', 'Uselessness_score', size=10, source=source,
                    fill_color='red', legend='Your position')

hover_tool.renderers.append(point)

plot.title.text_font = 'Raleway'
plot.xgrid.visible = False
plot.ygrid.visible = False
plot.xaxis.visible = False
plot.toolbar_location = None
plot.yaxis.axis_label = 'Uselessness_score'
plot.legend.location = 'top_left'
plot.legend.click_policy = 'hide'
