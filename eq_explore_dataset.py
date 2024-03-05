from pathlib import Path
import json

path = Path("mapping_datasets/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Dump data in more readable format
path = Path("mapping_datasets/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
