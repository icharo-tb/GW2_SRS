from dotenv import load_dotenv
import os
from pathlib import Path
import mysql.connector

dotenv_path = Path('ETL\LOAD_02\.env')
load_dotenv(dotenv_path=dotenv_path)

USER_PASS = os.getenv('MYQSL_PASS')

db = mysql.connector.connect(host ="localhost",user="root",passwd=USER_PASS)