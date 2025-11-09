# Africa Geology Data Shapefile

A comprehensive geospatial dataset containing geological information for the African continent in shapefile format.

## Overview

This repository provides geological data for Africa, including detailed geological formations, rock types, and age classifications. The data is provided in shapefile format, making it compatible with various GIS software and geospatial analysis tools.

## Data Source

**Credit: United States Geological Survey (USGS)**

This dataset is sourced from the United States Geological Survey, a scientific agency of the United States government that provides reliable scientific information about the Earth.

## Dataset Contents

The shapefile contains geological data for Africa including:

- **Geological formations** - Various rock units and formations across the continent
- **Long form names** - Detailed, descriptive names for geological features
- **Spatial data** - Geographic boundaries and locations of geological features
- **Attribute information** - Associated metadata for each geological feature

## File Format

The data is provided in **Shapefile** format, which typically includes:

- `.shp` - Shape format (the main file containing geometry)
- `.shx` - Shape index format
- `.dbf` - Attribute format (contains attribute data)
- `.prj` - Projection format (contains coordinate system information)
- Additional supporting files

## Usage

### GIS Software Compatibility

This shapefile can be used with various GIS applications:

- **QGIS** (Free and open-source)
- **ArcGIS** / ArcGIS Pro
- **GRASS GIS**
- **MapInfo**
- **Global Mapper**

### Python Libraries

```python
import geopandas as gpd

# Load the shapefile
gdf = gpd.read_file('path_to_shapefile.shp')

# View the first few rows
print(gdf.head())

# Plot the data
gdf.plot()
```

### R Usage

```r
library(sf)

# Read shapefile
africa_geology <- st_read("path_to_shapefile.shp")

# View structure
str(africa_geology)

# Plot
plot(africa_geology)
```

## Applications

This geological data can be used for:

- **Geological research** - Study of African continental geology
- **Resource exploration** - Mineral and energy resource assessment
- **Environmental studies** - Understanding geological influences on ecosystems
- **Educational purposes** - Teaching geology and GIS
- **Land use planning** - Informed decision-making for development
- **Hazard assessment** - Geological hazard mapping and analysis

## Data Attribution

When using this data in publications, presentations, or projects, please credit:

**United States Geological Survey (USGS)**

Recommended citation format:
```
U.S. Geological Survey, [Year]. Africa Geology Data Shapefile. 
Retrieved from [Repository URL]
```

## License

Please refer to the USGS data use policies and licensing information. USGS data is typically in the public domain, but proper attribution is expected and appreciated.

## Contributing

Contributions, corrections, and improvements to this dataset are welcome. Please submit issues or pull requests as needed.

## Contact & Support

For questions about the data or repository:
- Open an issue in this repository
- Refer to [USGS official resources](https://www.usgs.gov/) for detailed geological information

## Additional Resources

- [USGS Official Website](https://www.usgs.gov/)
- [USGS Geology and Geophysics](https://www.usgs.gov/programs/geology-and-geophysics)
- [African Geology Resources](https://www.usgs.gov/international/africa)

## Disclaimer

This data is provided as-is. While sourced from the reputable USGS, users should verify the data's suitability for their specific applications. The repository maintainer is not responsible for any decisions made based on this data.

---

**Last Updated:** November 2025  
**Maintainer:** Heed725  
**Data Source:** United States Geological Survey (USGS)
