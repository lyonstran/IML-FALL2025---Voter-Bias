import pandas as pd
from collections import defaultdict
import statistics

def create_cam_rankings(csv_path: str):
    df_cam = pd.DataFrame(columns=["team", "year", "week", "ap_rank", "average", "median"])
    df_scraped = pd.read_csv(csv_path)
    
    for (season, week), group in df_scraped.groupby(['Season', 'Week']):
        team_ranks = defaultdict(list)
        for _, row in group.iterrows():
            for rank in range(1, 26):
                if rank == 1:
                    col_name = "1st"
                elif rank == 2:
                    col_name = "2nd"
                elif rank == 3:
                    col_name = "3rd"
                elif rank == 21:
                    col_name = "21st"
                elif rank == 22:
                    col_name = "22nd"
                elif rank == 23:
                    col_name = "23rd"
                else:
                    col_name = f"{rank}th"
                
                team_name = row[col_name]
                if pd.notna(team_name) and team_name != "":
                    team_ranks[team_name].append(rank)
        
        team_points = {}
        for team, ranks in team_ranks.items():
            total_points = 0
            for rank in ranks:
                points = 26 - rank
                total_points += points
            team_points[team] = total_points
        
        sorted_teams = sorted(team_points.items(), key=lambda x: x[1], reverse=True)
        for ap_rank, (team, points) in enumerate(sorted_teams, 1):
            ranks = team_ranks[team]
            mean_rank = statistics.mean(ranks)
            median_rank = statistics.median(ranks)
            
            new_row = {
                'team': team,
                'year': season,
                'week': week,
                'ap_rank': ap_rank if ap_rank <= 25 else 26,
                'average': mean_rank, 
                'median': median_rank,  
            }
            
            df_cam = pd.concat([df_cam, pd.DataFrame([new_row])], ignore_index=True)
            df_cam.to_csv("test_output.csv", index=False)
    
    return df_cam

if __name__ == "__main__":
    df_rankings = create_cam_rankings("original_data/cfb_data_test_2014w1.csv")