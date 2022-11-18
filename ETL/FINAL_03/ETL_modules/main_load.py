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

        professions_dict = {
            "Guardian": 1,"Dragonhunter": 2,"Firebrand": 3,"Willbender": 4,
            "Revenant": 5,"Herald": 6,"Renegade": 7,"Vindicator": 8,
            "Warrior": 9,"Berserker": 10,"Spellbreaker": 11,"Bladesworn": 12,
            "Engineer": 13,"Scrapper": 14,"Holosmith": 15,"Mechanist": 16,
            "Ranger": 17,"Druid": 18,"Soulbeast": 19,"Untamed": 20,
            "Thief": 21,"Daredevil": 22,"Deadeye": 23,"Specter": 24,
            "Elementalist": 25,"Tempest": 26,"Weaver": 27,"Catalyst": 28,
            "Mesmer": 29,"Chronomancer": 30,"Mirage": 31,"Virtuoso": 32,
            "Necromancer": 33,"Reaper": 34,"Scourge": 35,"Harbinger": 36
        }

        class_id = professions_dict[profession]
        
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