import requests

respNFL = requests.get("https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard")
respNBA = requests.get("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20251228")

dataNFL = respNFL.json()
dataNBA = respNBA.json()

target_team_NFL = "Giants" 
target_team_NBA = "76ers" 

#Loop through games for NFL
for game in dataNFL['events']:
    matchup = game['competitions'][0]
    
    #matchup is the 2 teams playing against each other
    team_0 = matchup['competitors'][0]
    team_1 = matchup['competitors'][1]
    
    # Extract names to make checking easier
    name_0 = team_0['team']['displayName']
    name_1 = team_1['team']['displayName']
    
    if target_team_NFL in name_0 or target_team_NFL in name_1:
        
        # Get the Date / Game Status
        game_status = game['status']['type']['shortDetail']
        
        if target_team_NFL in name_0:
            # If Team 0 is the target, Team 1 is the opponent
            my_score = team_0['score']
            opp_name = name_1
            opp_score = team_1['score']
        else:
            # If Team 0 wasn't the target, Team 1 MUST be the target
            # So Team 0 is the opponent
            my_score = team_1['score']
            opp_name = name_0
            opp_score = team_0['score']
            
        print(f"Date/Status: {game_status}")
        print(f"{target_team_NFL}: {my_score}")
        print(f"Opponent: {opp_name} ({opp_score})")
        print("--------------------------------")

#Loop through games for NBA
for game in dataNBA['events']:
    matchup = game['competitions'][0]
    
    #matchup is the 2 teams playing against each other
    team_0 = matchup['competitors'][0]
    team_1 = matchup['competitors'][1]
    
    # Extract names to make checking easier
    name_0 = team_0['team']['displayName']
    name_1 = team_1['team']['displayName']
    
    if target_team_NBA in name_0 or target_team_NBA in name_1:
        
        # Get the Date / Game Status
        game_status = game['status']['type']['shortDetail']
        
        if target_team_NBA in name_0:
            # If Team 0 is the target, Team 1 is the opponent
            my_score = team_0['score']
            opp_name = name_1
            opp_score = team_1['score']
        else:
            # If Team 0 wasn't the target, Team 1 MUST be the target
            # So Team 0 is the opponent
            my_score = team_1['score']
            opp_name = name_0
            opp_score = team_0['score']
            
        print(f"Date/Status: {game_status}")
        print(f"{target_team_NBA}: {my_score}")
        print(f"Opponent: {opp_name} ({opp_score})")
        print("--------------------------------")