import pandas as pd

def preprocess():
    df = pd.read_csv('data/btc_data.csv')

    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    df = df.resample('D').mean()

    # ✅ FIXED LINE
    df = df.ffill()

    return df


if __name__ == "__main__":
    df = preprocess()
    print(df.head())