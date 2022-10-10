from main_etl import gw2_etl
import time

with open(r'C:\Users\DANIEL\workspace\gw2_srs\GW2_SRS\ETL\urls.txt') as f:

    count = 0
    nl = '\n'

    for line in f:
        count += 1
        stripped_line = line.strip()
        rep = stripped_line.replace('log', 'logContent')
        time.sleep(0.5)

        try:
            print(gw2_etl(rep))
            print(f"{nl}Log nº: {count}{nl}{('-'*10)}")
            time.sleep(1.0)
        except Exception as e:
            print(f"Error: {str(e)}")
            print('Line affected: ', line)
            pass

print('Finished!')

#--------------------------------------------
from main_etl import gw2_etl

dps_list = ['https://dps.report/3AOX-20220928-224933_sh','https://dps.report/Q4Pq-20220928-232112_dhuum','https://dps.report/OeXM-20220928-234635_ca','https://dps.report/kixH-20220929-000549_twins','https://dps.report/1fuJ-20220929-003141_qadim','https://dps.report/QSTK-20220926-224701_adina','https://dps.report/Hvth-20220926-231357_sabir','https://dps.report/7UO2-20220927-000023_qpeer']

for dps in dps_list:
    print(gw2_etl(dps))
    print('Done!')