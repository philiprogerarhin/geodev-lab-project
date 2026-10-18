# geodev-lab-project
Month 1
week 1
# Mapping Access to Healthcare Facilities in Greater Accra, Ghana

## Project Overview
This project will use GIS to map healthcare facilities and population distribution in Greater Accra, Ghana.

## Why It Matters
The project will help identify populated areas that are relatively far from healthcare facilities, supporting better healthcare planning.

## Research Question
Which populated areas in Greater Accra are relatively far from mapped healthcare facilities?

## What I Will Build
An interactive web map showing healthcare facilities, population distribution, and potential geographic gaps in access.

## Data Sources
- [Geofabrik](https://download.geofabrik.de/africa/ghana.html) – healthcare facility data
- [WorldPop](https://hub.worldpop.org/) – population data
- [HDX](https://data.humdata.org/) – administrative boundaries

Week 2: Data Collection and Exploration
Downloaded Ghana OpenStreetMap data and extracted healthcare facilities within Greater Accra using QGIS. Downloaded WorldPop 2025 population data and clipped it to the Greater Accra boundary. Explored the datasets in QGIS and documented their feature counts, geometry types, key attributes, and data quality observations in data-note.md.

Week 3: Data Preparation and Quality Checks

Prepared the healthcare facilities and population datasets for Greater Accra using QGIS. Clipped the healthcare facilities and population raster to the Greater Accra boundary and used EPSG:32630 (WGS 84 / UTM zone 30N) as the working coordinate reference system.

Checked the healthcare facilities layer using QGIS's Check Validity tool. All 790 features were valid, with zero invalid features and zero geometry errors. Identified 112 healthcare facility records with missing names. The population raster contains 246,551 valid cells and 878,845 NoData cells, which have been flagged for consideration during analysis.

The prepared healthcare facilities and Greater Accra boundary are saved as GeoPackages. Detailed quality-check results are documented in week3-quality-checks.md.



##Month 2: Preparation of environment. early python.
week 5: i setup python, vs code and the terminal, hello.py runs.
Week 6: set up the project with uv and added pandas. check.py prints the pandas version.
Week 7: analyse.py reads wards.csv, converts each area and classifies each ward.
