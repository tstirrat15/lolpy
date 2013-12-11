import LoLpy
from info import API_KEY

def main():
    print "Let's get started!"
    lolpy = LoLpy.LoLpy(API_KEY)
    print lolpy.get_summoner_by_name('Siren Swag')


if __name__ == "__main__":
    main()