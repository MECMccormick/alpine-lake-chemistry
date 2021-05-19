# Alpine Lake Chemistry: A long-term study of water quality in the Rocky Mountains
Alpine (high-elevation) lakes are vital sources of freshwater in the Rocky Mountains, and changes in their water quality propagate downstream. The communities that rely on these water sources are growing, and producing more emissions from industry and agriculture as they grow, resulting in nitrates, phosphates, and sulfates accumulating in the atmosphere. These compounds end up in alpine lakes via acid precipitaion, and alter water quality. In order to better protect and manage these vital sources of freshwater, we need to understand their baseline chemistry, and evaluate how that chemistry (as a function of ion concentration and acid neutralization capacity) has changed over the past three decades. This repository contains data and code for exploring the link between alpine lake chemistry and bedrock geology, and for analyzing changes in lake chemistry over time.

Using geospatial analyses, I hope to answer the following questions:

* **Does geology affect baseline levels of ions in lakes?**
* **How closely correlated are ion concentrations to water quality parameters?**
* **To what extent is alpine lake chemistry changing over time?**

## Data and Packages
The lake chemistry data are not yet published, but will be in the future via the USFS following federal guidelines. I have made the version I'm working with available in this repo. Please contact me if you have any issues accessing it in order to run the python scripts.

Currently, the entire workflow is contained in the 'ea-2021-lakechem-proj-MECM.ipynb' file. As long as you have downloaded the data provided in this repository, the notebook should run from start to finish with no issues.

You will need the following packages in order to run this notebook:
* numpy
* pandas
* matplotlib.pyplot
* earthpy
* geopandas
* folium
* contextily
* seaborn

## Applying this workflow
Currently, this workflow relies on simple .csv files containing lake chemistry and geology data. You may also want shapefiles of the boundaries of your study area for the purpose of generating map figures. I intend to update this repository and workflow with geospatial files representing the geology in these areas. These would also likely be shapefiles, probably sourced from the US Geological Survey's National Geologic Map Database (NGMD).
