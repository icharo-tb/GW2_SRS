from time import sleep
from main_etl import gw2_etl
import time

with open('urls.txt') as f:

    for line in f:
        stripped_line = line.strip()
        rep = stripped_line.replace('log', 'logContent')
        try:
            print(gw2_etl(rep))
            time.sleep(5.0)
        except Exception as e:
            print(f"Error: {str(e)}")