import pandas as pd

#------------
#cfb
#------------
ballot = pd.read_csv(r"C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\original_data\college_football_polls_original.csv")
reference = pd.read_csv(r"C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\output_data\cfb\cfb_cam_output.csv")
long_format = ballot.melt(
    id_vars=["Pollster", "Season", "Week"],
    value_vars=[str(i) for i in range(1, 26)],
    var_name="Rank",
    value_name="Team"
).dropna(subset = ['Team'])
long_format['Rank'] = long_format['Rank'].astype(int)


reference = reference.rename(columns = {"year": "Season", "week": "Week", "team": "Team"})
long_format["Season"] = long_format["Season"].astype(str)
long_format["Week"] = long_format["Week"].astype(str)
long_format["Team"] = long_format["Team"].astype(str)
reference["Season"] = reference["Season"].astype(str)
reference["Week"] = reference["Week"].astype(str)
reference["Team"] = reference["Team"].astype(str)


merge = long_format.merge(reference, on = ["Season", "Week", "Team"], how = "left")
merge = merge.dropna()
merge["bias1(v, t)"] = (merge["Rank"] - merge["ap_rank"]) / merge[["Rank", "ap_rank"]].min(axis = 1)
merge["bias2(v, t)"] = (merge["Rank"] - merge["average"]) / merge[["Rank", "average"]].min(axis = 1)
merge["bias3(v, t)"] = (merge["Rank"] - merge["median"]) / merge[["Rank", "median"]].min(axis = 1)
merge["bias0(v, t)_ap"] = (merge["Rank"] - merge["ap_rank"]) 
merge["bias0(v, t)_mean"] = (merge["Rank"] - merge["average"]) 

merge = merge.rename(columns = {'Team' : 'Team (t)', 'Pollster' : 'Pollster (v)'})
#merge.to_csv('cfb_master_bias_file.csv', index = False) <- uncomment to save file 

#------
# cfb_master_relative_percentage_bias
#------
df = merge.copy()
df["bias1(v, t)"] = df["bias1(v, t)"] * 100                 #bias1 - bias3 represent percent difference. 
df["bias2(v, t)"] = df["bias2(v, t)"] * 100
df["bias3(v, t)"] = df["bias3(v, t)"] * 100
# should bias0 be scaled as well? 

df.round(3)
df.to_csv('cfb_master_relative_percentage_bias.csv', index = False)

#---------
#cbb
#---------
# ballot2 = pd.read_csv(r'C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\original_data\college_basketball_polls_original.csv')
# reference2 = pd.read_csv(r'C:\Users\lyons\OneDrive\Desktop\IML-FALL2025---Voter-Bias\output_data\cbb\cbb_cam_output.csv')
# long_format2 = ballot2.melt(
#     id_vars=["Pollster", "Season", "Week"],
#     value_vars=[str(i) for i in range(1, 26)],
#     var_name="Rank",
#     value_name="Team"
# ).dropna(subset = ['Team'])

# long_format2['Rank'] = long_format2['Rank'].astype(int)

# long_format2["Season"] = long_format2["Season"].astype(str)
# long_format2["Week"] = long_format2["Week"].astype(str)
# long_format2["Team"] = long_format2["Team"].astype(str)

# reference2 = reference2.rename(columns={"year": "Season", "week": "Week", "team": "Team"})

# reference2["Season"] = reference2["Season"].astype(str)
# reference2["Week"] = reference2["Week"].astype(str)
# reference2["Team"] = reference2["Team"].astype(str)

# merge2 = long_format2.merge(reference2, on=["Season", "Week", "Team"], how="left")
# merge2 = merge2.dropna()
# merge2["bias1(v, t)"] = (merge2["Rank"] - merge2["ap_rank"]) / merge2[["Rank", "ap_rank"]].min(axis = 1)
# merge2["bias2(v, t)"] = (merge2["Rank"] - merge2["average"]) / merge2[["Rank", "average"]].min(axis = 1)
# merge2["bias3(v, t)"] = (merge2["Rank"] - merge2["median"]) / merge2[["Rank", "median"]].min(axis = 1)
# merge2 = merge2.rename(columns = {'Team' : 'Team (t)', 'Pollster' : 'Pollster (v)'})



# merge2.to_csv('cbb_master_bias_file.csv', index = False)