import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(epsg=32631)
facilities = gpd.read_file("data/processed/roads.gpkg", layer="roads").to_crs(epsg=32631)

agodi = wards[wards["ward_name"] == "Agodi"]

agodi_roads = gpd.clip(roads, agodi)
print("Roads in Agodi:", len(agodi_roads))

