LoLpy
=====

Python library for accessing League of Legends' API

##Getting Started:

1. Import lol.py into your python script.
2. Initialize a new LoLpy object using LoLpy(API_KEY) where API_KEY is your applications key.
3. Use LoLpy's methods to easily get information for your python applicatoin.

##Methods:

###getchampions()
Returns a python dictionary with all the League of Legends champions and their attributes.
```python
lolpy = LoLpy(API_KEY)
champions = lolpy.getchampions()
```

###get_game(summonerid)
Returns a python dictionary with information about the game a summoner is currently in and their recent games
```python
lolpy = LoLpy(API_KEY)
game = lolpy.get_game('Trick2g')
```

##Notes:
* To change region from NA, it can be changed in the contructor with the call LoLpy(API_KEY,region='EUW')
* Some methods cannot be called with certain regions, be sure to check the API if you have issues with regions other than NA