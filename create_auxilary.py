import pandas as pd
from collections import defaultdict

def create_cam_rankings(csv_path: str):
    df_cam = pd.DataFrame(columns=["team", "year", "week", "ap_rank", "average", "median"])
    df_scraped = pd.read_csv(csv_path)  
    for (season, week), group in df_scraped.groupby(['Season', 'Week']):
        #y2014 w1, y2014 w2, etc.
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
        print(group)
        print("team ranks", team_ranks)

if __name__ == "__main__":
    create_cam_rankings("original_data/cfb_data_test_2014w1.csv")