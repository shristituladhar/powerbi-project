import pandas as pd
import json

df = pd.read_csv('2023 building footprints (Project 2).csv')


def clean_geo_shape(geo_shape):
    try:
        geo_data = json.loads(geo_shape)
        geo_str = json.dumps(geo_data)
        return geo_str[:65535]
    except json.JSONDecodeError:
        return ''


df['Geo Shape'] = df['Geo Shape'].apply(clean_geo_shape)

df = df.fillna('')
df.to_csv('buildingfootprints.csv', index=False)
