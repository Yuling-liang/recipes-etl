import pandas as pd

# read the file
path = r'C:\Users\16234307708308258757\Downloads\recipes.json'
df = pd.read_json(path, lines=True)
df.head(10)

# extract recipes that have “Chilies” as one of the ingredients.

chilies_recipes = df[df.loc[:, 'ingredients'].str.lower().str.contains('chilies|chiles|chile|chilis|chillis', na=False)]
print(chilies_recipes)

# extra field to each of the extracted recipes with the name difficulty.
# The difficulty field  would have a value of "Hard" if the sum of prepTime and cookTime is greater than 1 hour,
# "Medium" if the total is between 30 minutes and 1 hour,
# "Easy" if the total is less than 30  minutes, and
# "Unknown" otherwise.

# check how do the prepTime and cookTime columns look, so cookTime could be in hour or minutes format (PT1H30M, PT60M), while prepTime is number

chilies_recipes.loc[:, 'cookTime']
chilies_recipes.loc[:, 'prepTime']

# write a function for transforming all the cells in the columns to minutes

def to_minutes(time):
    if 'H' in time and 'M' in time:   # for the cells that have ''H' and 'M', split them before calculating
        hr, m = time.split('H')
        hr = int(hr[2:])
        m = int(m[:-1])
        return hr * 60 + m
    elif 'H' in time:
        hr = int(time[2:-1])
        return hr * 60
    elif 'M' in time:
        m = int(time[2:-1])
        return m
    elif time.isdigit():  # if the time is a string of number, return integer
        return int(time)
    elif isinstance(time, float):  # If the time is a float, convert it to integer
        return int(time)
    else:
        return None

# apply the function to turn cookTime and prepTime into integer in minutes to new columns

chilies_recipes.loc[:, 'cookTime_m'] = chilies_recipes.loc[:, 'cookTime'].apply(to_minutes)
chilies_recipes.loc[:, 'prepTime_m'] = chilies_recipes.loc[:, 'prepTime'].apply(to_minutes)

# sum the new cookTime_m and prepTime_m columns to create new field totalTime

chilies_recipes.loc[:, 'totalTime_m'] = chilies_recipes.loc[:, 'prepTime_m'] + chilies_recipes.loc[:, 'cookTime_m']

# then, define a function to determine the difficulty of the recipes with chilies
def def_difficulty(time):
    if time > 60:
        return "Hard"
    elif 30 <= time <= 60:
        return "Medium"
    elif time < 30:
        return "Easy"
    else:
        return "Unknown"

# add the difficulty field to the table

chilies_recipes.loc[:, 'difficulty'] = chilies_recipes['totalTime_m'].apply(def_difficulty)

# save the result as a csv file

chilies_recipes.to_csv('recipes.csv', index=False)
