# Create a variable/Array to keep the ingredient that you want to search for
# Create a way to search for said ingredient by putting said ingredient into the ingredient search API
# then print out the recommendations
# //advancement//
# create a new variable that stores how the customer feel and in this way the code will recommend a drink
# give certain ingredients a "mood" and if it matches with the 

# Import libraries for http requests 
# You must download the requests module before using this 
import requests


# Get all the cocktails
response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=gin')
print(response.status_code)

# If successful then do something with the result
if response.status_code == 200:
  Cocktails = response.json()
  allDrinks = Cocktails['drinks']
  for drink in allDrinks:
    print(f" this is {drink['strDrink']}, and to make it you need to {drink['strInstructions']}")

# Otherwise show why the request was unsuccessful
else:
  print(f"Oh nooo something went wrong: {response.status_code} - {response.reason}")
