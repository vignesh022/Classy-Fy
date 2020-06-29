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

## Data Collection and Usage
### Accessing Spotify
Classy-Fy is primarily designed to work with user-created playlists, since playlists created by Spotify cannot be edited. To access a user's private Spotify data, authentication is required to faciliate Classy-Fy to work with their data. Since, Classy-Fy is designed to be deployed locally by a user, there are very limited privacy issues and concerns. The authentication issued is also temporary and ceases to exist once the user has exited the application.

Classy-Fy has been built fully in Python and uses Spotipy which is a lightweight Python library for the Spotify Web API. A complete guide and documentation about using Spotipy can be found [here](https://spotipy.readthedocs.io/en/2.12.0/#). The Spotify Web API is really powerful and allows for multitube of user related operations, read more about it [here](https://developer.spotify.com/documentation/web-api/).

To work with the Spotify Web API, a CLIENT_ID and CLIENT_SECRET are required. Both of these keys are highly valuable and should not be shared with other users under any circumstances else your account could be compromised.

### Obtaining Client Credentials
To get started with the process of obtaining the CLIENT_ID and CLIENT_SECRET keys, head to the Spotify for Developers section. You can navigate to it from [here](https://developer.spotify.com/dashboard/). Login with your Spotify credentials, once you are logged in to your account you should be greeted by this.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/spotify_dashboard.png?raw=true)

On the newly opened page, create a new app through the "My New App" option, which should open a pop-box asking for a name for your app and a description. You can name this app "Classy-Fy" and in the description section you can enter anything you desire, for convenience you can simply type "A Personalized Playlist Filter". Also make sure to check both boxes accepting the terms and conditions put forth by Spotify. If done correctly you should be at this stage.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/spotify_classyfy.png?raw=true)

Click "CREATE" and congratulations you now have your own personal Spotify based app!!. You should automatically be directed to a new page with a black background.

You sh
## Running Classy-Fy on your local machine
Classy-Fy uses Streamlit which is a really great open source library for building custom web-apps. You can learn about how awesome and easy to use Streamlit is [here](https://docs.streamlit.io/en/stable/)

Streamlit requires a version of Python 3.6 or later. If you need the latest version of Python for your local machine, you can grab it from [here](https://www.anaconda.com/products/individual) 

Once you've downloaded and installed the latest version of Python or have ensured that your version of Python is >= 3.6. You can clone this repository and/or download the various files included to run Classy-Fy 

Install the libraries needed to run Classy-Fy by opening up a new terminal window from within the Anaconda Navigator and simply running the following:
```
pip install -r requirements.txt
```


Now, to load up and run Classy-Fy, run the following command:
```
streamlit run streamlit_kmeans.py
```
To terminate the process in your terminal press Ctrl+C (You have to do this each time you wish to run the process anew from the terminal).

