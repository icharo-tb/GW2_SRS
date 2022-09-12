pathString = r'C:\Users\DANIEL\workspace\gw2_srs\GW2_SRS\ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_7\Qadim_The_Peerless\20220829-102116_prlqadim_kill.json'
#pathString = r'C:\Users\DANIEL\workspace\gw2_srs\GW2_SRS\ETL\EXTRACT_00\Web Scraping\Boss_data\Wing_7\Qadim_The_Peerless\NCGe-20220825-155811_qpeer.json'

#-----------------------------------------

sp = pathString.split('\\')
posSp = sp[-1]

bossTag = posSp.split('_')
nameTag = bossTag[1]


if len(bossTag) > 2:
    nameTag = bossTag[1]
elif len(bossTag) == 2:
    tagSplit = nameTag.split('.')
    nameTag = tagSplit[0]

#-----------------------------------------
data = 'Hi'

player_group = []
player_acc = []
player_names = []
player_classes = []

for player in data['players']:
    player_group.append(player['group'])
    player_acc.append(player['acc'])
    player_names.append(player['name'])
    player_classes.append(player['profession'])

# Wing-1
if nameTag == 'vg':
    # Create lists:
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []

    # Add data sorting
    # Phase_1
    phase1 = data['phases'][1]['dpsStats']

    phase1_time_raw = data['phases'][1]['duration']
    phase1_time = round(phase1_time_raw/1000,1)

    for dps in phase1:
        dps1_raw = dps[0]
        player_dps1.append(round(dps1_raw/phase1_time,2))

    # Phase_2
    phase2 = data['phases'][6]['dpsStats']

    phase2_time_raw = data['phases'][6]['duration']
    phase2_time = round(phase2_time_raw/1000,1)

    for dps in phase2:
        dps2_raw = dps[0]
        player_dps2.append(round(dps2_raw/phase2_time,2))

    # Phase_3
    phase3 = data['phases'][12]['dpsStats']

    phase3_time_raw = data['phases'][12]['duration']
    phase3_time = round(phase3_time_raw/1000,1)

    for dps in phase3:
        dps3_raw = dps[0]
        player_dps3.append(round(dps3_raw/phase3_time,2))

    # Add dict
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

elif nameTag == 'gors':

    player_dps1 = []
    player_dps2 = []
    player_dps3 = []

    # Phase_1
    phase1_dps = data['phases'][1]['dpsStats']

    phase1_time_raw = data['phases'][1]['duration']
    phase1_time = round(phase1_time_raw/1000,1)

    for dps in phase1_dps:
        dps1_raw = dps[0]
        player_dps1.append(round(dps1_raw/phase1_time,2))
    
    # Phase_2
    phase2_dps = data['phases'][4]['dpsStats']

    phase2_time_raw = data['phases'][4]['duration']
    phase2_time = round(phase2_time_raw/1000,1)

    for dps in phase2_dps:
        dps2_raw = dps[0]
        player_dps2.append(round(dps2_raw/phase2_time,2))

    # Phase_3
    phase3_dps = data['phases'][7]['dpsStats']

    phase3_time_raw = data['phases'][7]['duration']
    phase3_time = round(phase3_time_raw/1000,1)

    for dps in phase3_dps:
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

elif nameTag == 'sab':
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []
    player_dps4 = []

    # Phase_1
    phase1_dps = data['phases'][1]['dpsStats']

    phase1_time_raw = data['phases'][1]['duration']
    phase1_time = round(phase1_time_raw/1000,1)

    for dps in phase1_dps:
        dps1_raw = dps[0]
        player_dps1.append(round(dps1_raw/phase1_time,2))

    # Phase_2
    phase2_dps = data['phases'][3]['dpsStats']

    phase2_time_raw = data['phases'][3]['duration']
    phase2_time = round(phase2_time_raw/1000,1)

    for dps in phase2_dps:
        dps2_raw = dps[0]
        player_dps2.append(round(dps2_raw/phase2_time,2))
    # Phase_3
    phase3_dps = data['phases'][6]['dpsStats']

    phase3_time_raw = data['phases'][6]['duration']
    phase3_time = round(phase3_time_raw/1000,1)

    for dps in phase3_dps:
        dps3_raw = dps[0]
        player_dps3.append(round(dps3_raw/phase3_time,2))
    # Phase_4
    phase4_dps = data['phases'][9]['dpsStats']

    phase4_time_raw = data['phases'][9]['duration']
    phase4_time = round(phase4_time_raw/1000,1)

    for dps in phase4_dps:
        dps4_raw = dps[0]
        player_dps4.append(round(dps4_raw/phase4_time,2))

    stats_dict = {
        'players':{
            'group': player_group,
            'account': player_acc,
            'names': player_names,
            'profession': player_classes,
            'phase_1_dps': player_dps1,
            'phase_2_dps': player_dps2,
            'phase_3_dps': player_dps3,
            'phase_4_dps': player_dps4
        }
    }

# Wing-2
elif nameTag == 'sloth':
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []
    player_dps4 = []
    player_dps5 = []
    player_dps6 = []

    # Phase_1
    phase1_dps = data['phases'][1]['dpsStats']

    phase1_time_raw = data['phases'][1]['duration']
    phase1_time = round(phase1_time_raw/1000,1)

    for dps in phase1_dps:
        dps1_raw = dps[0]
        player_dps1.append(round(dps1_raw/phase1_time,2))

    # Phase_2
    phase2_dps = data['phases'][3]['dpsStats']

    phase2_time_raw = data['phases'][3]['duration']
    phase2_time = round(phase2_time_raw/1000,1)

    for dps in phase2_dps:
        dps2_raw = dps[0]
        player_dps2.append(round(dps2_raw/phase2_time,2))

    # Phase_3
    phase3_dps = data['phases'][5]['dpsStats']

    phase3_time_raw = data['phases'][5]['duration']
    phase3_time = round(phase3_time_raw/1000,1)

    for dps in phase3_dps:
        dps3_raw = dps[0]
        player_dps3.append(round(dps3_raw/phase3_time,2))

    # Phase_4
    phase4_dps = data['phases'][7]['dpsStats']

    
    phase4_time_raw = data['phases'][7]['duration']
    phase4_time = round(phase4_time_raw/1000,1)

    for dps in phase4_dps:
        dps4_raw = dps[0]
        player_dps4.append(round(dps4_raw/phase4_time,2))

    # Phase_5
    phase5_dps = data['phases'][9]['dpsStats']

    phase5_time_raw = data['phases'][9]['duration']
    phase5_time = round(phase5_time_raw/1000,1)

    for dps in phase5_dps:
        dps5_raw = dps[0]
        player_dps5.append(round(dps5_raw/phase5_time,2))

    # Phase_6
    phase6_dps = data['phases'][11]['dpsStats']

    phase6_time_raw = data['phases'][11]['duration']
    phase6_time = round(phase6_time_raw/1000,1)

    for dps in phase6_dps:
        dps6_raw = dps[0]
        player_dps6.append(round(dps6_raw/phase6_time,2))

    stats_dict = {
        'players':{
            'group': player_group,
            'account': player_acc,
            'names': player_names,
            'profession': player_classes,
            'phase_1_dps': player_dps1,
            'phase_2_dps': player_dps2,
            'phase_3_dps': player_dps3,
            'phase_4_dps': player_dps4,
            'phase_5_dps': player_dps5,
            'phase_6_dps': player_dps6
        }
    }

elif nameTag == 'matt':
    ice_phase_dps = []
    fire_phase_dps = []
    storm_phase_dps = []
    abomination_phase_dps = []

    # Ice_phase
    ice_phase = data['phases'][1]['dpsStats']

    ice_phase_time_raw = data['phases'][1]['duration']
    ice_phase_time = round(ice_phase_time_raw/1000,1)

    for dps in ice_phase:
        dps_ice_raw = dps[0]
        ice_phase_dps.append(round(dps_ice_raw/ice_phase_time,2))

    # Fire_phase
    fire_phase = data['phases'][3]['dpsStats']

    fire_phase_time_raw = data['phases'][3]['duration']
    fire_phase_time = round(fire_phase_time_raw/1000,1)

    for dps in fire_phase:
        dps_fire_raw = dps[0]
        fire_phase_dps.append(round(dps_fire_raw/fire_phase_time,2))

    # Storm_phase
    storm_phase = data['phases'][5]['dpsStats']

    storm_phase_time_raw = data['phases'][5]['duration']
    storm_phase_time = round(storm_phase_time_raw/1000,1)

    for dps in storm_phase:
        dps_storm_raw = dps[0]
        storm_phase_dps.append(round(dps_storm_raw/storm_phase_time,2))

    # Abomination_phase
    abomination_phase = data['phases'][6]['dpsStats']

    abomination_phase_time_raw = data['phases'][6]['duration']
    abomination_phase_time = round(abomination_phase_time_raw/1000,1)

    for dps in abomination_phase:
        dps_abom_raw = dps[0]
        abomination_phase_dps.append(round(dps_abom_raw/abomination_phase_time,2))

    stats_dict = {
        'players':{
            'group': player_group,
            'account': player_acc,
            'names': player_names,
            'profession': player_classes,
            'ice_phase_dps': ice_phase_dps,
            'fire_phase_dps': fire_phase_dps,
            'storm_phase_dps': storm_phase_dps,
            'abomination_phase_dps': abomination_phase_dps
        }
    }

# Wing-3
elif nameTag == 'kc':
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []
elif nameTag == 'xera':
    player_dps1 = []
    player_dps2 = []

# Wing-4
elif nameTag == 'cairn':
    full_fight_dps = []
elif nameTag == 'mo':
    from100_to75_dps = []
    from75_to50_dps = []
    from50_to25_dps = []
    from25_to0_dps = []
elif nameTag == 'sam':
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []
elif nameTag == 'dei':
    from100_to10_dps = []
    from10_to0_dps = []

# Wing-5
elif nameTag == 'sh':
    pre_breakbar1_dps = []
    pre_breakbar2_dps = []
    pre_breakbar3_dps = []
elif nameTag == 'dhuum':
    main_fight_dps = []
    dhuum_fight_dps = []
    ritual_dps = []

# Wing-6
elif nameTag == 'ca':
    burn1_dps = []
    burn2_dps = []
    burn3_dps = []
elif nameTag == 'twinlargos':
    nikare1_dps = []
    kenut1_dps = []

    nikare2_dps = []
    kenut2_dps = []

    nikare3_dps = []
    kenut3_dps = []
elif nameTag == 'qadim':
    qadimP1_dps = []
    qadimP2_dps = []
    qadimP3_dps = []

# Wing-7
elif nameTag == 'adina':
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []
    player_dps4 = []
elif nameTag == 'sabir':
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []
elif nameTag == 'prlqadim' or nameTag == 'qpeer':
    player_dps1 = []
    player_dps2 = []
    player_dps3 = []
    player_dps4 = []
    player_dps5 = []
    player_dps6 = []