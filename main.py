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

players_bench = [
    {'first_name': 'Daniel',
     'last_name': 'Pliński',
     'position': 'middle blocker'}
]


def make_rotation(team):
    player_for_rotation = team.pop(0)
    print(player_for_rotation)
    team.append(player_for_rotation)
    print(team)
    
# make_rotation(players_on_court)

def libero_on_bench(playing_team, bench_team):
        for player in bench_team:
            if player['position'] == 'middle blocker':
                libero = playing_team.pop(3)
                playing_team.insert(3, player)
                bench_team.append(libero)
                bench_team.remove(player)
                break
            
def libero_on_court(playing_team, bench_team):
    for player in bench_team:
        if player['position'] == 'libero':
            middle_blocker = playing_team.pop(0)
            playing_team.insert(0, player)
            bench_team.append(middle_blocker)
            bench_team.remove(player)

is_team_serving = False

def point_score(playing_team, bench_team, is_serving):
    
    if not is_serving:
        make_rotation(playing_team)
        if playing_team[3]['position'] == 'libero':
            libero_on_bench(playing_team, bench_team)
    else:
        if playing_team[0]['position'] == 'middle blocker':
            libero_on_court(playing_team, bench_team)
        print("Nie ma rotacji ponieważ zagrywasz!")
        
point_score(players_on_court, players_bench, is_team_serving)
point_score(players_on_court, players_bench, is_team_serving)