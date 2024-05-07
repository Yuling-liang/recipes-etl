# recipes-etl
recipes-etl

## What the Script Does
1. Reads a JSON file containing recipes.
2. Extracts recipes that have "Chilies" as one of the ingredients.
3. Adds a new field called "difficulty" to each extracted recipe based on the total time required (prepTime + cookTime).
4. Saves the resulting DataFrame to a CSV file called recipes.csv.

## Requirements
- Python (version 3.x)
- pandas (version 1.x)

## Python Version
The script was developed and tested using Python 3.12.0 and pandas 2.2.2

## Third-Party Modules Installation
You can install the required third-party module using pip
