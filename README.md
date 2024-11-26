# Learning Analytics
This repository uses the [Open University Learning Analytics Dataset](https://analyse.kmi.open.ac.uk/open_dataset) for several analytics applications.

## Directories
* /data
Contains the original .csv files from the [Open University Learning Analytics Dataset](https://analyse.kmi.open.ac.uk/open_dataset). These are not uploaded in this repository. Manipulated data is saved in subfolders in data. Download the original csv files and run the .py files to get all intermediate data manipulations.

* /EDA
General exploratory data analysis of the database

* /dashboard
Creation of dashboards based on the datasets. 

## EDA
Exploratory data analysis. Changes to data are saved in EDA subfolder in the data folder.
* eda.ipynb:
Exploratory data analysis of each table and some deeper dives on into some relationships. Limited data manipulation.

* eda.py:
Copy op manipulations performed in eda.ipynb

## dasboard
Changes to data are saved in dashboard subfolder in the data folder. Data manipulations can either be done running the numbered .ipynb files or the numbered .py files chronologically. Some numbers might have a DASH* named file, containing individual dashboard components.
* dashboard_functions.py:
Functions based on discoveries in Jupyter notebooks for easy creation 

* 01student_region_map:
Transformation of geoJSON to create a UK map, and data transformations for using this map. Regions are grouped by default due to overlapping categories in 'region' variable.







