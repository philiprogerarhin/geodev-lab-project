# Week 3: Data Preparation and Quality Checks

## 1. Coordinate Reference System (CRS)

The working CRS is EPSG:32630 — WGS 84 / UTM zone 30N. This projected coordinate system uses metres and is suitable for distance-based analysis in Greater Accra.

## 2. Reprojection and Clipping

The healthcare facilities layer was clipped to the Greater Accra boundary. The population raster was clipped to the Greater Accra boundary and reprojected to EPSG:32630.

The prepared healthcare facilities and Greater Accra boundary are saved as GeoPackages. The population raster is saved as a GeoTIFF.

## 3. Five Quality Checks

**Check 1: Geometry validity**
- Result: 790 valid healthcare facility features, 0 invalid features, and 0 geometry errors.
- Action: No geometry corrections were required by this check.

**Check 2: Feature count**
- Result: 790 healthcare facilities.
- Action: The feature count was recorded.

**Check 3: Missing facility names**
- Result: 112 records have NULL values in the `name` field.
- Action: Flagged for documentation; missing names were not automatically filled.

**Check 4: Population raster coverage**
- Result: 1,125,396 total cells, 246,551 valid cells, and 878,845 NoData cells. The NoData value is -99999.
- Action: Flagged for further consideration before interpreting population patterns.

**Check 5: CRS and spatial preparation**
- Result: The healthcare facilities, Greater Accra boundary, and population raster use EPSG:32630. The prepared vector layers were clipped to the Greater Accra study area.
- Action: The CRS and preparation status were recorded.

## 4. Analysis-Ready Files

- Healthcare facilities: `healthcare_facilities_greater_accra.gpkg`
- Greater Accra boundary: `greater_accra_boundary.gpkg`
- Population raster: `population_greater_accra_utm30n.tif`

The files are stored in the project's `Vital files` folder.

## 5. Outstanding Data-Quality Issue

The population raster contains a substantial number of NoData cells. Their distribution and effect on population-based analysis should be considered before interpreting healthcare-access gaps.
