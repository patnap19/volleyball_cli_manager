players_on_court = [
    {'first_name': 'Mariusz',
     'last_name': 'Wlazły',
     'position': 'opposite'},
    {'first_name': 'Michał',
     'last_name': 'Winiarski',
     'position': 'reciever'},
    {'first_name': 'Marcin',
     'last_name': 'Możdżonek',
     'position': 'middle blocker'},
    {'first_name': 'Maciej',
     'last_name': 'Dobrowolski',
     'position': 'setter'},
    {'first_name': 'Stephane',
     'last_name': 'Antiga',
     'position': 'reciever'},
    {'first_name': 'Paweł',
     'last_name': 'Zatorski',
     'position': 'libero'}
]


def make_rotation(team):
    player_for_rotation = team.pop(0)
    print(player_for_rotation)
    team.append(player_for_rotation)
    print(team)
    
make_rotation(players_on_court)