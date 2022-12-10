import json
import random

from miscellaneous.typography import * 
from functions.selectors import *
from functions.wishing import *

loop = True

def main():
    global loop
    while loop == True:
        try:
            character = input(f"{EMPHASIZE.BOLD}Character Name: {EMPHASIZE.END}")
            file = open(f"banners/event/{character}.json", "r") 
            character_banner = json.loads(file.read())
            loop = False
        except OSError:
            print(f"{COLOR.RED}ERROR | '{character}' does not exist.{COLOR.END}")
    
    print(character_banner["bannerName"])
    print(f"{character_banner['bannerStartDate']} to {character_banner['bannerEndDate']}")

    loop = True
    character_wish(character_banner)

if __name__ == "__main__":
    main()