from datetime import datetime
from pytz import timezone
from starplot import MapPlot, Projection
from starplot.styles import PlotStyle, extensions

style = PlotStyle().extend(
    extensions.GRAYSCALE,
    extensions.MAP,
)
style.legend.visible = False
style.bayer_labels.visible = False

tz = timezone("GMT")
dt = datetime(2024, 3, 20, 3, 7, tzinfo=tz)  # July 13, 2023 at 10pm PT
lat, lon = (52.377956, 4.897070)

N = 1
n = MapPlot(
    projection=Projection.STEREO_NORTH,
    lat=lat,
    lon=lon,
    dt=dt,
    ra_min=0,
    ra_max=24,
    dec_min=-15,
    dec_max=90,
    limiting_magnitude=5,
    style=style,
    resolution=2800,
)
n.plot_horizon()
n.set_circle_boundary()
n.plot_calendar(N)

n.export("11_planisphere_north_52N.png", padding=0.3)

S = -1
s = MapPlot(
    projection=Projection.STEREO_SOUTH,
    lat=lat,
    lon=lon,
    dt=dt,
    ra_min=0,
    ra_max=24,
    dec_min=-90,
    dec_max=15,
    limiting_magnitude=5,
    style=style,
    resolution=2800,
)
s.plot_horizon()
s.set_circle_boundary()
s.plot_calendar(S)

s.export("11_planisphere_south_52N.png", padding=0.3)