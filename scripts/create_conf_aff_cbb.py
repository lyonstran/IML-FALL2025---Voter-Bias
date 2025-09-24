import pandas as pd
import time

def process_poll_data_cbb(df, year):
    season_df = df[df["Season"] == year]

    long_df = season_df.melt(
        id_vars=['Season', 'Week', 'Pollster'],
        value_vars=[str(i) for i in range(1, 26)],
        var_name='Rank',
        value_name='Team'
    ).dropna(subset=['Team'])

    rank_points = {str(i): 26 - i for i in range(1, 26)}
    long_df['Points'] = long_df['Rank'].map(rank_points)

    poll_df = (
        long_df.groupby(['Season', 'Week', 'Team'], as_index=False)['Points']
        .sum()
        .rename(columns={'Points': 'Total_Points'})
    )

    url = f'https://www.sports-reference.com/cbb/seasons/men/{year}.html'
    tables = pd.read_html(url, attrs={"id": "coaches-polls"})

    team_df = tables[0]

    if isinstance(team_df.columns, pd.MultiIndex):
        team_df.columns = [
            str(col[-1]) if "Unnamed" not in str(col[-1]) else str(col[0])
            for col in team_df.columns
        ]
    else:
        team_df.columns = [str(c).strip() for c in team_df.columns]

    school_col = [c for c in team_df.columns if "school" in c.lower()][0]
    conf_col   = [c for c in team_df.columns if "conf" in c.lower()][0]

    team_df = team_df[[school_col, conf_col]].copy()
    team_df.columns = ["School", "Conf"]

    team_df = team_df.dropna()
    team_df = team_df[team_df.School != 'School']

    def normalize_school(school):
        s = school.lower().strip()
        s = s.replace(".", "").replace("&", "and")
        if s == "uconn":
            return "connecticut"
        if s == "unc":
            return "north-carolina"
        if s == "smu":
            return "southern-methodist"
        if s.startswith("st "):
            return s.replace("st ", "saint ")
        return s.replace(" ", "-")

    poll_teams = poll_df['Team'].unique().tolist()

    map_school_to_mascot = {}
    for school in team_df['School'].unique():
        norm = normalize_school(school)
        matches = [t for t in poll_teams if t.startswith(norm)]
        if not matches:
            matches = [t for t in poll_teams if norm in t]
        if matches:
            map_school_to_mascot[school] = matches[0]

    team_df['School'] = team_df['School'].map(map_school_to_mascot)
    team_df = team_df.dropna(subset=['School'])

    conf_map = dict(zip(team_df['School'], team_df['Conf']))
    poll_df['Conference'] = poll_df['Team'].map(conf_map)

    poll_df = poll_df[['Season', 'Week', 'Team', 'Conference', 'Total_Points']]
    return poll_df

#cbb
def process_all_years_cbb(df):
    all_dfs = []
    for year in sorted(df.Season.unique()):
        try:
            season_df = process_poll_data_cbb(df, year)
            all_dfs.append(season_df)
            print(f"Processed {year}")
            time.sleep(20)
        except Exception as e:
            print(f"Skipped {year} due to error: {e}")
    all_years_df = pd.concat(all_dfs, ignore_index = True)
    return all_years_df