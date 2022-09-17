from main_etl import gw2_etl
import time
import sys

with open('urls.txt') as f:

    for line in f:
        stripped_line = line.strip()
        rep = stripped_line.replace('log', 'logContent')
        time.sleep(2)

        try:
            print(gw2_etl(rep))
            print('-'*10)
            time.sleep(5)
        except Exception as e:
            print(f"Error: {str(e)}")
            print('Line affected:', line)
            sys.exit()