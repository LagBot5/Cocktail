# Import libraries for http requests 
# You must download the requests module before using this 
import requests


# Get all the cocktails
response = 200 #requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=gin')
print(response) #.status_code
sad = true

# If successful then do something with the result
if response == 200:
    # Cocktails = response.json
    # allDrinks = Cocktails['drinks']
    if sad == true:
        
        for drink in allDrinks:
        print(f"I am sad so I need to drink it off so give me ", {drink['strAlcoholic']})

# Otherwise show why the request was unsuccessful
else:
  print(f"Oh nooo something went wrong: {response.status_code} - {response.reason}")