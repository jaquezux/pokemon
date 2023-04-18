import requests

def get_abilities(poke):
    print (f"\n{pokemon.title()}'s abilities are:")
    for i in poke['abilities']:
        print(i['ability']['name'])

def get_type(poke):
    print (f"\n{pokemon.title()}'s type is:")
    for i in poke['types']:
        print(i['type']['name'])

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