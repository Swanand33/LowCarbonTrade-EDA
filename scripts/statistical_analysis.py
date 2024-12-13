import pandas as pd
import scipy.stats as stats

def perform_ttest(df, column, year_threshold):
    before = df[df['Year'] < year_threshold][column].dropna()
    after = df[df['Year'] >= year_threshold][column].dropna()
    return stats.ttest_ind(before, after, equal_var=False)

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_trade_data.csv")
    t_stat, p_value = perform_ttest(df, 'Trade_Value', 2010)
    print(f"T-Statistic: {t_stat}, P-Value: {p_value}")