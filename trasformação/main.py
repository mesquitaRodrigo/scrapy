import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('/home/rodrigo/projetos/scrapy/data/shopee.jsonl',lines=True)

df = df.dropna(how='all')

df['ID'] = range(1, len(df) + 1)

pd.options.display.max_columns = None

df['_data_coleta'] = datetime.now()

df_expanded = df.join(pd.json_normalize(df["locationDetails"])).drop(columns=["locationDetails"])

conn = sqlite3.connect('/home/rodrigo/projetos/scrapy/data/shopee.db')

df_expanded.to_sql('shopee_items', conn, if_exists='replace', index=False)

conn.close()

print(df.head())

