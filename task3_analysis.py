import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def main():
    df = pd.read_csv("cleaned_data.csv")
    text = " ".join(df["keyword"])
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    words = text.split()
    stop_words = set(stopwords.words('english'))
    stop_words.update({"india"}) 
    filtered_words = [word for word in words if word not in stop_words]
    freq = pd.Series(filtered_words).value_counts().reset_index()
    freq.columns = ["word", "count"]
    freq.to_csv("analysis_results.csv", index=False)
    print("Clean analysis using NLTK")
    print(freq.head(10))

if __name__ == "__main__":
    main()