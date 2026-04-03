# TrendPulse - Data Pipeline Project

## Overview
TrendPulse is a simple data pipeline project that fetches live trending data, processes it, analyzes patterns, and visualizes insights using Python.

---

## Project Workflow

1. Data Collection → Fetch news data using API → raw_data.csv  
2. Data Processing → Clean data → cleaned_data.csv  
3. Data Analysis → Remove stopwords, find frequency → analysis_results.csv  
4. Data Visualization → Create graph → trend_visualization.png  

---

## Installation

pip install -r requirements.txt

---

## Environment Setup

Create .env file:

NEWS_API_KEY=your_api_key_here

---

## Run Project

python task1_data_collection.py  
python task2_data_processing.py  
python task3_analysis.py  
python task4_visualization.py  

---

## Outputs

raw_data.csv  
cleaned_data.csv  
analysis_results.csv  
trend_visualization.png  

---

## Tech Used

Python, pandas, requests, matplotlib, nltk, dotenv  

---

## Author

Praveen Bala
