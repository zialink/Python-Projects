from capture import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]= df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]= df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds= ColumnDataSource(df)
t= figure(x_axis_type='datetime', height=100, width= 500, sizing_mode="scale_width",  title= "Motion Graph")
t.yaxis.minor_tick_line_color=None
t.ygrid[0].ticker.desired_num_ticks=1

hover= HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
t.add_tools(hover)

t.quad(left="Start", right="End", bottom=0, top= 1, color="green", source=cds)

output_file("motion_graph.html")
show(t)
