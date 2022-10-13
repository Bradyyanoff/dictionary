afc_east_west_wins = {'bills': 4,
                      'jets': 3,
                      'dolphins': 3,
                      'patriots': 2,
                      'chiefs': 3,
                      'chargers': 3,
                      'broncos': 2,
                      'raiders': 1}
largest_so_far = 'raiders'
for team_name in afc_east_west_wins.keys():
    print(f"The {team_name} have {afc_east_west_wins[team_name]} wins so far")

if afc_east_west_wins.keys() == largest_so_far:
    afc_east_west_wins = [team_name]

