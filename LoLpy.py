import json
import urllib2

y:
    def __init__(self, api_key, region = 'na'):
        self.api_key = api_key
        self.region = region

    def makelolapicall(self, func):
        return json.loads(urllib2.urlopen('http://prod.api.pvp.net/api/lol/' + urllib2.quote(self.region + func) + '?api_key=' + urllib2.quote(self.api_key)).read())

    def makeproapicall(self, func):
        return json.loads(urllib2.urlopen('http://prod.api.pvp.net/api/' + urllib2.quote(self.region + func) + '?api_key=' + urllib2.quote(self.api_key)).read())
        
    def get_champions(self):
        print self.makelolapicall('/v1.1/champion')

    def get_game_by_id(self, summonerid):
        print self.makelolapicall('/v1.1/game/by-summoner/' + summonerId + '/recent')

    def get_league_by_id(self, summonerid):
        print self.makeproapicall('/v2.1/league/by-summoner/' + summonerId + '/recent')

    def get_stats_summary_by_id(self, summonerid):
        print self.makelolapicall('/v1.1/stats/by-summoner/' + summonerId + '/summary')

    def get_stats_ranked_by_id(self, summonerid):
        print self.makelolapicall('/v1.1/stats/by-summoner/' + summonerId + '/ranked')

    def get_summoner_masteries_by_id(self, summonerid):
        print self.makelolapicall('/v1.1/summoner/' + summonerId + '/masteries')

    def get_summoner_runes_by_id(self, summonerid):
        print self.makelolapicall('/v1.1/summoner/' + summonerId + '/runes')

    def get_summoner_by_id(self, summonerid):
        print self.makelolapicall('/v1.1/summoner/' + summonerId)

    def get_summoner_name_by_id(self, summonerid):
        print self.makelolapicall('/v1.1/summoner/' + summonerId + '/masteries')

    def get_team_by_id(self, summonerid)
        print self.makeproapicall('/v2.1/team/by-summoner' + + '/masteries')

    #############

    def get_summoner_by_name(self, name):
        return self.makelolapicall('/v1.1/summoner/by-name' + name)
    
    def get_game(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makelolapicall('/v1.1/game/by-summoner/' + summonerId + '/recent')

    def get_league(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makeproapicall('/v2.1/league/by-summoner/' + summonerId + '/recent')

    def get_stats_summary(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makelolapicall('/v1.1/stats/by-summoner/' + summonerId + '/summary')

    def get_stats_ranked(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makelolapicall('/v1.1/stats/by-summoner/' + summonerId + '/ranked')

    def get_summoner_masteries(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makelolapicall('/v1.1/summoner/' + summonerId + '/masteries')

    def get_summoner_runes(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makelolapicall('/v1.1/summoner/' + summonerId + '/runes')

    def get_summoner(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makelolapicall('/v1.1/summoner/' + summonerId + '/masteries')

    def get_summoner_name(self, name):
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makelolapicall('/v1.1/summoner/' + summonerId + '/masteries')

    def get_team(self, name)
        name = name.replace(' ','')
        summonerId = get_summoner_by_name(name)['id']
        print self.makeproapicall('/v2.1/team/by-summoner' + + '/masteries')
