# Week 2: Data Note

## 1. Healthcare Facilities

- **Source:** [Geofabrik Ghana OpenStreetMap data](https://download.geofabrik.de/africa/ghana.html)
- **Dataset:** Healthcare facilities extracted for Greater Accra.
- **Feature count:** 790
- **Geometry:** Point
- **Key columns:** `fid`, `osm_id`, `code`, `fclass`, `name`
- **Data quality:** 112 records have missing facility names (`NULL`), approximately 14.2% of the records. Other fields may still help identify these facilities.

## 2. Population Raster

- **Source:** [WorldPop Data Hub](https://hub.worldpop.org/)
- **Dataset:** Ghana population 2025, WorldPop R2024B v1
- **Format:** GeoTIFF (`.tif`)
- **Geometry:** Raster grid
- **Dimensions:** 1,454 columns × 774 rows, one band
- **CRS:** EPSG:32630 — WGS 84 / UTM zone 30N
- **Data type:** Float32
- **Pixel size:** Approximately 92.36 metres
- **Data quality:** QGIS reports a minimum value of 0, maximum of approximately 273.88, and valid-data percentage of 21.82%. NoData coverage needs to be checked before interpreting population distribution.

## 3. Greater Accra Boundary

- **Source:** To be confirmed from the original administrative-boundary download.
- **Dataset:** Greater Accra boundary extracted from the Ghana administrative-boundary dataset.
- **Feature count:** 1
- **Geometry:** Polygon (MultiPolygon)
- **Key columns:** To be confirmed from the attribute table.
- **Data quality:** The layer contains one selected regional boundary. Missing attribute values have not yet been checked.
