# Netflix Data Analysis

## Overview

This project explores Netflix content using Exploratory Data Analysis (EDA), data visualization, and sentiment analysis techniques in Python. The analysis aims to understand Netflix’s content distribution, identify recurring trends among actors and directors, analyze content growth over time, and examine sentiment patterns in content descriptions.

An additional country-based analysis was performed to identify the top actors in the United States, United Kingdom, and France.

---

# Objectives

The objectives of this analysis are:

* Understand the type of content available on Netflix
* Explore similarities and patterns in Netflix content
* Identify what Netflix focuses on in terms of ratings and content type
* Perform sentiment analysis on Netflix content descriptions
* Analyze the top actors in the USA, UK, and France

---

# Dataset

The dataset contains Netflix titles information including:

* Title
* Type (Movie / TV Show)
* Director
* Cast
* Country
* Release Year
* Rating
* Description

The dataset was analyzed using Python and Pandas.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Plotly Express
* TextBlob
* Regular Expressions (re)
* Jupyter Notebook
* VS Code

---

# Analysis Performed

## 1. Rating Distribution Analysis

* Analyzed the distribution of Netflix content ratings using pie charts.
* Identified dominant audience categories such as TV-MA and TV-14.

## 2. Top Directors Analysis

* Identified directors with the highest number of Netflix titles.

## 3. Top Actors Analysis

* Analyzed actors with the highest number of appearances on Netflix.

## 4. Content Trend Analysis

* Explored Netflix content growth over time from 2010 onwards.
* Compared Movies and TV Shows trends.

## 5. Sentiment Analysis

* Performed sentiment analysis on Netflix descriptions using TextBlob.
* Classified descriptions into Positive, Neutral, and Negative sentiment categories.

## 6. Country-Based Actor Analysis

* Filtered content from:

  * United States
  * United Kingdom
  * France
* Identified the top 10 actors in each country.
* Visualized actor distribution using bar charts.

---

# Key Findings

* Netflix primarily focuses on mature audience content.
* Content production increased significantly after 2010.
* TV Shows experienced rapid growth over recent years.
* Most Netflix descriptions have neutral or positive sentiment.
* The United States contains the largest concentration of recurring actors.
* Certain directors and actors appear repeatedly across Netflix content.

---

# Project Structure

```text
netflix-data-analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── visualizations/
│   ├── rating_distribution.png
│   ├── top_directors.png
│   ├── top_actors.png
│   ├── content_trend.png
│   ├── sentiment_analysis.png
│   └── country_actor_analysis.png
│
├── netflix_analysis.ipynb
├── netflix_analysis.py
├── report.pdf
└── README.md
```

---

# Visualizations

## Rating Distribution

![Rating Distribution](visualizations/rating_distribution.png)

## Top Directors

![Top Directors](visualizations/top_directors.png)

## Top Actors

![Top Actors](visualizations/top_actors.png)

## Content Trends

![Content Trends](visualizations/content_trend.png)

## Sentiment Analysis

![Sentiment Analysis](visualizations/sentiment_analysis.png)

---

# Future Improvements

Possible extensions of this project include:

* Genre analysis
* Country-level content comparison
* Recommendation systems
* Advanced NLP analysis
* Interactive dashboards using Streamlit or Dash

---

# Author

Hosainy Eltayeb

GitHub: @b-shadow7
