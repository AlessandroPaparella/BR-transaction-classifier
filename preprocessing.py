import pandas as pd


df = pd.read_csv("train.csv")
df['Label0']=df['Label0'].map({False:0, True:1})
df=df.drop(["txData", "txHash"], axis=1)

import gc
gc.collect()

from sklearn.model_selection import train_test_split
train, val = train_test_split(df, test_size=0.1, random_state=42)


df = None
import gc

gc.collect()

train.to_csv('training.csv', index=False)
val.to_csv('validation.csv', index=False)

df = pd.read_csv("test.csv")
df=df.drop(["txData", "txHash"], axis=1)
df.to_csv('test.csv', index=False)

