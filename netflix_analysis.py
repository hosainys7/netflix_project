# %%

#"""
#Netflix Data Analysis

#Exploratory data analysis (EDA) on Netflix content:
#- Rating distribution
#- Top directors and actors
#- Content trends over years
#- Sentiment analysis
#- Top actors in USA, UK, France

#Python libraries used: Pandas, Plotly, TextBlob, NumPy

import numpy as np #for linear algebra
import pandas as pd #for data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px #for interactive data visualization
from textblob import TextBlob #for text processing and sentiment analysis
import re #for regular expressions

# Load the dataset
dff= pd.read_csv('data/netflix_titles.csv')

dff.head() # Display the first few rows of the dataset

# %%
dff.shape # Check the shape of the dataset (number of rows and columns)

# %%
dff.columns # Check the column names in the dataset

# %%
z = dff.groupby(['rating']).size().reset_index(name='counts') # Group the dataset by 'rating' and count the occurrences of each rating
piechart = px.pie(z, values='counts', names='rating', title='Distribution of Ratings on Netflix', color_discrete_sequence=px.colors.qualitative.Set3) # Create a pie chart to visualize the distribution of ratings
piechart.show() # Display the pie chart

# %%
dff['director'] = dff['director'].fillna('No director specified') # Fill missing values in the 'director' column with 'No director specified'
filtered_directors = pd.DataFrame() # Create an empty DataFrame to store the filtered directors
filtered_directors = dff['director'].str.split(',', expand=True).stack() # Split the 'director' column by comma and stack the resulting columns into a single Series
filtered_directors= filtered_directors.to_frame() # Convert the Series to a DataFrame
filtered_directors.columns = ['Director'] # Rename the column to 'director'
directors = filtered_directors.groupby(['Director']).size().reset_index(name='Total Content') # Group the DataFrame by 'director' and count the occurrences of each director
directors = directors[directors.Director != 'No director specified'] # Filter out the rows where the director is 'No director specified'
directors = directors.sort_values(by='Total Content', ascending=False)
directorstop5 = directors.head(5) # Get the top 5 directors based on the total content
directorstop5 = directorstop5.sort_values(by=['Total Content']) # Sort the top 5 directors by total content in ascending order
fig1 = px.bar(directorstop5, x= 'Total Content', y='Director', title='Top 5 Directors with the Most Content on Netflix')
fig1.show() # Display the bar chart of the top 5 directors with the most content on Netflix

# %%
dff['cast'] = dff['cast'].fillna('No cast specified') # Fill missing values in the 'cast' column with 'No cast specified'
filtered_cast = pd.DataFrame() # Create an empty DataFrame to store the filtered cast members
filtered_cast = dff['cast'].str.split(',', expand=True).stack() # Split the 'cast' column by comma and stack the resulting columns into a single Series
filtered_cast = filtered_cast.to_frame() # Convert the Series to a DataFrame
filtered_cast.columns = ['Actor'] # Rename the column to 'cast'
actors = filtered_cast.groupby(['Actor']).size().reset_index(name='Total Content') # Group the DataFrame by 'cast' and count the occurrences of each cast member
actors = actors[actors.Actor != 'No cast specified'] # Filter out the rows where the cast member is 'No cast specified'
actors = actors.sort_values(by=['Total Content'], ascending=False) # Sort the actors by total content in descending order
actorstop5 = actors.head(5)
actorstop5 = actorstop5.sort_values(by=['Total Content']) # Sort the top 5 actors by total content in ascending order
fig2 = px.bar(actorstop5, x='Total Content', y='Actor', title='Top 5 Actors with the Most Conten on Netflix')
fig2.show() # Display the bar chart of the top 5 actors with the most content on Netflix

# %%
df1 = dff[['type', 'release_year']] # Select the 'type' and 'release_year' columns from the dataset
df1 = df1.rename(columns={'release_year': 'Release Year'}) # Rename the columns for better readability
df2 = df1.groupby(['Release Year','type']).size().reset_index(name='Total Content') # Group the DataFrame by 'release_year' and 'type', and count the occurrences of each combination
df2 = df2[df2['Release Year'] >= 2010 ] # Filter the DataFrame to include only rows where the release year is greater than or equal to 2010
fig3 = px.line(df2, x="Release Year", y="Total Content", color='type', title= 'Trend of Content') 
fig3.show() # Display the line chart showing the trend of content on Netflix over the years

# %%
dfx = dff[['release_year', 'description']].copy()
dfx = dfx.rename(columns={'release_year': 'Release Year'})

dfx['polarity'] = dfx['description'].apply(lambda text: TextBlob(str(text)).sentiment.polarity)

def get_sentiment(p):
    if p > 0.1:
        return 'Positive'
    elif p < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

dfx['Sentiment'] = dfx['polarity'].apply(get_sentiment)

sentiment_counts = (
    dfx[dfx['Release Year'] >= 2010]
    .groupby(['Release Year', 'Sentiment'])
    .size()
    .reset_index(name='Total Content')
)

fig4 = px.bar(
    sentiment_counts,
    x='Release Year',
    y='Total Content',
    color='Sentiment',
    title='Sentiment Analysis of Netflix Content Over the Years'
)

fig4.show()


# %%
actors_country = dff[['title', 'cast', 'country']].copy() # Select the 'title', 'cast', and 'country' columns from the dataset
actors_country['country'] = actors_country['country'].fillna('No country specified') # Fill missing values in the 'country' column with 'No country specified'
actors_country['cast'] = actors_country['cast'].fillna('No cast specified') # Fill missing values in the 'cast' column with 'No cast specified'
actors_country['country'] = actors_country['country'].str.split(',')
actors_country = actors_country.explode('country') # Explode the 'country' column to create a new row for each country
actors_country['country'] = actors_country['country'].str.strip() # Remove leading and trailing whitespace from the 'country' column
actors_country["cast"] = actors_country["cast"].str.split(",")
actors_country = actors_country.explode("cast")
actors_country["cast"] = actors_country["cast"].str.strip()


# %%
actors_country = actors_country[
    (actors_country["cast"] != "No cast specified") &
    (actors_country["country"] != "No Country Specified")
]

# %%
actor_counts = (
    actors_country
    .groupby(["country", "cast"])
    .size()
    .reset_index(name="Total Content")
)
actor_counts.head()

# %%
selected_countries = ["United States", "United Kingdom", "France"]

filtered = actors_country[
    actors_country["country"].isin(selected_countries)
]

# %%
filtered["country"].unique()

# %%
top_actors_by_country = (actor_counts.sort_values(
    ["country","Total Content"], ascending=[True, False]
    )
.groupby("country")
.head(5)
)

# %%
# Only visualize the top 5 actors in UK, USA, and France


selected_countries = ['United States', 'United Kingdom', 'France']
top_actors_selected = top_actors_by_country[top_actors_by_country['country'].isin(selected_countries)]

# Pie chart for each of the 3 countries
for country in selected_countries:
    df_country = top_actors_selected[top_actors_selected['country'] == country]
    fig = px.bar(
        df_country,
        x= 'Total Content',
        y='cast',
        title=f'Top 5 Actors in {country}',
    )
    fig.show()



