import pandas as pd

def main():
    df = pd.read_csv("raw_data.csv")
    df = df.drop_duplicates()
    df["keyword"] = df["keyword"].str.lower().str.strip()
    df = df[df["keyword"] != ""]
    df.to_csv("cleaned_data.csv", index=False, encoding="utf-8")
    print("Data cleaned successfully")
    print(df.head())

if __name__ == "__main__":
    main()