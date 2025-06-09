# South-Asian Interactive Geo-Map

This repository provides a small example of how to build an interactive map of
the Dallas&ndash;Fort Worth (DFW) area highlighting South Asian community regions
and centers.

The map is generated using Python and the [Folium](https://python-visualization.github.io/folium/) library. It loads
basic information about community centers from `data/community_centers.csv` and
creates an HTML file named `dfw_map.html` with clickable markers and simple
polygon overlays for areas with large South Asian populations.

## Requirements
- Python 3.8+
- `folium` Python package

## Usage
1. Install dependencies (ideally in a virtual environment):
   ```bash
   pip install folium
   ```
2. Run the script:
   ```bash
   python generate_map.py
   ```
   This will create `dfw_map.html` in the project directory.
3. Open `dfw_map.html` in a web browser to explore the map.

Feel free to extend `data/community_centers.csv` with additional locations or
adjust the polygons in `generate_map.py` to better fit your data.
