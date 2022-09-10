import pandas as pd
import json

def store_data():

    with open(r'C:\Users\DANIEL\workspace\gw2_srs\GW2_SRS\ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_1\Valley_Guardian\20220823-171406_vg_kill.json') as file:
        data = json.load(file)

    # Players Data:
    player_group = []
    player_acc = []
    player_names = []
    player_classes = []

    for player in data['players']:
        player_group.append(player['group'])
        player_acc.append(player['acc'])
        player_names.append(player['name'])
        player_classes.append(player['profession'])

    # Player's DPS Data:
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []

    phase1 = data['phases'][1]['dpsStats']

    phase1_time_raw = data['phases'][1]['duration']
    phase1_time = round(phase1_time_raw/1000,1)

    for dps in phase1:
        dps1_raw = dps[0]
        player_dps1.append(round(dps1_raw/phase1_time,2))

    phase2 = data['phases'][6]['dpsStats']

    phase2_time_raw = data['phases'][6]['duration']
    phase2_time = round(phase2_time_raw/1000,1)

    for dps in phase2:
        dps2_raw = dps[0]
        player_dps2.append(round(dps2_raw/phase2_time,2))

    phase3 = data['phases'][12]['dpsStats']

    phase3_time_raw = data['phases'][12]['duration']
    phase3_time = round(phase3_time_raw/1000,1)

    for dps in phase3:
        dps3_raw = dps[0]
        player_dps3.append(round(dps3_raw/phase3_time,2))

    stats_dict = {
        'players':{
            'group': player_group,
            'account': player_acc,
            'names': player_names,
            'profession': player_classes,
            'phase_1_dps': player_dps1,
            'phase_2_dps': player_dps2,
            'phase_3_dps': player_dps3
        }
    }

    df = pd.DataFrame(stats_dict['players'], columns=['group','account','names','profession','phase_1_dps','phase_2_dps','phase_3_dps'])

    pathName = 'ETL\TRANSFORM_01\Players_info'
    df.to_csv(f"{pathName}\player_stats.csv",index=True)

    return 'Success!'
pass

print(store_data())