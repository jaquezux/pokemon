import requests

def pegar_habilidades(poke):
    print (f"\n{pokemon.title()}'s abilities are:")
    for i in poke['abilities']:
        print(i['ability']['name'])

def pegar_tipo(poke):
    print (f"\n{pokemon.title()}'s type is:")
    for i in poke['types']:
        print(i['type']['name'])

def main():
    global pokemon
    pokemon = str(input('Insert Pokemon: '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke = res.json()
    pegar_habilidades(poke)
    pegar_tipo(poke)

if __name__ == '__main__':
    main()

# 
# Insert Pokemon: geodude

# Geodude's abilities are:
# rock-head
# sturdy
# sand-veil

# Geodude's type is:
# rock
# ground
#