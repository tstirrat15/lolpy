import LoLpy
from info import API_KEY


def main():
    print "Let's get started!"
    lolpy = LoLpy.LoLpy(API_KEY)
    account = lolpy.get_summoner_by_name('Dyrus')
    # ranked = lolpy.get_stats_ranked('Dyrus')
    print account


if __name__ == "__main__":
    main()
