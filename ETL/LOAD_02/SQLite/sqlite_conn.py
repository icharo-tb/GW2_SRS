import sqlite3
import json
import pandas as pd

def sqlite_conn(file):

    with open(file) as f:
        jsonString = json.load(f)

    conn = sqlite3.connect(r'C:\Users\DANIEL\OneDrive\Escritorio\BD_Study\SQL\SQLite\SQLite_queries\gw2_srs.db')
    print('Connected!')

    cur = conn.cursor()
    print(cur)

    cur.execute(
        'DROP TABLE IF EXISTS dhuum_player_stats_01'
    )
    conn.commit()
    print('Table droped!')

    cur.execute(
        'CREATE TABLE IF NOT EXISTS dhuum_player_stats_01 ("field1" INTEGER, "group" INTEGER, "account" TEXT, "names" TEXT, "profession" TEXT, "Main_fight_dps" INTEGER, "Dhuum_fight_dps" INTEGER, "Ritual_dps" INTEGER)'
    )
    conn.commit()
    print('Table created!')

    df = pd.DataFrame(jsonString, columns=['id','group','account','names','profession','Main_fight_dps','Dhuum_fight_dps','Ritual_dps'])
    df.to_sql('dhuum_player_stats_01', conn, if_exists='replace', index=False)
    print('Dataframe completed!')

    return 'Done!'

print(sqlite_conn(r'C:\Users\DANIEL\workspace\gw2_srs\GW2_SRS\ETL\TRANSFORM_01\Players_info\18_dhuum_player_stats.json'))

#------------------------------------------

import sqlite3

name_lst = ['dudu1','mecha1','scrapper1']

conn = sqlite3.connect(r'C:\Users\DANIEL\OneDrive\Escritorio\BD_Study\SQL\SQLite\SQLite_queries\gw2_srs.db')
print('Connected!')

cur = conn.cursor()
print(cur)

for name in name_lst:
    cur.execute(
        f'INSERT INTO player_info(name) VALUES("{name}")'
    )
    conn.commit()
    print('Data inserted!')