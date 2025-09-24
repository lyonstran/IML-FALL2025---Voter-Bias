import pandas as pd
import matplotlib.pyplot as plt

def graph_weekly_bias(input_csv: str): # get weekly bias visuals for mean and std
    graph_weekly_bias_mean(input_csv)
    graph_weekly_bias_std(input_csv)

def graph_weekly_bias_mean(input_csv: str):
    df = pd.read_csv(input_csv)
    
    df = df.reset_index(drop=True)
    df['plot_index'] = range(len(df)) # x values be all the weeks 
    
    plt.figure(figsize=(16, 8))
    
    plt.plot(df['plot_index'], df['bias1_mean'], 'o-', label='AP Rank', linewidth=2, markersize=3) # set up the lines
    plt.plot(df['plot_index'], df['bias2_mean'], 's-', label='Mean', linewidth=2, markersize=3)
    plt.plot(df['plot_index'], df['bias3_mean'], '^-', label='Median', linewidth=2, markersize=3)
   
    week1_indices = df[df['week'] == 1]['plot_index'].tolist() 
    week1_years = df[df['week'] == 1]['season'].tolist()
    
    plt.xticks(week1_indices, week1_years) # only week 1 should indicate the year
    
    plt.title('Voter Bias Measurements', fontsize=16, fontweight='bold')
    plt.xlabel('Year (marked at Week 1)', fontsize=12)
    plt.ylabel('Bias (mean)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_week_mean.png') 

def graph_weekly_bias_std(input_csv: str):
    df = pd.read_csv(input_csv)
    
    df = df.reset_index(drop=True)
    df['plot_index'] = range(len(df)) # x values be all the weeks 
    
    plt.figure(figsize=(16, 8))
    
    plt.plot(df['plot_index'], df['bias1_std'], 'o-', label='AP Rank', linewidth=2, markersize=3) # set up the lines
    plt.plot(df['plot_index'], df['bias2_std'], 's-', label='Mean', linewidth=2, markersize=3)
    plt.plot(df['plot_index'], df['bias3_std'], '^-', label='Median', linewidth=2, markersize=3)
   
    week1_indices = df[df['week'] == 1]['plot_index'].tolist()
    week1_years = df[df['week'] == 1]['season'].tolist()
    
    plt.xticks(week1_indices, week1_years)
    
    plt.title('Voter Bias Measurements', fontsize=16, fontweight='bold')
    plt.xlabel('Year (marked at Week 1)', fontsize=12)
    plt.ylabel('Bias (std)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_week_std.png')

def graph_team_bias(input_csv: str): # runs team bias
    graph_team_bias_ap(input_csv)
    graph_team_bias_mean(input_csv)

def graph_team_bias_ap(input_csv: str):
    df = pd.read_csv(input_csv)

    team_avg_bias = df.groupby('team')['bias1_mean'].mean().sort_values() # group by year so each row is a different team 

    plt.figure(figsize=(40,10)) 
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=5)
    plt.yticks(fontsize=12)
    plt.ylabel("Average AP Rank Bias", fontsize=14)
    plt.title("Average Bias per Team", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_team_visual_ap.png')

def graph_team_bias_mean(input_csv: str):
    df = pd.read_csv(input_csv)

    team_avg_bias = df.groupby('team')['bias2_mean'].mean().sort_values()

    plt.figure(figsize=(40,10)) 
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=5)
    plt.yticks(fontsize=12)
    plt.ylabel("Average Mean Bias", fontsize=14)
    plt.title("Average Bias per Team", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_team_visual_mean.png')

def graph_voter_bias(input_csv: str): # runs voter bias
    graph_voter_bias_ap(input_csv)
    graph_voter_bias_mean(input_csv)

def graph_voter_bias_ap(input_csv: str):
    df = pd.read_csv(input_csv)
    team_avg_bias = df.groupby('voter')['bias1_mean'].mean().sort_values() # group by year so each row is a different team 

    plt.figure(figsize=(40,20)) 
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=5)
    plt.yticks(fontsize=12)
    plt.ylabel("Average AP Rank Bias", fontsize=14)
    plt.title("Average Bias per Voter", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_voter_visual_ap.png')

def graph_voter_bias_mean(input_csv: str):
    df = pd.read_csv(input_csv)
    team_avg_bias = df.groupby('voter')['bias2_mean'].mean().sort_values()

    plt.figure(figsize=(40,20)) 
    plt.bar(team_avg_bias.index, team_avg_bias.values, color='skyblue')
    plt.xticks(rotation=90, fontsize=5)
    plt.yticks(fontsize=12)
    plt.ylabel("Average Mean Bias", fontsize=14)
    plt.title("Average Bias per Voter", fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('cfb_ss_voter_visual_mean.png')


if __name__ == "__main__":
    graph_voter_bias("/Users/albertbogdan/IML-FALL2025---Voter-Bias/output_data/cfb/summary_stats/cfb_ss_voter.csv")