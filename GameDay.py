import requests

# Define all leagues, their API endpoints, and target teams
leagues = [
    {
        "name": "NFL",
        "url": "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard",
        "target_team": "Giants"
    },
    {
        "name": "NBA",
        "url": "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20251228",
        "target_team": "76ers"
    },
    {
        "name": "NCAA",
        "url": "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard",
        "target_team": "Gonzaga"
    }
]

# Loop through each league
for league in leagues:
    print(f"\n===== {league['name']} =====")
    
    response = requests.get(league['url'])
    data = response.json()
    target_team = league['target_team']
    
    for game in data['events']:
        matchup = game['competitions'][0]
        
        team_0 = matchup['competitors'][0]
        team_1 = matchup['competitors'][1]
        
        name_0 = team_0['team']['displayName']
        name_1 = team_1['team']['displayName']
        
        if target_team in name_0 or target_team in name_1:
            game_status = game['status']['type']['shortDetail']
            
            if target_team in name_0:
                my_score = team_0['score']
                opp_name = name_1
                opp_score = team_1['score']
            else:
                my_score = team_1['score']
                opp_name = name_0
                opp_score = team_0['score']
                
            print(f"Date/Status: {game_status}")
            print(f"{target_team}: {my_score}")
            print(f"Opponent: {opp_name} ({opp_score})")
            print("--------------------------------")