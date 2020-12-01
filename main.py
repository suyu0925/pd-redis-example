import pandas as pd
import pyarrow as pa
import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def save(df, key='test_df'):
    r.set(key, pa.serialize(df).to_buffer().to_pybytes())


def load(key='test_df'):
    df = pa.deserialize(r.get(key))
    return df


df = pd.DataFrame({'A': [1, 2, 3]})

save(df)

loaded_df = load()

df == loaded_df
