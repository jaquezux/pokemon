# Consuming data from PokeAPI with Python

<img alt="pokemon-banner-jaquezux" src="pokemon-banner.png" width="1000">

In this project I created some Python functions to consume data from PokeAPI.
The documentation about PokeAPI can be read in this link: https://pokeapi.co/docs/v2

#### 📒 1) Import requests library.
```python
import requests
```

#### 📋 2) Define the endpoints you want to consume. In that case, I used "abilities" and "type". For each endpoint, I will create a function to request the data from the API.

##### 2.1) Get ability function:
```python
def get_abilities(poke):
    print (f"\n{pokemon.title()}'s abilities are:")
    for i in poke['abilities']:
        print(i['ability']['name'])
```

##### 2.2) Get type function:
```python
def get_type(poke):
    print (f"\n{pokemon.title()}'s type is:")
    for i in poke['types']:
        print(i['type']['name'])
```

#### ⌨️ 3) Create the main function. This will be responsible for request data from PokeAPI, besides executing the get_abilities and get_types functions.
```python
def main():
    global pokemon
    pokemon = str(input('Insert Pokemon: '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    get_abilities(poke)
    get_type(poke)
    
if __name__ == '__main__':
    main()
```

After that, the program should work like this:

Insert Pokemon: geodude

Geodude's abilities are:
- rock-head
- sturdy
- sand-veil

Geodude's type is:
- rock
- ground

