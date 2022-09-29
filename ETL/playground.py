from main_etl import gw2_etl
import time

with open('urls.txt') as f:

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
            time.sleep(2.5)
        except Exception as e:
            print(f"Error: {str(e)}")
            print('Line affected: ', line)
            pass

print('Finished!')

#--------------------------------------------
from main_etl import gw2_etl
print(gw2_etl('https://gw2wingman.nevermindcreations.de/logContent/20220926-010942_vg_kill'))