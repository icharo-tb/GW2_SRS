import json
from main_extract import Boss

with open('HUeg-20220829-210824_gors.json','r') as f:
    data = json.loads(f.read())

#p_data = data['players'][0]
#-----------Players Data-----------
# player_group = []
# player_acc = []
# player_names = []
# player_classes = []



# def player_data(p_data):

#     try:
#         player_group.append(p_data['group'])
#         player_acc.append(p_data['acc'])
#         player_names.append(p_data['name'])
#         player_classes.append(p_data['profession'])
#     except IndexError as e:
#         print(f'Error: {e}')

#     return True


class Encounter_Data:

    def __init__(self,data):
        self.__dict__ = dict(data)

class players(Encounter_Data):

    def findp(self):

        pgroup = []
        pacc = []
        pname = []
        pclass = []

        for i in data['players']:
            pgroup.append(i['group'])
            pacc.append(i['acc'])
            pname.append(i['name'])
            pclass.append(i['profession'])
        
        return pgroup, pacc, pname, pclass

class dps(Encounter_Data):

    def find_dps(self,name: str):


        player_dps1 = []
        player_dps2 = []
        player_dps3 = []
        player_dps4 = []
        player_dps5 = []
        player_dps6 = []

        ice_phase_dps = []
        fire_phase_dps = []
        storm_phase_dps = []
        abomination_phase_dps = []

        full_fight_dps_list = []

        from100_to75_dps = []
        from75_to50_dps = []
        from50_to25_dps = []
        from25_to0_dps = []

        from100_to10_dps = []
        from10_to0_dps = []

        pre_breakbar1_dps = []
        pre_breakbar2_dps = []
        pre_breakbar3_dps = []

        main_fight_dps = []
        dhuum_fight_dps = []
        ritual_dps = []

        burn1_dps = []
        burn2_dps = []
        burn3_dps = []

        nikare1_dps = []
        kenut1_dps = []

        nikare2_dps = []
        kenut2_dps = []

        nikare3_dps = []
        kenut3_dps = []

        qadimP1_dps = []
        qadimP2_dps = []
        qadimP3_dps = []


        pass
    pass

do = Encounter_Data(data)
print(do.players[1]['acc'])

ps = players(data).findp()

print(ps)


#-----------LOAD-----------

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

my_val = 'Tempest'
print(professions_dict[my_val])