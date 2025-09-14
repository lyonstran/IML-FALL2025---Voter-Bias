import pandas as pd
from collections import defaultdict
import statistics


def create_cam_rankings(csv_path: str): # for every team in a year/week, 
    df_cam = pd.DataFrame(columns=["team", "year", "week", "ap_rank", "average", "median"]) # df to be returned
    df_scraped = pd.read_csv(csv_path) 
    df_scraped['Season'] = pd.to_numeric(df_scraped['Season'], errors='coerce') # to order numbers
    df_scraped['Week'] = pd.to_numeric(df_scraped['Week'], errors='coerce') # to order numbers

    for (season, week), group in df_scraped.groupby(['Season', 'Week']): # go through by each week/year
        team_ranks = defaultdict(list) # map, (team -> all AP ranks for that week/year)
        for _, row in group.iterrows():
            for rank in range(1, 26):
                team_name = row.iloc[rank] 
                if pd.notna(team_name) and team_name != "":
                    team_ranks[team_name].append(rank)
                else:
                    team_ranks[team_name].append(26)
        
        team_points = {}
        for team, ranks in team_ranks.items():
            total_points = 0
            for rank in ranks:
                points = 26 - rank
                total_points += points
            team_points[team] = total_points
        
        filtered_team_points = {team: points for team, points in team_points.items() if isinstance(team, str) and team.strip() != "" and not team.isdigit()} # gets rid of week and year in DF
        sorted_teams = sorted(filtered_team_points.items(), key=lambda x: x[1], reverse=True) # from first to last, get summary statistics
        for ap_rank, (team, points) in enumerate(sorted_teams, 1):
            ranks = team_ranks[team]
            mean_rank = statistics.mean(ranks)
            mean_rank = round(mean_rank, 3)
            median_rank = statistics.median(ranks)
            
            new_row = {
                'team': team,
                'year': int(season),
                'week': int(week),
                'ap_rank': ap_rank if ap_rank <= 25 else 26,
                #'ap_rank': ap_rank, <- leave no cap on, which I'd assume would extend the ranks (if we want to go past 26) 
                #'points' : points, #<- would it be helpful to keep track of total points? 
                # ^^^^ the commented code I think would make sense if we want to try and extend beyond top 25, otherwise
                #           we could always set non ranked teams to 0; whichever makes most sense for our goals
                # I'm leaning towards maybe cutting out the non ranked teams? (you mentioned the average and median need to 
                # be determined) 
                'average': mean_rank, 
                'median': median_rank,  
            }
            
            df_cam.loc[len(df_cam)] = new_row
    df_cam.to_csv("cam_output.csv", index=False)
    return df_cam

def create_voters(csv_path: str): # df of all voters in a certain week/year
    df_voters = pd.DataFrame(columns=["year", "week", "voters"]) # df to be returned
    df_scraped = pd.read_csv(csv_path) 

    df_scraped['Season'] = pd.to_numeric(df_scraped['Season'], errors='coerce') 
    for (season, week), group in df_scraped.groupby(['Season', 'Week']): # sort by week/year
        voters = set() # set of all voters
        for _, row in group.iterrows():
            voters.add(row["Pollster"]) # add all the voters into the set
        new_row = {
                'year': int(season),
                'week': int(week),
                'voters': tuple(voters), 
            }   # make the new row
        df_voters.loc[len(df_voters)] = new_row
    df_voters = df_voters.sort_values(['year', 'week']).reset_index(drop=True)   # organize df by week/year  
    df_voters.to_csv("create_voters_output.csv", index=False)
    return df_voters

def create_teams(csv_path: str): # df of all teams in a certain week/year
    df_teams = pd.DataFrame(columns=["year", "week", "teams"]) # df to be returned
    df_scraped = pd.read_csv(csv_path) 

    df_scraped['Season'] = pd.to_numeric(df_scraped['Season'], errors='coerce') 
    for (season, week), group in df_scraped.groupby(['Season', 'Week']): # sort by week/year
        teams = set() # set of all teams
        for _, row in group.iterrows():
            for i in range (1, 26):
                teams.add(row[str(i)]) # add all the teams into the set
        new_row = {
                'year': int(season),
                'week': int(week),
                'teams': tuple(teams), 
            }   # make the new row
        df_teams.loc[len(df_teams)] = new_row
    df_teams = df_teams.sort_values(['year', 'week']).reset_index(drop=True)   # organize df by week/year  
    df_teams.to_csv("create_teams_output.csv", index=False)
    return df_teams

if __name__ == "__main__":
    #df_rankings = create_cam_rankings("original_data/college_basketball_polls_original.csv")
    df_voters = create_teams("/Users/albertbogdan/IML-FALL2025---Voter-Bias/original_data/college_basketball_polls_original.csv")