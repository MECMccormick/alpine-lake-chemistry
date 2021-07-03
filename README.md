# What's in my Water?: Assessing water quality in alpine lakes in the Rocky Mountains
Alpine (high-elevation) lakes are vital sources of freshwater in the Rocky Mountains, and changes in their water quality propagate downstream. The communities that rely on these water sources are growing, and producing more emissions from industry and agriculture as they grow, resulting in nitrates, phosphates, and sulfates accumulating in the atmosphere. These compounds end up in alpine lakes via acid precipitaion, and alter water quality. In order to better protect and manage these vital sources of freshwater, we need to understand their baseline chemistry, and evaluate how that chemistry (as a function of ion concentration and acid neutralization capacity) has changed over the past three decades. This repository contains data and code for exploring the link between alpine lake chemistry and bedrock geology, and for analyzing changes in lake chemistry over time.

Using geospatial analyses, I hope to answer the following questions:

* **Does geology affect baseline levels of ions in lakes?**
* **To what extent is alpine lake chemistry changing over time?**

## Data
I am working with data from a long-term survey of lake water quality conducted by the US Forest Service. Chuck Rhoades (https://www.fs.usda.gov/rmrs/people/crhoades) and Tim Fegel (https://www.fs.usda.gov/rmrs/people/tfegel) of the US Forest Service Rocky Mountain Research Station are the principal investigators for this project and the 'owners' of these data, which are not yet published. In the future, the data will be publicly available and published via the USFS following federal guidelines. I have made the version I am working with available in this repo (in the 'data' folder). You will need to download the data in this repository in order to run the workflow. Please contact me if you have any issues accessing it in order to run the python scripts. Additional data used in this workflow were downloaded from the US Census Bureau's TIGER shapefile database (which is free and open for public use: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html). You are welcome to access the data through the online portal, or simply download the subset provided in the 'data' folder. The file types used are: .csv and .shp

## Outputs
This workflow generates several figures, saved by the script as .png files in a folder named 'figures.' A blog-style write up of my work so far is available in the form of both a second notebook and an html file.

## Running this workflow
The main body of this workflow is contained in the 'alpine_lake_chemistry_workflow.ipynb' file. The notebook relies on some python packages that you may not have installed. The 'lakes-environment.yml' file provided in this repo contains all of the packages you will need to run this workflow. The environment is based on CU Boulder Earth Lab's 'earth-analytics-python' environment. Please install and run the environment. As long as you have downloaded the data provided in this repository and run the environment, the notebook should run from start to finish with no issues.

### Installing and running the environment
1. In bash, `cd` to the `alpine-lake-chemistry` directory.
2. Install the `lakes-environment.yml` file.
```
$ cd alpine-lake-chemistry
$ conda env create -f lakes-environment.yml
```
3. Now you can activate the workflow environment and launch Jupyter Notebook...
```
$ conda activate lake-chem-env
$ jupyter notebook
```
4. ...and run the workflow notebook from there!

## Applying this workflow
Currently, this workflow relies on simple .csv files containing lake chemistry and geology data structured as follows:
|site_name|date|sample_type|Ca|NH4|NO3|...|geo_type|
|---------|----|-----------|--|---|---|---|--------|
|A Lake|Tomorrow|NULL|0|0|0|...|levitating|

This workflow could be adapted and applied to data regarding chemistry of water, soil, vegetation, etc. You may also want shapefiles of the boundaries of your study area for the purpose of generating map figures.

#### Citation information
[![DOI](https://zenodo.org/badge/368690878.svg)](https://zenodo.org/badge/latestdoi/368690878)
