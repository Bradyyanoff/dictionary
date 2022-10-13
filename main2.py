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
    if afc_east_west_wins[team_name] > afc_east_west_wins[largest_so_far]:
        largest_so_far = team_name
print(f"The team: {largest_so_far} has the most wins with {afc_east_west_wins[largest_so_far]} wins")
