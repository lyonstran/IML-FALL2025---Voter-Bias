import pandas as pd

def create_cam_rankings(csv_path: str):
    df = pd.read_csv(csv_path)  
    for (season, week), group in df.groupby(['Season', 'Week']):
        print(group)
        break

if __name__ == "__main__":
    create_cam_rankings("original_data/college_football_polls_original.csv")