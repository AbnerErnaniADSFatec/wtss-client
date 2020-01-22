from wtss import wtss

# w = wtss("http://localhost:5000")
w = wtss("http://brazildatacube.dpi.inpe.br")

cv_list = w.list_coverages()

print(cv_list)

cv_scheme = w.describe_coverage("C64m:MEDIAN")

print(cv_scheme)

ts = w.time_series("C64m:MEDIAN", "red", -12.0, -54.0, start_date="2018-01-01", end_date="2018-12-31")

print(ts["red"])
print(ts["nir"])
print(ts.timeline)