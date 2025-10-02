import random
import time

from controller import add_pokemon_to_db, fetch_pokemon_data


def main():
    while True:
        pokemon_id = random.randint(1, 1025)
        pokemon_schema = fetch_pokemon_data(pokeomon_id=pokemon_id)
        if pokemon_schema:
            print(f"Adcionando o {pokemon_schema} a pokedex/banco de dados.")
            add_pokemon_to_db(pokemon_schema=pokemon_schema)
        else:
            print(f"Não foi possíve obter dados do pokemon número: {pokemon_id}")
        time.sleep(10)


if __name__ == "__main__":
    main()
