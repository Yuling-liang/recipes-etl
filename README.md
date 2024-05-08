# recipes-etl
recipes-etl
[https://github.com/Yuling-liang/recipes-etl.git](URL)

## Purpose
Extract the recipes that contain chilis in the ingredients, add a new field called "difficulty" based on the total time required (prepTime + cookTime), and save the resulting DataFrame to a CSV file called recipes.csv.

## What does the code do
1. Read the recipe JSON file from path
2. Extract all the recipes with "Chilies", or "chilies", "chles", "chile", "chilis", "chillis"
3. Define function to_minutes() for changing strings like "PT1H30M" or "PT70M" to numbers in minute, cause "cookTime" and "prepTime" columns contain such format, also consider if it is string of number or number
4. Add two new transformed columns as "cookTime_m" and "prepTime_m" when applying function to_minutes() to "cookTime" and "prepTime"
5. Sum "cookTime_m" and "prepTime_m" to create column "totalTime_m"
6. Define function def_difficulty() to return difficulty categories "Hard" (more than 60 minutes), "Medium" (30 to 60 minutes), "Easy" (less than 30 minutes), "Unknown" (NaN)
7. Create column "difficulty" from applying def_difficulty() to column "totalTime_m"
8. Save the transformed chilies recipes to csv file recipes.csv.

## How to run the code
1. Make sure pandas is installed
2. Paste the path of the recipe JSON file in path = '{your path}'
3. Run all the lines 
5. The result is saved as a CSV file called recipes.csv.

## Requirements
- Python (version 3.x)
- pandas (version 1.x)

## Python version
Developed and tested using Python 3.12.0 and pandas 2.2.2

## Module installation
If pandas is not installed, make sure Python 3.x is installed, then you can install pandas by entering "pip install pandas" in commend prompt
