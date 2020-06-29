import sys
import pandas as pd
import numpy as np
import spotipy
import spotipy.util as util
import streamlit as st

img_url = "https://pyxis.nymag.com/v1/imgs/2b7/b66/dc2752664adfba3b8523d73873c5bf8034-26-spotify.2x.rsocial.w600.jpg"
st.image(img_url)

st.title("CLASSY-FY")
st.write("Welcome to Classy-fy: A user-personalized playlist labeler")

sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
cid ='Enter your CLIENT_ID here'
secret ='Enter your CLIENT_SECRET here'
redirect_uri='http://localhost:8888/callback/'
#redirect_uri='http://127.0.0.1:8501'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
#sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#sp.trace=False
scope = 'user-library-read playlist-read-private'

user_name = st.text_input("Please enter you Spotify username")
st.write("You can fetch your username by checking your account details on https://www.spotify.com/us/account/overview/")

uri_list = st.text_input("Please enter the URI of the Spotify song/playlist you want sorted")

if(user_name):

    if(st.button('Click here to login into your Spotify account')):
        #
        token = util.prompt_for_user_token(user_name, scope,client_id=cid, client_secret=secret, redirect_uri=redirect_uri)
        #user_songs = pd.read_csv("user_songs.csv")

        if token:
            sp = spotipy.Spotify(auth=token)
            current_user = sp.current_user()
            username = current_user["display_name"]
            playlists = sp.user_playlists(username)
            playlist_uris = []
            playlist_labels = {}
            count=0
            for playlist in playlists['items']:
                pl_name = playlist['name']
                playlist_uris.append(playlist["id"])
                playlist_labels[pl_name] = count
                print("Playlist name: {}".format(pl_name))
                count+=1
        else:
            print("Can't get token for", username)

        def songs_database(playlist_uris):
            songs_df = pd.DataFrame()
            for uri in playlist_uris:
                playlist = sp.user_playlist("spotify",uri)
                songs = playlist["tracks"]["items"]
                ids = []
                song_names = []
                song_artist = []

                for i in range(len(songs)):
                    ids.append(songs[i]["track"]["id"])
                    song_names.append(songs[i]["track"]["name"])
                    song_artist.append(songs[i]["track"]["artists"][0]['name'])
                features = sp.audio_features(ids)
                df1 = pd.DataFrame()
                for each in features:
                    if(each != None):
                        d = pd.DataFrame(each,index=[0])
                    df1 = df1.append(d,ignore_index=True)
                df2 = pd.DataFrame()
                df2["track_title"] = song_names
                df2["track_artist"] = song_artist
                df2["playlist_name"] = playlist["name"]
                df3 = pd.concat([df2,df1], axis=1)

                if songs_df.empty:
                    songs_df = df3
                else:
                    songs_df = pd.concat([songs_df,df3],axis=0,ignore_index=True)

            return songs_df

        user_songs = songs_database(playlist_uris)
        user_songs["label_id"] = user_songs["playlist_name"].map(playlist_labels)

        user_songs.to_csv("user_songs.csv",index=False,header=True)

        ## KNN ##
        # Import train_test_split function
        from sklearn.model_selection import train_test_split

        #user_songs = user_songs.sample(frac=1).reset_index(drop=True)
        train_cols = ['danceability','energy', 'key', 'loudness', 'speechiness', 'acousticness',
                      'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
        target_cols = "label_id"
        features = user_songs[train_cols]
        target = user_songs[target_cols]

        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        features_scaled = scaler.fit_transform(features)

        # Split dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=1)

        #Import scikit-learn metrics module for accuracy calculation
        from sklearn import metrics
        # Model Accuracy, how often is the classifier correct?
        #print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

        ## Modified K-Means ##
        def cluster_centroids(X):
            return((X.mean()))

        playlist_clusters = {}
        features = user_songs.sample(frac=1).reset_index(drop=True)
        train_cols = ['danceability','energy', 'key', 'loudness', 'speechiness', 'acousticness',
                      'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
        target_cols = "label_id"
        result_cols = ["track_title","track_artist"]
        target = features[target_cols]

        # Split dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=1)
        y_test = y_test.reset_index(drop=True)

        for each in playlist_labels:
            temp = pd.DataFrame()
            temp = X_train[X_train["playlist_name"] == each]
            temp2 = pd.DataFrame(scaler.fit_transform(temp[train_cols]))
            playlist_clusters[each] = cluster_centroids(temp2)

        playlist_clusters = pd.DataFrame.from_dict(playlist_clusters, orient='index')

        X_test_scaled = pd.DataFrame(scaler.fit_transform(X_test[train_cols]))

        def distances(X):
            X = np.array(X)
            df = pd.DataFrame(index=playlist_clusters.index.copy())
            for index,each in playlist_clusters.iterrows():
                Y = np.array(each)
                distance = np.linalg.norm(X - Y)
                df.loc[index,"distance"] = distance
            return (df.idxmin(axis = 0)[0])

        predictions = []

        for index,song in X_test_scaled.iterrows():
            predictions.append(distances(song))

        predictions = pd.Series(predictions)
        predictions = predictions.rename("assigned_playlist")
        y_pred = predictions.map(playlist_labels)

        count=0
        for i in range(len(y_pred)):
            if(y_pred[i] == y_test[i]):
                count+=1
        acc = count/len(y_pred)
        st.write("Validation Accuracy: ",acc)

        X_final = X_test[result_cols]
        X_final = X_final.reset_index(drop=True)
        songs_result = pd.concat([X_final,predictions],axis=1,)
        st.write("Here are the songs from the playlist you uploaded to be classyfied:")
        st.write("  ")
        st.write(songs_result)

        from math import pi
        import matplotlib.pyplot as plt
        #%matplotlib inline

        playlist_clusters.columns = train_cols
        polarplot = playlist_clusters.to_dict("index")

        N = len(train_cols)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        fig = plt.figure(figsize=(8,8))
        ax = plt.subplot(111, polar=True)
        ax.set_theta_offset(pi)
        ax.set_theta_direction(1)

        #ax.spines["polar"].set_visible(False)

        plt.xticks(angles, train_cols)

        ax.set_rlabel_position(-180)
        plt.yticks([0, 0.5, 1], ["0", "0.5","1"], color="grey", size=7)
        plt.ylim(0, 1)

        # Ind1
        for i, key in enumerate(polarplot.keys()):
            if i <len(polarplot):
                values=list(playlist_clusters.iloc[i])
                print(values)
                values += values[:1]
                ax.plot(angles, values, linewidth=1, linestyle='solid', label=key)

        # Add legend
        plt.legend(bbox_to_anchor=(0.1, 0.1))
        st.pyplot()

# Removing access token once all operations are completed and user is required to login again
    import os
    filename = ".cache-%s" % user_name
    #print(filename)
    if os.path.exists(filename):
        os.remove(filename)
        #print("file removed")
