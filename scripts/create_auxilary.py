import pandas as pd
from collections import defaultdict
import statistics


def create_cam_rankings(csv_path: str): # for every team in a year/week, 
    df_cam = pd.DataFrame(columns=["team", "year", "week", "ap_rank", "average", "median"]) # df to be returned
    df_scraped = pd.read_csv(csv_path) 

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
                'year': season,
                'week': week,
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
    df_cam.to_csv("test_output.csv", index=False)
    return df_cam

def create_voters(csv_path: str):
    return "work in progress"

def create_teams(csv_path: str):
    return "work in progress"

if __name__ == "__main__":
    df_rankings = create_cam_rankings("original_data/college_basketball_polls_original.csv")