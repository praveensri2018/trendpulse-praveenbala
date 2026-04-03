import pandas as pd
import os

def main():
    # Load JSON file
    file_path = "data/trends_20260403.json"

    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    df = pd.read_json(file_path)

    print(f"Loaded {len(df)} stories from {file_path}")

    df = df.drop_duplicates(subset="post_id", keep="first")
    print(f"After removing duplicates: {len(df)}")

    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")
    
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].fillna(0).astype(int)

    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}")

    # Clean title (remove spaces)
    df["title"] = df["title"].str.strip()

    # Save data into CSV file
    output_path = "data/trends_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"\nSaved {len(df)} rows to {output_path}")

    print("\nStories per category:")
    print(df["category"].value_counts())

if __name__ == "__main__":
    main()