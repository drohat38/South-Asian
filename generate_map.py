import csv
import folium

# Center of Dallas-Fort Worth area
DFW_CENTER = [32.9, -97.0]


def add_population_regions(m):
    """Highlight general regions known for sizable South Asian communities."""
    regions = {
        "Irving": [
            [32.80, -97.03],
            [32.80, -96.90],
            [32.95, -96.90],
            [32.95, -97.03],
        ],
        "Frisco": [
            [33.09, -96.91],
            [33.09, -96.78],
            [33.17, -96.78],
            [33.17, -96.91],
        ],
        "Plano": [
            [33.00, -96.77],
            [33.00, -96.64],
            [33.10, -96.64],
            [33.10, -96.77],
        ],
    }
    for name, coords in regions.items():
        folium.Polygon(
            coords,
            color="blue",
            weight=2,
            fill=True,
            fill_color="blue",
            fill_opacity=0.15,
            popup=name,
        ).add_to(m)


def add_community_centers(m, csv_path="data/community_centers.csv"):
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            folium.Marker(
                [float(row["lat"]), float(row["lon"])],
                tooltip=row["name"],
                popup=f"<b>{row['name']}</b><br>{row['description']}<br>{row['address']}",
            ).add_to(m)


def build_map():
    m = folium.Map(location=DFW_CENTER, zoom_start=10, tiles="CartoDB positron")
    add_population_regions(m)
    add_community_centers(m)
    m.save("dfw_map.html")


if __name__ == "__main__":
    build_map()
