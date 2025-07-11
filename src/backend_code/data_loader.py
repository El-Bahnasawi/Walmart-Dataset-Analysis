import pandas as pd


def load_data():
    train_df = pd.read_csv("data/train.csv")
    features_df = pd.read_csv("data/features.csv")
    stores_df = pd.read_csv("data/stores.csv")

    df = (train_df
           .merge(features_df, how='left', indicator=True)
           .merge(stores_df, how='left'))
    
    df = df.loc[df['Weekly_Sales'] > 0] #outliers

    df['month'] = pd.DatetimeIndex(df['Date']).month #extract month data

    df.drop("_merge", axis=1, inplace=True)
    df['Total_MarkDown'] = df[['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']].sum(axis=1)

#     df = df.sample(frac=0.5, random_state=42)
    return df