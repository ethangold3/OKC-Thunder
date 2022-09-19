import pandas as pd
import numpy as np

shots = pd.read_csv('shots_data.csv')

def C3_conditions(s):
    if (abs(s['x'])>22) and (s['y'] <= 7.8):
        return 1
    else:
        return 0

def NC3_conditions(s):
    if (((s['y']**2)+(s['x']**2))**(.5))>23.75 and (s['y'] > 7.8):
        return 1
    else:
        return 0
    
def TPT_conditions(s):
    if s['C3']==0 and s['NC3']==0:
        return 1
    else:
        return 0

    
shots['C3'] = shots.apply(C3_conditions, axis=1)
shots['NC3'] = shots.apply(NC3_conditions, axis=1)
shots['2PT'] = shots.apply(TPT_conditions, axis=1)


def print_shot_report(team_name,col):
    print("Percent of Shots Attempted in ",col," Zone by ",team_name,": ", round(shots.loc[shots['team'] == team_name, col].mean(),3))
    filtered_shots =shots.loc[(shots[col] == 1) & (shots['team'] == team_name)]
    made = filtered_shots['fgmade'].sum()
    if filtered_shots['2PT'].mean() ==0:
        made = made*1.5
    total = len(filtered_shots)
    print(col," EFG for ",team_name,": ",round(made/total,3))

print_shot_report("Team A","2PT")
print_shot_report("Team A","NC3")
print_shot_report("Team A","C3")
print_shot_report("Team B","2PT")
print_shot_report("Team B","NC3")
print_shot_report("Team B","C3")

