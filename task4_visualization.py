import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("analysis_results.csv").head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(df["word"], df["count"])
    plt.xlabel("Count")
    plt.ylabel("Word")
    plt.title("Top 10 Trending Words")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("trend_visualization.png")
    plt.show()
    print("Visualization created")

if __name__ == "__main__":
    main()