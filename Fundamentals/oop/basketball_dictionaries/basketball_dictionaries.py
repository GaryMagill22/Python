joel = {'name': 'Joel Embiid', 
        'age':  32,
        'position': 'Power Forward', 
        'team': 'Philidelphia 76ers'}


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# List of player dictionaries

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# Update the constructor to accept a dictionary with a single players info instead of individual arguments for the attributes.


class Player:

    def __init__(self, player_info):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']


    @classmethod
    def get_team(cls, team_list):
        player_objects = []
        for d in team_list:
            player_objects.append(cls(d))
        return player_objects
    
#PLAYERS INSTANCES

player_kevin = Player(kevin)
print(kevin)

player_joel = Player(joel)
print(joel)

player_jason = Player(jason)
print(jason)

player_kyrie = Player(kyrie)
print(kyrie)
result = Player.get_team(players)
print(result[0].name)
[{Player},{Player}]
# ... (class definition and large list of players here)
# for loop  to populate the new_team variable with Player objects.
# new_team = []
# for player_info in players:
#     player = Player(player_info)
#     new_team.append(player)
    
# print(new_team)



# all_players = Player.get_team(new_team)
# for p in all_players:
#     print(p.name)