from pathlib import Path
import json
import plotly.express as px

path = Path("mapping_datasets/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = "Earthquakes on earth"
fig = px.scatter_geo(lat=lats, lon=lons, title=title)
fig.show()
