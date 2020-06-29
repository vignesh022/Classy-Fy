<p align="center">
  <img width="300" height="300" src="https://i.imgur.com/ojKHKY4.png">
</p>

# Classy-Fy

### A Personalized Playlist Filter for Spotify Music

## Background and Motivation
Music Streaming has seen a sharp increase in growth across all facets of operation particularly revenue and subscriber growth. The number of paid subscribers in the US alone for 2019 was at all time high of 60.4 million subscribers according to the RIAA (Recording Industry Association of America).[[1]](https://techcrunch.com/2020/02/26/streaming-services-accounted-for-nearly-80-of-all-music-revenue-in-2019/)

Regular users of Spotify's platform often curate and build their own playlists adjusting it to their unique tastes and for different situations. For example, a given user might have a dedicated playlist for when are working/focusing on their jobs, a separate playlist for when they hit the gym, and similarly a new playlist for a different activity. 

Spotify currently does not assign new music to a user playlists, the process of assigning songs to your playlists still needs to be done manually. Assuming an average length of 4 minutes per song, to simply organize and sort a mere 15 songs into your playlists takes a whole hour if you fully listen to them and gauge their fit. When dealing with more than 50+ songs the time investment is substantial. Can this process be automated while simultaneously ensuring songs are matched accurately with the best fitting playlist?

Introducing Classy-Fy, a tool for users to quickly organize new and upcoming music into their respective playlists. Classy-Fy has been designed along the lines of being a proof-of-concept for a feature/add-on on Spotify in future to help their premium subscribers quickly sort new music in their libraries. Classy-Fy currently functions as a locally deployable script which facilitates users to login into their Spotify accounts, authorize Classy-Fy access to their personal playlist data, and allow for label assignment. Users of Classy-Fy can submit either a single track/song to be assigned a playlist label or a brand new playlist altogther.

## Requirements to run Classy-Fy on your local machine
Classy-Fy uses Streamlit which is a really great open source library for building custom web-apps. You can learn about how awesome and easy to use Streamlit is [here](https://docs.streamlit.io/en/stable/)

Streamlit requires a version of Python 3.6 or later. If you need the latest version of Python for your local machine, you can grab it from [here](https://www.anaconda.com/products/individual) 

Once you've downloaded and installed the latest version of Python or have ensured that your version of Python is >= 3.6. You can clone this repository and/or download the various files included to run Classy-Fy 

Install the libraries needed to run Classy-Fy by opening up a new terminal window from within the Anaconda Navigator and simply running the following:
```
pip install -r requirements.txt
```
Once all the requisite packages have been installed, you can run the following in your terminal window to test if Streamlit installed correctly:
```
streamlit hello
```
If yes, you should automatically be directed to a new page with a message saying "Welcome to Streamlit". The page should look like this [here](https://imgur.com/pxYtk1e)

Now, to load up and run Classy-Fy, run the following command:
```
streamlit run streamlit_kmeans.py
```
