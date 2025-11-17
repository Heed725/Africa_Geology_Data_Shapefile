# 🌍 Africa Geology Data Shapefile

[![Download ZIP](https://img.shields.io/badge/Download-ZIP-brightgreen?style=for-the-badge&logo=download&logoColor=white)](../../archive/refs/heads/main.zip)
[![USGS](https://img.shields.io/badge/Source-USGS-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAdgAAAHYBTnsmCAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAERSURBVCiRY2AYBcMYMDIwMPxn+P+fAQtg+v///38GZBwzM7P/DAwM/7EpZvr//z8jVBELCwvjfwYGBkZGRkYmqCJ0hUxQJ6BrYoJqYGBgYPr//z8zTCE2Nzb9////n5GBgYHx////zDAJRkZGJpgpDAwMjMzMzP8ZGRn/MzIy/v/PwPCfkZGRiYGBgZEBajoTVCPjfwYGBkYGBgYmBgYGJgYGhv+MjIxMDAwMjAwMDP8ZGBiYGBgYGBkYGP4zMjL+Z2Bg+M/IyPCfgYHhPyMjw38GBob/DAwM/xkZGf8zMDD8Z2Bg+M/AwPCfkZHhPwMDw38GBob/jIyM/xkYGP4zMjL8Z2Bg+P+fgYGBYRQMYwAAuQM6+nGH4NQAAAAASUVORK5CYII=)](https://www.usgs.gov/)
[![License](https://img.shields.io/badge/License-Public%20Domain-lightgrey?style=for-the-badge)](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits)

[![QGIS](https://img.shields.io/badge/QGIS-Compatible-green?style=flat-square&logo=qgis&logoColor=white)](https://qgis.org/)
[![ArcGIS](https://img.shields.io/badge/ArcGIS-Compatible-blue?style=flat-square&logo=arcgis&logoColor=white)](https://www.esri.com/en-us/arcgis/about-arcgis/overview)
[![Python](https://img.shields.io/badge/Python-GeoPandas-yellow?style=flat-square&logo=python&logoColor=white)](https://geopandas.org/)
[![R](https://img.shields.io/badge/R-sf%20Package-276DC3?style=flat-square&logo=r&logoColor=white)](https://r-spatial.github.io/sf/)
[![Format](https://img.shields.io/badge/Format-Shapefile-orange?style=flat-square&logo=geojson&logoColor=white)]()

> A comprehensive geospatial dataset containing detailed geological information for the African continent. Perfect for researchers, students, and GIS professionals.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Quick Start](#-quick-start)
- [Dataset Contents](#-dataset-contents)
- [Download](#-download)
- [Usage Examples](#-usage-examples)
- [Applications](#-applications)
- [Data Attribution](#-data-attribution)
- [Contributing](#-contributing)
- [Support](#-support)

---

## 🔍 Overview

This repository provides high-quality geological data for Africa, including detailed geological formations, rock types, and age classifications. The dataset is maintained in shapefile format for maximum compatibility with GIS software and geospatial analysis tools.

**Data Source:** United States Geological Survey (USGS)  
**Coverage:** African Continent  
**Format:** Shapefile (.shp, .shx, .dbf, .prj)  
**Coordinate System:** Included in .prj file

---

## 🚀 Quick Start

### Prerequisites

- GIS Software (QGIS, ArcGIS, etc.) OR
- Python with GeoPandas OR
- R with sf package

### Installation

**Option 1: Direct Download**

Click the button below to download the complete dataset:

[![Download Now](https://img.shields.io/badge/⬇️_Download_Complete_Dataset-ZIP-success?style=for-the-badge)](../../archive/refs/heads/main.zip)

**Option 2: Git Clone**

```bash
git clone https://github.com/yourusername/africa-geology-shapefile.git
cd africa-geology-shapefile
```

---

## 📦 Dataset Contents

The shapefile package includes comprehensive geological data:

| Feature | Description |
|---------|-------------|
| 🗺️ **Geological Formations** | Various rock units and formations across Africa |
| 📝 **Long Form Names** | Detailed, descriptive names for geological features |
| 📍 **Spatial Data** | Precise geographic boundaries and locations |
| 🏷️ **Attribute Information** | Rich metadata for each geological feature |
| 🔢 **Age Classifications** | Geological time period information |
| 🪨 **Rock Types** | Comprehensive lithological classifications |

### File Structure

```
africa-geology/
├── africa_geology.shp      # Main geometry file
├── africa_geology.shx      # Shape index file
├── africa_geology.dbf      # Attribute data
├── africa_geology.prj      # Coordinate system
├── africa_geology.cpg      # Character encoding
└── README.md              # This file
```

---

## ⬇️ Download

### Download Options

| Method | Link | Size |
|--------|------|------|
| **ZIP Archive** | [![Download ZIP](https://img.shields.io/badge/Download-ZIP-brightgreen?style=flat-square&logo=download)](../../archive/refs/heads/main.zip) | ~XX MB |
| **Git Clone** | `git clone [repository-url]` | ~XX MB |
| **Individual Files** | Browse repository files | Varies |

---

## 💻 Usage Examples

### ![QGIS](https://img.shields.io/badge/-QGIS-589632?style=flat&logo=qgis&logoColor=white)

1. Open QGIS
2. Go to **Layer → Add Layer → Add Vector Layer**
3. Browse to the `.shp` file
4. Click **Add**

### ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) GeoPandas

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the shapefile
geology = gpd.read_file('africa_geology.shp')

# Display basic information
print(f"Total features: {len(geology)}")
print(f"Coordinate System: {geology.crs}")
print("\nFirst 5 rows:")
print(geology.head())

# Create a simple plot
fig, ax = plt.subplots(figsize=(15, 15))
geology.plot(ax=ax, column='ROCK_TYPE', legend=True, cmap='tab20')
plt.title('Africa Geological Formations', fontsize=16)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()

# Export to different format
geology.to_file('africa_geology.geojson', driver='GeoJSON')
```

### ![R](https://img.shields.io/badge/-R-276DC3?style=flat&logo=r&logoColor=white) sf Package

```r
library(sf)
library(ggplot2)

# Read shapefile
africa_geology <- st_read("africa_geology.shp")

# View structure and summary
str(africa_geology)
summary(africa_geology)

# Create visualization
ggplot(africa_geology) +
  geom_sf(aes(fill = ROCK_TYPE), color = NA) +
  theme_minimal() +
  labs(title = "Africa Geological Formations",
       fill = "Rock Type") +
  theme(legend.position = "bottom")

# Check coordinate reference system
st_crs(africa_geology)

# Calculate area of geological units
africa_geology$area_km2 <- st_area(africa_geology) / 1e6
```

### ![ArcGIS](https://img.shields.io/badge/-ArcGIS-2C7AC3?style=flat&logo=arcgis&logoColor=white) ArcGIS Pro

1. Open ArcGIS Pro
2. In the **Catalog** pane, browse to the shapefile location
3. Drag and drop the `.shp` file onto your map
4. Right-click the layer → **Properties** → **Symbology** to customize

---

## 🎯 Applications

This geological dataset enables a wide range of applications:

| Domain | Use Cases |
|--------|-----------|
| 🔬 **Research** | Continental geology studies, tectonic analysis, geological evolution |
| ⛏️ **Resource Exploration** | Mineral prospecting, hydrocarbon assessment, geothermal mapping |
| 🌱 **Environmental** | Soil-geology relationships, groundwater studies, ecosystem analysis |
| 🎓 **Education** | Teaching geology, GIS training, academic research |
| 🏗️ **Planning** | Infrastructure development, land use planning, construction suitability |
| ⚠️ **Hazard Assessment** | Seismic risk, landslide susceptibility, geological hazard mapping |
| 💧 **Hydrology** | Aquifer identification, water resource management |
| 🌾 **Agriculture** | Soil parent material analysis, agricultural suitability |

---

## 📚 Data Attribution

### Citation

When using this dataset in publications, presentations, or projects, please provide proper attribution:

**Recommended Citation:**

```
U.S. Geological Survey (2025). Africa Geology Data Shapefile. 
Retrieved from https://github.com/yourusername/africa-geology-shapefile
```

**BibTeX Format:**

```bibtex
@dataset{usgs_africa_geology_2025,
  author = {{U.S. Geological Survey}},
  title = {Africa Geology Data Shapefile},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/yourusername/africa-geology-shapefile}
}
```

---

## 📄 License

This dataset is sourced from the **United States Geological Survey (USGS)**, which provides data in the **public domain**. 

- ✅ Free to use for any purpose
- ✅ No permission required
- ✅ Commercial use allowed
- ⚠️ Attribution appreciated (see above)

For detailed information, visit: [USGS Copyright and Credits](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Issues** - Found an error? [Open an issue](../../issues)
2. **Suggest Improvements** - Have ideas? Share them!
3. **Submit Updates** - Fork, modify, and create a pull request
4. **Share Use Cases** - Show us how you're using the data

### Contribution Guidelines

- Ensure data accuracy and provide sources
- Follow the existing file structure
- Update documentation as needed
- Test changes before submitting

---

## 📞 Support

### Getting Help

- 📧 Contact: [Hemedlungo@gmail.com]

### External Resources

- 🌐 [USGS Official Website](https://www.usgs.gov/)
- 🗺️ [USGS Geology Programs](https://www.usgs.gov/programs/geology-and-geophysics)
- 🌍 [USGS Africa Resources](https://www.usgs.gov/international/africa)
- 📚 [QGIS Documentation](https://docs.qgis.org/)
- 🐍 [GeoPandas Documentation](https://geopandas.org/)

---

## ⚠️ Disclaimer

This dataset is provided **as-is** without warranty of any kind. While sourced from the reputable USGS, users should:

- Verify data suitability for specific applications
- Conduct independent validation for critical projects
- Check for updates and newer versions periodically

The repository maintainer is not responsible for decisions made based on this data.

---

## 🔖 Tags

`geology` `africa` `shapefile` `gis` `geospatial` `usgs` `geological-data` `qgis` `arcgis` `geopandas` `open-data` `earth-science` `cartography` `spatial-analysis`

---

<div align="center">

**Made with 🌍 by Heed725**

**Last Updated:** November 2025

[![Download](https://img.shields.io/badge/⬇️_Download_Now-Click_Here-success?style=for-the-badge)](../../archive/refs/heads/main.zip)

**⭐ Star this repository if you find it useful!**

</div>
