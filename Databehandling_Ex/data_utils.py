import matplotlib.pyplot as plt
import pandas as pd

def plot_missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    
    if len(missing) == 0:
        print("No missing values found!")
        return
    
    plt.figure(figsize=(10, 6))
    missing.plot(kind='bar')
    plt.title('Columns with Missing Values')
    plt.ylabel('Number of Missing Values')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()