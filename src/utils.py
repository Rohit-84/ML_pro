import os
import sys
import pandas as pd

from dotenv import load_dotenv

import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

def mysql_connection():
    db = pymysql.connect(
        host = host,
        database=database,
        user=user,
        password=password)
    
    df = pd.read_sql_query("select * from Iris", db)
    print("succesfully connect to the databse")
    return df