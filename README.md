<p align="center">
  <img width="300" height="300" src="https://i.imgur.com/ojKHKY4.png">
</p>

# Classy-Fy 

## A user-personalized playlist filter for new and emerging music on Spotify

The average length of a song is ~ 4 minutes, to organize and sort a mere 15 songs into your playlists could take a whole hour if you thoroughly listen to them and gauge their fit. When dealing with more than 50+ songs, the time investment is substantial. Can this process be automated while simultaneously ensuring songs are matched accurately with the best fitting playlist?

Introducing, Classy-Fy an application for the active Spotify user/subscriber to help them quickly and efficiently organize their music into their library playlists. It functions by developing an understanding of a given user's taste in music and takes an entirely unbiased approach when assigning playlist labels to songs.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/classyfy_example.png?raw=true)

The methods utilized in the design and development of Classy-Fy can be extended and applied to understand and predict user/consumer behavior in the product analytics sector.

# Motivation

Music Streaming has seen a sharp increase in growth across all facets of the operation, mainly revenue and subscriber growth. The number of paid subscribers in the US alone for 2019 was at an all-time high of 60.4 million subscribers, according to the RIAA (Recording Industry Association of America).

<p align="center">
  <img width="496" height="387" src="https://github.com/vignesh022/Classy-Fy/blob/master/Images/usa_paid_subscribers.png?raw=true">
</p>

### Defining the problem

Regular users of Spotify's platform often curate and build their playlists, adjusting it to their unique tastes and for different situations. For example, my taste in music is relatively broad, and I maintain a dedicated playlist for the different types of music I listen to, as illustrated below.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/spotify_playlist_example.png?raw=true)

### Conceptualizing a potential solution

Classy-Fy is a tool designed to organize new and upcoming music into user-created playlists quickly. I developed Classy-Fy along the lines of being a proof-of-concept for a feature/add-on on Spotify in the future to help subscribers quickly sort new music into their libraries.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/classyfy_ex.png?raw=true)

Classy-Fy currently functions as a locally deployable script, which facilitates users to log in to their Spotify accounts, authorize access to their private playlist data, and allow for label assignment. Users of Classy-Fy can submit a single song to be assigned a playlist label or a playlist of songs.

# Running Python and Streamlit on your machine

Classy-Fy is built using Streamlit, which is a really great open source library for building custom web-apps. You can learn about how awesome and easy to use Streamlit is [here](https://docs.streamlit.io/en/stable/)

Streamlit requires a version of Python 3.6 or later. If you need the latest version of Python for your local machine, you can grab it from [here](https://www.anaconda.com/products/individual) 

Once you've downloaded and installed the latest version of Python or have ensured that your version of Python is >= 3.6. You can clone this repository and/or download the various files included to get ready to run Classy-Fy. 

Install the required libraries needed to run Classy-Fy by creating and activating a new python environment and simply running the following:
```
pip install -r requirements.txt
```

# Creating a Spotify Application to access User Data

I designed Classy-Fy to primarily work with user-created playlists since editing playlists created by Spotify is not possible. Access to a user's private Spotify data requires authentication. Classy-Fy can be deployed locally by a user, and there are no privacy issues and concerns. The authentication issued is also temporary and ceases to exist once the user has exited the application.

### Accessing Spotify

Classy-Fy has been built fully in Python and uses Spotipy, a lightweight Python library for the Spotify Web API. A complete guide and documentation about using Spotipy can be found [here](https://spotipy.readthedocs.io/en/2.12.0/#). The Spotify Web API is powerful and allows for several user-related operations, read more about it [here](https://developer.spotify.com/documentation/web-api/).

To work with the Spotify Web API, a CLIENT_ID and CLIENT_SECRET are required. Both of these keys are highly valuable and should not be shared with other users under any circumstances else your account could be compromised.

### Obtaining Client Credentials

To get started with the process of obtaining the CLIENT_ID and CLIENT_SECRET keys, head to the Spotify for Developers section. You can navigate to it from [here](https://developer.spotify.com/dashboard/). Login with your Spotify credentials, once you are logged in to your account you should be greeted by this.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/spotify_dashboard.png?raw=true)

On the newly opened page, create a new app through the "My New App" option, which should open a pop-box asking for a name for your app and a description. You can name this app "Classy-Fy" and in the description section you can enter anything you desire, for convenience you can simply type "A Personalized Playlist Filter". Also make sure to check both boxes accepting the terms and conditions put forth by Spotify. If done correctly you should be at this stage.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/spotify_classyfy.png?raw=true)

Click "CREATE" and congratulations you now have your own personal Spotify based app!!. You should automatically be directed to a new page with a black background.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/spotify_credentials.png?raw=true)

You can view your CLIENT_SECRET and CLIENT_ID on the above page. Make a note of both as you will need them to run the scripts to allow for user authentication with the Spotify Web API.

### Whitelisting the callback from Classy-Fy

When performing user-authentication using the Spotify Web API, the process requires a valid redirect URI and for the URI to be whitelisted by the app so that it is not flagged as suspicious and invasive.

On the same page where you viewed your Spotify CLIENT_ID and CLIENT-SECRET, there should an "EDIT SETTINGS" button on the top right. Click on it and you should see a pop-box with your app name, description, Website, etc. The 4th option is Redirect URIs, paste the following in the section "http://localhost:8888/callback/" (without quotes) and click "ADD". Click "SAVE" at the bottom else you will have to repeat the process all over again to add the URI.

If you plan to run the Jupyter Notebooks in this repository, make sure to add "http://localhost:8501/" as another Redirect URI to the application else you might encounter login issues.

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/spotify_redirectURI.png?raw=true)

### Entering Client Credentials in Classy-Fy Script

Once you've gotten your CLIENT_ID, CLIENT_SECRET, and set your redirect URIs, you can head over to the "streamlit_kmeans.py" file and enter your details into the file.
Set the value of your CLIENT_ID to the variable "cid" and your CLIENT_SECRET to the "secret" variable. Ensure your keys are wrapped in quotes as they are interpreted as strings by the Spotipy package.

Now, to load up and run Classy-Fy, run the following command:
```
streamlit run streamlit_kmeans.py
```
You should be automatically taken to a new tab in your web browser and greeted with the Classy-Fy layout. Simply enter the required details and you're ready to use Classy-Fy.

# Data Processing, Modeling, and Validation

Classy-Fy functions off the data extracted from a given user's song library. The Spotify Web API provides a dense variety of information regarding the songs, albums, playlists, and artists. To organize and match songs with the best fitting playlist, I utilized the audio features provided by Spotify for each song.

### Feature Selection
Spotify provides 18 [audio features](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) for every song in their database. Among these 18, only 13 are numerical and can be used to differentiate between songs of varying styles and genres. Following a detailed exploration of the 13 quantitative features, I decided to drop two features that displayed very low variability of values across the whole database.

### Modeling and Validation
The process of assigning playlist labels to songs using Classy-Fy is an unsupervised classification problem. I realized that the user-created playlists do not always adhere to the same level of specification that Spotify uses when curating their playlists. The unsupervised approach used also made validating my algorithmic approach a challenging task as there were no labels to use as a ground truth.

I selected 3 ML-based classification/clustering approaches and used them to accomplish the label assignment, namely, K-Nearest Neighbors (KNN), a Modified K-Means approach, and Random Forests. All three algorithms I used were deployed on the same training and validation dataset to contrast their performance against each other and select the best approach. The table below shows the validation accuracy achieved by each algorithm:

| Classification Approach | Validation Accuracy |
|-------------------------|---------------------|
| K-Nearest Neighbors | 48% |
| Modified K-Means | 66% |
| Random Forests | 69% |

I selected the Modified K-Means as our final choice since it presented significantly higher accuracy to K-Nearest Neighbors, and was comparable in performance with the Random Forest model. The Modified K-Means model is also superior to the Random Forest model in terms of interpretability and explainability.

The traditional K-Means approach of partitioning the songs into clusters and evaluating similarity at every stage followed by reorganization would destroy the user-created playlists. Instead, I treated each user-created playlist as an individual cluster; these distinct clusters contain songs that have been curated by the user. The playlists each possess a unique audio predictors vector, which is the mean of the audio features of their constituent songs. I utilized these individual audio vectors to determine the Euclidean distance between the predictors of a song submitted for labeling and the multiple clusters. Following the computation of the Euclidean distances, I assigned the label of the "nearest" playlist to the song.

To validate the above approach, I used a two-pronged approach for all 3 of the classification methods mentioned above.

  * Firstly, I selected a random subset of Spotify music genres from their 45+ available kinds and proceeded to extract all the available playlists for those chosen genres. This comprehensive selection of songs is a labeled dataset, and I had labels to associate each song to its source playlist in the Spotify database. I proceeded to split this selection into a 75/25 training and validation dataset and deployed all three classification methods to gain a measure of the accuracy of the label assignment.
  
  * Secondly, I used the user-created playlists for a given user. This step involved using only those songs which were part of the playlists that matched our selection criteria. I split this selection into a 75/25 training and validation dataset and deployed all three classification methods to gain a measure of the accuracy of the label assignment. This step is unique to each user since the assumption is that no two users have exactly the same choice of songs when it comes to curating music for their playlists.
  
The overall dataflow for Classy-Fy can be summarized as:

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/Data_flow.png?raw=true)

# Visualizing the difference between playlists

Let's take a quick peek at the results Classy-Fy provides for a given user-submitted list:

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/classyfy_results.png?raw=true)

Classy-Fy assigns labels to the submitted songs and allows for a quick organization of any new music you're keen to listen to. The polar/radar chart allows the user to view and compare in detail which features vary between the different playlists.

To further illustrate how effective Classy-Fy is at its purpose, let me show you an example polar chart for a 2 playlist validation case:

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/party_vs_focus.png?raw=true)

The above chart compares the features for music coming from 2 distinctly different playlists named "Party" and "Focus". "Party" essentially is a collection of music that you might listen to at a club or when you looking to have a fun time, whereas "Focus" is a playlist of music that is curated to help listeners focus while they're studying, working from home, and/or any activity that needs concentration.

"Party" songs measure higher on "danceability", "valence", "energy" compared to "Focus" songs which are predominantly high on "instrumentalness" and "acousticness". This example achieved a 91% accuracy of label assignment.

Another example I want to showcase is a 5 playlist validation example:

![](https://github.com/vignesh022/Classy-Fy/blob/master/Images/5_playlist_validation.png?raw=true)

I achieved a 70% accuracy of label assignment for this case.

# Caveats & Improvements

The main driving force behind designing Classy-Fy stemmed from my own experience organizing my music library as I migrated across platforms in the past. Having a tool like Classy-Fy back in the day would have facilitated a smoother transition. That being said, Classy-Fy is primarily purposed to advise a user on the best matching playlist label for a given song. If users disagree with the playlist assignment by Classy-Fy for particular songs and proceed to reassign the playlists manually, they are providing new information for Classy-Fy to learn and improve on its previous iteration. This process assists Classy-Fy in improving its accuracy the more you use it.

Improvements to the accuracy can be addressed by engineering new features to help facilitate better separation between playlists of a similar vibe/sound. All predictors I have utilized to this point are quantitative; my model can benefit from the inclusion of categorical variables that assist in differentiating tracks similar to each other on a feature basis. Another valuable avenue to explore is the inclusion of audio signal processing data to develop a more robust model that incorporates all aspects of a given song and utilizing a different clustering algorithm like DBSCAN or Gaussian Mixture Modeling and comparing to see if it improves on the original choice of approach.
