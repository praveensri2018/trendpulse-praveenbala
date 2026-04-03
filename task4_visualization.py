import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    file_path = "data/trends_analysed.csv"

    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    df = pd.read_csv(file_path)

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    top10 = df.sort_values(by="score", ascending=False).head(10)
    top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

    plt.figure(figsize=(8,6))
    plt.barh(top10["short_title"], top10["score"])
    plt.xlabel("Score")
    plt.ylabel("Story Title")
    plt.title("Top 10 Stories by Score")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("outputs/chart1_top_stories.png")

    category_counts = df["category"].value_counts()

    plt.figure(figsize=(6,4))
    plt.bar(category_counts.index, category_counts.values)
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.title("Stories per Category")
    plt.tight_layout()
    plt.savefig("outputs/chart2_categories.png")

    plt.figure(figsize=(6,4))

    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]

    plt.scatter(popular["score"], popular["num_comments"], label="Popular")
    plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

    plt.xlabel("Score")
    plt.ylabel("Number of Comments")
    plt.title("Score vs Comments")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/chart3_scatter.png")

    fig, axes = plt.subplots(1, 3, figsize=(18,5))

    axes[0].barh(top10["short_title"], top10["score"])
    axes[0].set_title("Top Stories")
    axes[0].invert_yaxis()

    axes[1].bar(category_counts.index, category_counts.values)
    axes[1].set_title("Category Count")

    axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
    axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
    axes[2].set_title("Score vs Comments")
    axes[2].legend()

    fig.suptitle("TrendPulse Dashboard")
    plt.tight_layout()
    plt.savefig("outputs/dashboard.png")

    print("Charts saved in outputs/ folder")

if __name__ == "__main__":
    main()