# reads data from the Pokémon api to choose from 5 cards to battle against random 2

# Concept:
# The script fetches 5 random Pokémon from the PokéAPI.
# The player selects one Pokémon for battle.
# The game randomly selects two enemy Pokémon.
# The battle is based on base stats (Attack, Defense, HP).
# The Pokémon with the highest total base stats wins!

import requests
import random
import pygame
import io

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 860, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Battle")

# Fetch Pokémon Data
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    data = response.json()
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
    image_url = data["sprites"]["front_default"]

    # Download image and convert it to a Pygame Surface
    image_response = requests.get(image_url)
    image_bytes = io.BytesIO(image_response.content)
    image_surface = pygame.image.load(image_bytes).convert_alpha()  # Preserve transparency

    return {
        "name": data["name"].capitalize(),
        "hp": stats["hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "total": stats["hp"] + stats["attack"] + stats["defense"],
        "image": pygame.transform.scale(image_surface, (96, 96))  # Resize for display
    }

# Get 5 random Pokémon for the player
player_pokemon = [get_pokemon_data(random.randint(1, 151)) for _ in range(5)]

# Load background image
background = pygame.image.load("battle_background.jpg")  # Add a Pokémon battle background image

# Game loop
running = True
selected_pokemon = None
font = pygame.font.Font(None, 32)

while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))  # Draw background

    # Draw Pokémon choices
    for i, p in enumerate(player_pokemon):
        screen.blit(p["image"], (50 + i * 150, 400))  # Display Pokémon images
        text = font.render(p["name"], True, (0, 0, 0))
        screen.blit(text, (50 + i * 150, 550))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(5):
                if 50 + i * 150 < x < 150 + i * 150 and 400 < y < 500:
                    selected_pokemon = player_pokemon[i]
                    running = False  # Exit selection screen

    pygame.display.flip()

# If a Pokémon was selected, start battle
if selected_pokemon:
    enemy_pokemon = [get_pokemon_data(random.randint(1, 151)) for _ in range(2)]

    # Determine winner
    all_pokemon = [selected_pokemon] + enemy_pokemon
    winner = max(all_pokemon, key=lambda p: p["total"])
    
    # Display battle results
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        
        # Show player's Pokémon
        screen.blit(selected_pokemon["image"], (150, 250))
        text = font.render(f"You: {selected_pokemon['name']} ({selected_pokemon['total']} Stats)", True, (0, 0, 0))
        screen.blit(text, (150, 200))

        # Show enemy Pokémon
        screen.blit(enemy_pokemon[0]["image"], (500, 200))
        screen.blit(enemy_pokemon[1]["image"], (500, 350))
        text1 = font.render(f"Enemy 1: {enemy_pokemon[0]['name']} ({enemy_pokemon[0]['total']} Stats)", True, (0, 0, 0))
        text2 = font.render(f"Enemy 2: {enemy_pokemon[1]['name']} ({enemy_pokemon[1]['total']} Stats)", True, (0, 0, 0))
        screen.blit(text1, (500, 150))
        screen.blit(text2, (500, 300))

        # Show battle result
        result_text = "You won!" if winner["name"] == selected_pokemon["name"] else f"You lost! {winner['name']} was the strongest."
        text_result = font.render(result_text, True, (255, 0, 0))
        screen.blit(text_result, (300, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

pygame.quit()

