from wtss import wtss

# w = wtss("http://www.dpi.inpe.br/tws")
w = wtss("http://localhost:5000/wtss/tws")

cv_list = w.list_coverages()

print(cv_list)

cv_scheme = w.describe_coverage("mod13q1_512")

print(cv_scheme)

ts = w.time_series("mod13q1_512", ("red", "nir"), -12.0, -54.0, "", "")

print(ts["red"])
print(ts["nir"])
print(ts.timeline)