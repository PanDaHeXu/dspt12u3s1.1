import pandas as pd
import time

df = pd.DataFrame([[1, 4, 6], [2, 4, 5], [1, 1, 0]])

while 1 == 1:

    time.sleep(2)
    df = df + 1
    print(df.head())
