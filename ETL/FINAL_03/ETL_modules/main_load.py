#----------------IMPORTS-----------------
import sys
import pymongo
import sqlite3

#----------------MAIN FUNCTION-----------------

def load():
    print('-'*10)

    #-----------SQLite conn-----------
    print('SQLite conn starting...')

    try:
        conn = sqlite3.connect(r'C:\Users\DANIEL\OneDrive\Escritorio\BD_Study\SQL\SQLite\SQLite_queries\gw2_srs.db')
        cur = conn.cursor()
    except Exception as e:
        print('Connection could not be done' + str(e))
        sys.exit()
    
    #-----------DPS data insert-----------
    try:
        if nameTag == 'vg':
            boss_id = 1

            for (dps1,dps2,dps3,acc) in zip(player_dps1,player_dps2,player_dps3,player_acc):
                cur.execute(
                    f"INSERT INTO vg_dps(phase1_dps,phase2_dps,phase3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'gors':
            boss_id = 2
            
            for (dps1,dps2,dps3,acc) in zip(player_dps1,player_dps2,player_dps3,player_acc):
                cur.execute(
                    f"INSERT INTO gors_dps(phase1_dps,phase2_dps,phase3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'sab':
            boss_id = 3
            
            for (dps1,dps2,dps3,dps4,acc) in zip(player_dps1,player_dps2,player_dps3,player_dps4,player_acc):
                cur.execute(
                    f"INSERT INTO sab_dps(phase1_dps,phase2_dps,phase3_dps,phase4_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},{dps4},'{acc}')"
                )
        elif nameTag == 'sloth':
            boss_id = 4

            for (dps1,dps2,dps3,dps4,dps5,dps6,acc) in zip(player_dps1,player_dps2,player_dps3,player_dps4,player_dps5,player_dps6,player_acc):
                cur.execute(
                    f"INSERT INTO sloth_dps(phase1_dps,phase2_dps,phase3_dps,phase4_dps,phase5_dps,phase6_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},{dps4},{dps5},{dps6},'{acc}')"
                )
        elif nameTag == 'matt':
            boss_id = 5

            for (dps1,dps2,dps3,dps4,acc) in zip(ice_phase_dps,fire_phase_dps,storm_phase_dps,abomination_phase_dps,player_acc):
                cur.execute(
                    f"INSERT INTO matt_dps(ice_dps,fire_dps,storm_dps,abomination_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},{dps4},'{acc}')"
                )
        elif nameTag == 'kc':
            boss_id = 6

            for (dps1,dps2,dps3,acc) in zip(player_dps1,player_dps2,player_dps3,player_acc):
                cur.execute(
                    f"INSERT INTO kc_dps(phase1_dps,phase2_dps,phase3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'xera':
            boss_id = 7

            for (dps1,dps2,acc) in zip(player_dps1,player_dps2,player_acc):
                cur.execute(
                    f"INSERT INTO xera_dps(phase1_dps,phase2_dps,FK_player_id) VALUES({dps1},{dps2},'{acc}')"
                )
        elif nameTag == 'cairn':
            boss_id = 8

            for (dps1,acc) in zip(full_fight_dps_list,player_acc):
                cur.execute(
                    f"INSERT INTO cairn_dps(full_fight_dps,FK_player_id) VALUES({dps1},'{acc}')"
                )
        elif nameTag == 'mo':
            boss_id = 9

            for (dps1,dps2,dps3,dps4,acc) in zip(from100_to75_dps,from75_to50_dps,from50_to25_dps,from25_to0_dps,player_acc):
                cur.execute(
                    f"INSERT INTO mo_dps(_100to75,_75to50,_50to25,_25to0,FK_player_id) VALUES({dps1},{dps2},{dps3},{dps4},'{acc}')"
                )
        elif nameTag == 'sam':
            boss_id = 10

            for (dps1,dps2,dps3,acc) in zip(player_dps1,player_dps2,player_dps3,player_acc):
                cur.execute(
                    f"INSERT INTO sam_dps(phase1_dps,phase2_dps,phase3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'dei':
            boss_id = 11

            for (dps1,dps2,acc) in zip(from100_to10_dps,from10_to0_dps,player_acc):
                cur.execute(
                    f"INSERT INTO dei_dps(_100to10,_10to0,FK_player_id) VALUES({dps1},{dps2},'{acc}')"
                )
        elif nameTag == 'sh':
            boss_id = 12

            for (dps1,dps2,dps3,acc) in zip(pre_breakbar1_dps,pre_breakbar2_dps,pre_breakbar3_dps,player_acc):
                cur.execute(
                    f"INSERT INTO sh_dps(prebreakbar1_dps,prebreakbar2_dps,prebreakbar3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'dhuum':
            boss_id = 13

            for (dps1,dps2,dps3,acc) in zip(main_fight_dps,dhuum_fight_dps,ritual_dps,player_acc):
                cur.execute(
                    f"INSERT INTO dhuum_dps(main_fight_dps,dhuum_fight_dps,ritual_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'ca':
            boss_id = 14

            for (dps1,dps2,dps3,acc) in zip(burn1_dps,burn2_dps,burn3_dps,player_acc):
                cur.execute(
                    f"INSERT INTO ca_dps(burn1_dps,burn2_dps,burn3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'twinlargos' or nameTag == 'twins':
            boss_id = 15

            for (dps1,dps2,dps3,dps4,dps5,dps6,acc) in zip(nikare1_dps,kenut1_dps,nikare2_dps,kenut2_dps,nikare3_dps,kenut3_dps,player_acc):
                cur.execute(
                    f"INSERT INTO twinlargos_dps(nikare1_dps,kenut1_dps,nikare2_dps,kenut2_dps,nikare3_dps,kenut3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},{dps4},{dps5},{dps6},'{acc}')"
                )
        elif nameTag == 'qadim':
            boss_id = 16

            for (dps1,dps2,dps3,acc) in zip(qadimP1_dps,qadimP2_dps,qadimP3_dps,player_acc):
                cur.execute(
                    f"INSERT INTO qadim1_dps(qadim_p1_dps,qadim_p2_dps,qadim_p3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'adina':
            boss_id = 17

            for (dps1,dps2,dps3,dps4,acc) in zip(player_dps1,player_dps2,player_dps3,player_dps4,player_acc):
                cur.execute(
                    f"INSERT INTO adina_dps(phase1_dps,phase2_dps,phase3_dps,phase4_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},{dps4},'{acc}')"
                )
        elif nameTag == 'sabir':
            boss_id = 18

            for (dps1,dps2,dps3,acc) in zip(player_dps1,player_dps2,player_dps3,player_acc):
                cur.execute(
                    f"INSERT INTO sabir_dps(phase1_dps,phase2_dps,phase3_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},'{acc}')"
                )
        elif nameTag == 'prlqadim' or nameTag == 'qpeer':
            boss_id = 19

            for (dps1,dps2,dps3,dps4,dps5,dps6,acc) in zip(player_dps1,player_dps2,player_dps3,player_dps4,player_dps5,player_dps6,player_acc):
                cur.execute(
                    f"INSERT INTO prlqadim_dps(phase1_dps,phase2_dps,phase3_dps,phase4_dps,phase5_dps,phase6_dps,FK_player_id) VALUES({dps1},{dps2},{dps3},{dps4},{dps5},{dps6},'{acc}')"
                )
    except Exception as e:
        print(f"Failed to insert dps data: {str(e)}")
    
    #-----------Players name, profession and account data insert-----------
    for (name,acc,profession) in zip(player_names,player_acc,player_classes):

        if profession == 'Guardian':
            class_id = 1
        elif profession == 'Dragonhunter':
            class_id = 2
        elif profession == 'Firebrand':
            class_id = 3
        elif profession == 'Willbender':
            class_id = 4
        elif profession == 'Revenant':
            class_id = 5
        elif profession == 'Herald':
            class_id = 6
        elif profession == 'Renegade':
            class_id = 7
        elif profession == 'Vindicator':
            class_id = 8
        elif profession == 'Warrior':
            class_id = 9
        elif profession == 'Berserker':
            class_id = 10
        elif profession == 'Spellbreaker':
            class_id = 11
        elif profession == 'Bladesworn':
            class_id = 12
        elif profession == 'Engineer':
            class_id = 13
        elif profession == 'Scrapper':
            class_id = 14
        elif profession == 'Holosmith':
            class_id = 15
        elif profession == 'Mechanist':
            class_id = 16
        elif profession == 'Ranger':
            class_id = 17
        elif profession == 'Druid':
            class_id = 18
        elif profession == 'Soulbeast':
            class_id = 19
        elif profession == 'Untamed':
            class_id = 20
        elif profession == 'Thief':
            class_id = 21
        elif profession == 'Daredevil':
            class_id = 22
        elif profession == 'Deadeye':
            class_id = 23
        elif profession == 'Specter':
            class_id = 24
        elif profession == 'Elementalist':
            class_id = 25
        elif profession == 'Tempest':
            class_id = 26
        elif profession == 'Weaver':
            class_id = 27
        elif profession == 'Catalyst':
            class_id = 28
        elif profession == 'Mesmer':
            class_id = 29
        elif profession == 'Chronomancer':
            class_id = 30
        elif profession == 'Mirage':
            class_id = 31
        elif profession == 'Virtuoso':
            class_id = 32
        elif profession == 'Necromancer':
            class_id = 33
        elif profession == 'Reaper':
            class_id = 34
        elif profession == 'Scourge':
            class_id = 35
        elif profession == 'Harbinger':
            class_id = 36
        cur.execute(
            f'INSERT INTO player_info(account,name,boss_id,profession_id) VALUES("{acc}","{name}",{boss_id},{class_id})'
        )
        conn.commit()
    print('Player data inserted!')

    print('-'*10)

    #-----------MongoDB conn-----------
    print('MongoDB conn starting...')

    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
    except Exception as e:
        print('Connection could not be done' + str(e))
        sys.exit()

    db = client['GW2_SRS']
    collection = db['players_info']

    collection.insert_one(json_data)
    print('MongoDB load done!')