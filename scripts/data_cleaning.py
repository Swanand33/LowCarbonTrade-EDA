import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df_cleaned = df.dropna()
    return df_cleaned

if __name__ == "__main__":
    cleaned_data = clean_data("data/Trade_in_Low_Carbon_Technology_Products.csv")
    cleaned_data.to_csv("data/cleaned_trade_data.csv", index=False)