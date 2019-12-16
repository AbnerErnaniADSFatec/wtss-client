import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates
from wtss import wtss

w = wtss("http://www.dpi.inpe.br/tws")

# retrieve the time series for location with longitude = -54, latitude =  -12
ts = w.time_series("mod13q1_512", "red", -12.0, -54.0, start_date="2001-01-01", end_date="2001-12-31")

fig, ax = pyplot.subplots()

ax.plot(ts.timeline, ts["red"], 'o-')

fig.autofmt_xdate()
pyplot.show()