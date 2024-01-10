"""Creating Dataframe using pandas."""
import os
import pandas as pd

import numpy as np

if __name__ == "__main__":
    # dictionary of lists
    data = {
        "First Score": [100, 90, np.nan, 95],
        "Second Score": [30, 45, 56, np.nan],
        "Third Score": [np.nan, 40, 80, 98],
    }
    # Creating a data frame from dict
    df = pd.DataFrame(data)

    # using isnull() function
    print(df.isnull())
    # filling null value
    new_df = df.fillna(0)
    print(new_df)
    # drop the null fields
    # df.dropna(inplace=True)
    # print(df)

    # Iterating over df
    for i, j in df.iterrows():
        print(i, j)
        print()
    # iterating over columns
    columns = list(df)
    for i in columns:
        # printing the third element of the columns
        print(df[i][2])
