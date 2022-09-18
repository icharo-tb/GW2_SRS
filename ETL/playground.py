from main_etl import gw2_etl
import time
import sys

with open('urls.txt') as f:

    count = 0

    for line in f:
        count += 1
        stripped_line = line.strip()
        rep = stripped_line.replace('log', 'logContent')
        time.sleep(0.5)

        try:
            print(gw2_etl(rep))
            print()
            print('Count: ', count)
            print('-'*10)
            time.sleep(2.5)
        except Exception as e:
            print(f"Error: {str(e)}")
            print('Line affected:', line)
            sys.exit()

print('Finished!')