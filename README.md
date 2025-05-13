# StaInferring Cuba's Hidden Economy: A Bayesian Latent Variable Model

Hi there! This repo contains an analysis of economic indicators and latent economic models for Cuba and the Dominican Republic (DR), using various geospatial and economic data sources.

## Repo Structure

### `/data`
Contains the data files used in the analysis:
- Geospatial data in TIFF format:
  - Nighttime lights (VIIRS)
  - Vegetation index (NDVI)
  - Road density (OSM)
- Economic data:
  - Meta's Relative wealth index (RWI) for the DR

### `/notebooks`
Jupyter notebooks containing the analysis:
- `cuba_eda.ipynb`: Exploratory data analysis for Cuba
- `cuba_latent_econ_model.ipynb`: Latent economic model implementation for Cuba
- `dr_eda.ipynb`: Exploratory data analysis for the DR
- `dr_latent_econ_model.ipynb`: Latent economic model implementation for the DR, as well as cross-validation code
- `/cuba` and `/dominican-republic`: Scripts to generate the VIIRS and NDVI data from Google Earth Engine. Road density data retrieved from Geofabriks and processed on Google Earth Engine.

### `/essay`
Contains my Latex code and corresponding PDF for my final writeup

### `/presentation`
Contains the Latex code and corresponding presentation slides.

### `/images`
Contains all images used in my presentation and final writeup

### `/midterm`
Contains materials from my midterm submission, used to help inform parts of my essay and presentation.

## Data Sources

The analysis utilizes several key data sources:
- VIIRS nighttime lights data
- NDVI (Normalized Difference Vegetation Index)
- OpenStreetMap road density data
- Relative wealth index data

## Requirements

The project uses Python with several important libraries. Please check the corresponding files to see which ones to install!


Thank you for making it this far! Please enjoy my project.

