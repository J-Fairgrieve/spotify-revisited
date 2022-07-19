# Spotify Revisited

James Fairgrieve

Linkedin: [https://www.linkedin.com/in/jfairgrieve/](https://www.linkedin.com/in/jfairgrieve/)

## Contents
 - About the Project
 - Resources
 - Findings
 - Conclusion
 - Acknowledgements

## About the Project
Spotify is one of the largest music streaming providers to date, founded in 2006 by Daniel Ek & Martin Lorentzon. There are over 422 million monthly active users, with around 182 million of those being paying subscribers.

Through the developer platform, you can access the audio features in order to further explore tracks, albums, artists & playlists within the platform. Some of these features include:

 - Mood: Danceability, Valence, Energy, Tempo
 - Properties: Loudness, Speechiness, Instrumentalness
 - Context: Liveness, Acousticness
 - Segments, Tatums, Bars, Beats, Pitches, Timbre etc.

Another powerful tool within the developer platform is the ability to create recommendations for listeners by utilising the above metrics with Spotify's own algorithms.

There are certain limitations to what can be extracted for analysis. For example, only 100 songs can be extracted at a time. The playlists must also be public (available to be viewed by everyone, not just the user running the reports). This project will analyse two playlists:

 - UK Top 50
 - UK Viral 50

Two playlists focusing on one localised area, both looking at popular songs but with varying results. The Top 50 playlist collates the most streamed songs on Spotify at the time. However, the Viral 50 playlist also takes the user interactions into account (sharing to blogs, social media for example). By delving deeper into these playlists using the developer platform we can analyse the type of songs that are top/viral & compare the shape of the two playlists.

Please note, the playlist data is accurate as of 01/07/2022

## Resources
 - Spotify for Developers
 - UK Top 50 Playlist
 - UK Viral 50 Playlist

## Findings

### Playlist Features

![Playlist Features](https://raw.githubusercontent.com/J-Fairgrieve/spotify-revisited/main/Images/Top%20and%20Viral%2050%20Feature%20Analysis.png "Top/Viral 50 Feature Analysis")

 - Both playlists have a high Danceability and Energy
 - Both playlists have a low Instrumentalness and Speechiness
 - The Top 50 playlist's highest scoring feature is Danceability
 - The Viral 50 playlist's highest scoring feature was energy

### Top 50 Playlist Analysis

![Top 50 Playlist Correlation Matrix](https://github.com/J-Fairgrieve/spotify-revisited/blob/main/Images/Top%2050%20Features%20Matrix.png?raw=true "Correlation Matrix")

Correlation amongst the Top 50 is relatively weak, apart from energy and acousticness with a strong negative correlation of -0.74

![Acousticness and Energy Scatter Plot](https://github.com/J-Fairgrieve/spotify-revisited/blob/main/Images/acousticness%20energy%20scatter%20plot.png?raw=true "Scatter Plot")

![Acousticness and Energy Box Plot](https://github.com/J-Fairgrieve/spotify-revisited/blob/main/Images/acousticness%20energy%20box%20plot.png?raw=true "Box Plot")

There are three outliers for acousticness:

| Artist        | Album             | Track             | Acousticness | Energy |
| ------------- | -------------     | ----------------- | ------------ | ------ |
| Joji          | Glimpse of Us     | Glimpse of Us     | 0.89         | 0.32   |
| Harry Styles  | Harry's House     | Matilda           | 0.90         | 0.29   |
| Billie Eilish | Happier Than Ever | Happier Than Ever | 0.77         | 0.23   |

There is one outlier for energy:

| Artist        | Album             | Track             | Acousticness | Energy |
| ------------- | -------------     | ----------------- | ------------ | ------ |
| Billie Eilish | Happier Than Ever | Happier Than Ever | 0.77         | 0.23   |

### Viral 50 Playlist Analysis

![Viral 50 Playlist Correlation Matrix](https://github.com/J-Fairgrieve/spotify-revisited/blob/main/Images/Viral%2050%20Features%20Matrix.png?raw=true "Correlation Matrix")

In contrast to the Top 50, the Viral 50 playlist has a mostly negative correlation. The only positive correlation is between Danceability and Valence (0.53).

![Danceability and Valence Scatter Plot](https://github.com/J-Fairgrieve/spotify-revisited/blob/main/Images/danceability%20valence%20scatter%20plot.png?raw=true "Scatter Plot")

![Danceability and Valence Box Plot](https://github.com/J-Fairgrieve/spotify-revisited/blob/main/Images/danceability%20valence%20box%20plot.png?raw=true "Box Plot")

There is one outlier for Danceability:

| Artist        | Album             | Track             | Acousticness | Energy |
| ------------- | -------------     | ----------------- | ------------ | ------ |
| Sleep Miracle | Brown Sleep Noise | Brown Sleep Noise | 0.06         | 0.06   |

## Acknowledgements
A special thanks to the original group who I worked alongside during the original project, we definitely learned a lot together! Please have a look at our original project [here](https://github.com/Amina-H1/spotify-project)