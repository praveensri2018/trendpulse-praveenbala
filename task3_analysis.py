import pandas as pd
import numpy as np
import os

def main():
    file_path = "data/trends_clean.csv"

    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    df = pd.read_csv(file_path)

    print(f"Loaded data: {df.shape}")

    print("\nFirst 5 rows:")
    print(df.head())

    avg_score = df["score"].mean()
    avg_comments = df["num_comments"].mean()

    print(f"\nAverage score   : {avg_score:.2f}")
    print(f"Average comments: {avg_comments:.2f}")

    print("\n--- NumPy Stats ---")

    scores = df["score"].values

    print(f"Mean score   : {np.mean(scores):.2f}")
    print(f"Median score : {np.median(scores):.2f}")
    print(f"Std deviation: {np.std(scores):.2f}")
    print(f"Max score    : {np.max(scores)}")
    print(f"Min score    : {np.min(scores)}")

    category_counts = df["category"].value_counts()
    top_category = category_counts.idxmax()
    top_count = category_counts.max()

    print(f"\nMost stories in: {top_category} ({top_count} stories)")

    max_comments_row = df.loc[df["num_comments"].idxmax()]
    print(f'\nMost commented story: "{max_comments_row["title"]}" — {max_comments_row["num_comments"]} comments')

    df["engagement"] = df["num_comments"] / (df["score"] + 1)

    df["is_popular"] = df["score"] > avg_score

    output_path = "data/trends_analysed.csv"
    df.to_csv(output_path, index=False)

    print(f"\nSaved to {output_path}")

if __name__ == "__main__":
    main()