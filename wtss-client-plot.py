import matplotlib.pyplot as pyplot
import matplotlib.dates as mdates
from wtss import wtss

# w = wtss("http://localhost:5000")
w = wtss("http://brazildatacube.dpi.inpe.br")

# retrieve the time series for location with longitude = -54, latitude =  -12
ts = w.time_series("C64m:MEDIAN", "red", -12.0, -54.0, start_date = "2018-01-01", end_date = "2018-12-31")

fig, ax = pyplot.subplots()

ax.plot(ts.timeline, ts["red"], 'o-')

fig.autofmt_xdate()
pyplot.show()