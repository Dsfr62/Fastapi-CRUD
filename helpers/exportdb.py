from sqlalchemy import engine
import pandas as pd

from config import dbEngine

def export_table(tablename:str, engine:engine=dbEngine):
    df = pd.read_sql_table(tablename, engine)
    return df.to_csv("{}.csv".format(tablename), index=False, header=True)