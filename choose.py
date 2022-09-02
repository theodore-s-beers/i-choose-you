# Standard imports
import random
import shutil
import tempfile

# Third-party imports
import climage
import requests


def main():
    # Apparently this is how many Pokémon there are with images (inclusive range)
    n = random.randint(1, 898)

    r1 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{n}")

    if r1.status_code != 200:
        print(f"Error: PokéAPI request failed (status code {r1.status_code})")
        return

    j = r1.json()

    img_url = j["sprites"]["other"]["official-artwork"]["front_default"]

    if img_url is None:
        print("Error: No image found for this Pokémon")
        return

    r2 = requests.get(img_url, stream=True)

    if r2.status_code != 200:
        print(f"Error: PokéAPI request failed (status code {r2.status_code})")
        return

    with tempfile.NamedTemporaryFile() as temp:
        shutil.copyfileobj(r2.raw, temp)

        image = climage.convert(
            temp, is_unicode=True, is_truecolor=True, is_256color=False, width=40
        )

        # Print the name, now that the image is ready
        p_name = j["name"].upper()
        print("========================================")
        print(f"    \033[1mI choose you, {p_name}!\033[0m")
        print("========================================")

        print(image)

    print("============== STATS ===================")

    for stat in j["stats"]:
        s_name = stat["stat"]["name"]

        # Replace hyphens with spaces, and capitalize each word
        s_name = " ".join([word.capitalize() for word in s_name.split("-")])

        # HP should be all caps
        if s_name == "Hp":
            s_name = "HP"

        print(f"{s_name}: {stat['base_stat']}")

    # Empty line
    print()

    abilities = []

    for ability in j["abilities"]:
        a_name = ability["ability"]["name"]

        # Replace hyphens with spaces, and capitalize each word
        a_name = " ".join([word.capitalize() for word in a_name.split("-")])

        abilities.append(a_name)

    if abilities:
        print("============= ABILITIES ================")

    for ability in abilities:
        print(f"- {ability}")


if __name__ == "__main__":
    main()
