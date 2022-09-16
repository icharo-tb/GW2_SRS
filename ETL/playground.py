from main_etl import gw2_etl

with open('urls.txt') as f:

    for line in f:
        stripped_line = line.strip()
        rep = stripped_line.replace('log', 'logContent')
        try:
            print(gw2_etl(rep))
        except Exception as e:
            print(f"Error: {str(e)}")