'''
Docstring for LAB5.class__contains10
. Implement __contains__. Create a class where you can check "value in object" 
using __contains__.  
'''
class Team:
    def __init__(self, name, players=None):
        self.name = name
        if players is None:
            self.players = set()
        else:
            self.players = set(players)

    def __repr__(self):
        player_lst = sorted(list(self.players))
        return f"Team {self.name}, Players are {player_lst}"
    
    def __contains__(self, item):
        return item in self.players
teamA = Team(
    name='Python warriors',
    players =['Ana', 'Bob', 'Christie', 'Emili']
)
print(teamA)
player1='Christie'
print(f"Is Player1 in Team? {player1 in teamA} ")
player2='Grace'
print(f"Is Player1 in Team? {player2 in teamA} ")