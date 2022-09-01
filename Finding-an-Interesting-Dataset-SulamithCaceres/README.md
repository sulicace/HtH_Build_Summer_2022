# Why are you interested in this data set?
I'm interested in learning more about the qualities and factors that contribute to a song's likeliness into becoming a Spotify Hit. As a Spotify user and music enjoyer, I was interested in knowing the differences between each of the songs labeled as Spotify Hits, whether it be its tempo, loudness, year, and more!

---
For this analysis, I will be using the csv file "Top Hits Spotify from 2000-2019" by Mark Koverha from [this kaggle link](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019?resource=download). "This dataset contains audio statistics of the top 2000 tracks on Spotify from 2000-2019. The data contains about 18 columns each describing the track and it's qualities."

# What are 10 (or more) questions that you hope to answerthrough your data analysis?

No. | Question
:-:|:-
1 | Out of the Spotify Top Hits, are there more explicit songs or non-explicit songs?
2 | What is the percentage of explicit songs in 1999? 
3 | What is the percentage of explicit songs in 2019?
4 | Are explicit songs considered more popular than non-explicit songs throughout the years?
5 | Which genres consist of higher numbers of Spotify Top Hits?
6 | What is the average energy level of a Spotify Top Hit per year?
7 | What is the average length of a Spotify Top Hit per year?
8 | What is the average tempo rate of a Spotify Top Hit per year?
9 | Which artists have the most Spotify Top Hits?
10 | How many artists have the least amount of Spotify Top Hits?

# Machine Learning Model: Logistic Regression
I planned on using a machine learning model to answer one of my biggest questions: how do these song features affect their outcomes, specifically, can a machine determine how likely a song is to be explicit or not explicit?
I used a Logistic Regression model to determine how many songs would the computer predict to be explicit or not explicit with the songs features. For this model, I used the following variables/features: popularity, danceability, mode, and energy
