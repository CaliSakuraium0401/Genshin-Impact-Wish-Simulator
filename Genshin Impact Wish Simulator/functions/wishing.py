import random
import math
import random
import sys

from miscellaneous.typography import * 
from functions.selectors import *


# Weapon Wish Banner
    # A 5-star character or weapon – 0.7% chance of dropping
    # A 4-star character or weapon – 6% chance of dropping
    # A 3-star weapon – 93.3% chance of dropping.

loop = True

def character_wish(character_banner):
    # Character Wish Banner

    global loop 

    while loop == True:
        try:
            wishes = int(input(f"{EMPHASIZE.BOLD}Wishes (1-10): {EMPHASIZE.END}"))
            pity = int(input(f"{EMPHASIZE.BOLD}Pity (0-89): {EMPHASIZE.END}"))
            loop = False
        except ValueError:
            print(f"{COLOR.RED}ERROR | invalid input, use the input type shown.{COLOR.END}")

    loop = True

    while loop == True:
        five_star_guranteed = input(f"{EMPHASIZE.BOLD}5 ★ Guranteed (True/False): {EMPHASIZE.END}").title()
        if (five_star_guranteed == "True") or (five_star_guranteed == "False"):
            four_star_guranteed = input(f"{EMPHASIZE.BOLD}4 ★ Guranteed (True/False): {EMPHASIZE.END}").title()
            if (four_star_guranteed == "True") or (four_star_guranteed == "False"):
                loop = False
            else:
                print(f"{COLOR.RED}ERROR | invalid input, use the input type shown.{COLOR.END}")    
        else:
            print(f"{COLOR.RED}ERROR | invalid input, use the input type shown.{COLOR.END}")

    for wish in range(wishes):

        pity += 1
        
        if pity % 10 == 0:
        
            chance = 100.00

            if pity == 90:

                pity = 0

                if five_star_guranteed == True:
                    print(f"{COLOR.YELLOW}5 ★ | {random.choice(character_banner['bannerPromotionalFiveStars'])}{COLOR.END}")
                    five_star_guranteed = False
                else:

                    if random.choice(["Won", "Lost"]) == "Lost":
                        print(f"{COLOR.YELLOW}5 ★ | {random.choice(character_banner['bannerFiveStars'])}{COLOR.END}")
                        five_star_guranteed = True
                    else:
                        print(f"{COLOR.YELLOW}5 ★ | {random.choice(character_banner['bannerPromotionalFiveStars'])}{COLOR.END}")
 
            else:
                
                if four_star_guranteed == True:
                    print(f"{COLOR.PURPLE}4 ★ | {random.choice(character_banner['bannerPromotionalFourStars'])}{COLOR.END}")
                    four_star_guranteed = False
                else:

                    if random.choice(["Character", "Weapon"]) == "Character":
                        print(f"{COLOR.PURPLE}4 ★ | {random.choice(character_banner['bannerFourStarCharacters'])}{COLOR.END}")
                    else:
                        print(f"{COLOR.PURPLE}4 ★ | {random.choice(character_banner['bannerFourStarWeapons'])}{COLOR.END}")

        else:

            chance = round(random.uniform(0, 100), 3)

            # A 5-star character  – 0.6% chance of dropping.
            if (chance >= 0) and (chance <= 0.600): 
                
                pity = 0

                if five_star_guranteed == True:
                    print(f"{COLOR.YELLOW}5 ★ | {random.choice(character_banner['bannerPromotionalFiveStars'])}{COLOR.END}")
                    five_star_guranteed = False
                else:

                    if random.choice(["Won", "Lost"]) == "Lost":
                        print(f"{COLOR.YELLOW}5 ★ | {random.choice(character_banner['bannerFiveStars'])}{COLOR.END}")
                        five_star_guranteed = True
                    else:
                        print(f"{COLOR.YELLOW}5 ★ | {random.choice(character_banner['bannerPromotionalFiveStars'])}{COLOR.END}")
    
            # A 4-star character or weapon – 5.1% chance of dropping
            elif (chance >= 0.600) and (chance <= 5.100): 
                
                if four_star_guranteed == True:
                    print(f"{COLOR.PURPLE}4 ★ | {random.choice(character_banner['bannerPromotionalFourStars'])}{COLOR.END}")
                    four_star_guranteed = False
                else:

                    # 2.5% FOUR STAR CHARACTER
                    if random.choice(["Character", "Weapon"]) == "Character":
                        print(f"{COLOR.PURPLE}4 ★ | {random.choice(character_banner['bannerFourStarCharacters'])}{COLOR.END}")
                    
                    # 2.5% FOUR STAR WEAPON
                    else:
                        print(f"{COLOR.PURPLE}4 ★ | {random.choice(character_banner['bannerFourStarWeapons'])}{COLOR.END}")

                    four_star_guranteed == True
            
            # A 3-star weapon – 94.3% chance of dropping.
            elif (chance >= 5.100) and (chance < 100): 
                print(f"{COLOR.CYAN}3 ★ | {random.choice(character_banner['bannerThreeStarWeapons'])}{COLOR.END}")