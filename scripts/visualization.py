import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_heatmap(df):
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned_trade_data.csv")
    plot_correlation_heatmap(df)