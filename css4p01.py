# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:15:02 2024

@author: ONISURU OLUWATAYO R
"""

import pandas as pd
file = pd.read_csv("C:/Users/Administrator/CSS_2024/CSS2024_Day1/movie_dataset.csv",index_col=0)
df=pd.DataFrame(file)
df.dropna(inplace=True)

#Movie with the highest Rating
highest_rating_movie = df.loc[df["Rating"].idxmax()]
print(highest_rating_movie)

#average Revenue of All movies in the Dataset
average_revenue = df["Revenue (Millions)"].mean()
print(f' The average revenue in Millions is ${average_revenue}')

#average revenue of movies from 2015 to 2017 
df_2015_2017 = df[(df['Year']>=2015) & (df['Year']<=2017)]

average_revenue = df_2015_2017["Revenue (Millions)"].mean()
print(f' The average revenue in Millions for movies from 2015 to 2017 is ${average_revenue}')

#How many movies were released in the year 2016?
count_2016 = (file["Year"] == 2016).sum()
print(f'the number of movies in 2016 is {count_2016}')


#How many movies were directed by Christopher Nolan?
count_nolan_movies = (file["Director"] == "Christopher Nolan").sum()
print(f'the number of movies Directed by Christopher Nolan: {count_nolan_movies}')

#How many movies in the dataset have a rating of at least 8.0?

count_8_rating = (file["Rating"] >= 8.0).sum()
print(f' the number of movies with at least 8.0 Rating {count_8_rating}')

#What is the median rating of movies directed by Christopher Nolan?
median_nolan_rating = file[file["Director"] == "Christopher Nolan"]["Rating"].median()
print(f' the median rating of movies directed by Chris Nolan is {median_nolan_rating}')


    
#Find the year with the highest average rating?
average_rating_by_year = file.groupby("Year")['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(year_highest_average_rating)

#What is the percentage increase in number of movies made between 2006 and 2016?
movies_count_2016 = len(file[file["Year"] == 2016])
movies_count_2006 = len(file[file["Year"] == 2006])
percentage_increase = ((movies_count_2016 - movies_count_2006) / movies_count_2006)*100

print(percentage_increase)

#Find the most common actor in all the movies?

#Note, the "Actors" column has multiple actors names. You must find a way to search for the most common actor in all the movies.
actors_file = file['Actors'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('Actor')
most_common_actor = actors_file['Actor'].mode().iloc[0]
print(f'Most common actor in all movies: {most_common_actor}')


#How many unique genres are there in the dataset?

#Note, the "Genre" column has multiple genres per movie. You must find a way to identify them individually.
movie_unique_Genre = file["Genre"].str.split(',').explode().str.strip()
num_unique_genre = movie_unique_Genre.nunique()
print(f'the number of unique genres is {num_unique_genre}')

#Do a correlation of the numerical features,
num_col_file = file._get_numeric_data().columns
correlation_matrix = file[num_col_file].corr()

# what insights can you deduce?
