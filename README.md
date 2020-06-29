<p align="center">
  <img width="300" height="300" src="https://i.imgur.com/ojKHKY4.png">
</p>

# Classy-Fy

### A Personalized Playlist Filter for Spotify Music

## Background and Motivation
Music Streaming has seen a sharp increase in growth across all facets of operation particularly revenue and subscriber growth. The number of paid subscribers in the US alone for 2019 was at all time high of 60.4 million subscribers according to the RIAA (Recording Industry Association of America).[[1]](https://techcrunch.com/2020/02/26/streaming-services-accounted-for-nearly-80-of-all-music-revenue-in-2019/)

Spotify who are one of the worldwide leaders in the music streaming industry boast upwards of 280 million active monthly users on their platform of which 130 million are "Premium" subscribers.[[2]](https://newsroom.spotify.com/company-info/). Spotify does a great job of recommending music to their subscribers based off their listening tastes, the artists they are partial to, and the genre of music. They also house a multitude of playlists spanning more than 45+ broad musical genres. 

Regular users of Spotify's platform often curate and build their own playlists adjusting it to their unique tastes and for different situations. For example, a given user might have a dedicated playlist for when are working/focusing on their jobs, a separate playlist for when they hit the gym, and similarly a new playlist for a different activity. 

Spotify currently does not assign new music to a user playlists, the process of assigning songs to your playlists still needs to be done manually. Assuming an average length of 4 minutes per song, to simply organize and sort a mere 15 songs into your playlists takes a whole hour if you fully listen to them and gauge their fit. When dealing with more than 50+ songs the time investment is substantial. Can this process be automated while simultaneously ensuring songs are matched accurately with the best fitting playlist?

Introducing Classy-Fy, a tool for users to quickly organize new and upcoming music into their respective playlists. Classy-Fy has been designed along the lines of being a proof-of-concept for a feature/add-on on Spotify in future to help their premium subscribers quickly sort new music in their libraries. Classy-Fy currently functions as a locally deployable script which facilitates users to login into their Spotify accounts, authorize Classy-Fy access to their personal playlist data, and allow for label assignment. Users of Classy-Fy can submit either a single track/song to be assigned a playlist label or a brand new playlist altogther.

## Requirements to run Classy-Fy on your local machine
Import Streamlit using:
```python3
import streamlit as st```
