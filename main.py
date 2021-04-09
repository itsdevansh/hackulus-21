from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tkinter import *
import tkinter as tk
import webbrowser
from _ast import Lambda

def open_spotify(url):
    webbrowser.open(url, new = 2)
def create_label(text):
    return tk.Label(master = frm_recommendations, text = text)
def create_button(text, url):
    return tk.Button(master = frm_recommendations, text = text, command = lambda : open_spotify(url))
def clear(*args):
    args.destroy()
def display_recommendations(response):
    lbl_track_name = tk.Label(master = frm_recommendations, text = 'Track Name')
    lbl_artist_name = tk.Label(master = frm_recommendations, text = 'Artist Name')
    lbl_play_it = tk.Label(master = frm_recommendations, text = 'Play It')
    lbl_track_name.grid(row = 0, column = 0)
    lbl_artist_name.grid(row = 0, column = 1)
    lbl_play_it.grid(row = 0, column = 2)
    for idx, track in enumerate(response['tracks']):
        lbl_track_name_recommended = create_label(track['name'])
        lbl_track_name_recommended.grid(row = idx +1, column = 0)
        lbl_artist_name_recommended = create_label(track['artists'][0]['name'])
        lbl_artist_name_recommended.grid(row = idx + 1, column = 1)
        btn_play_it_recommended = create_button('Play It', track['external_urls']['spotify'])
        btn_play_it_recommended.grid(row = idx +1, column = 2, padx = 30)

def get_recommendation():
	search = ent_search.get()
	sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials("4d4a5193b9fd430c94bc51d415e7d785", "5c561eb16dee40a991241a40f3122242"))
	result = sp.search(q = search, limit = 1)
	id_list = [result['tracks']['items'][0]['id']]
	recommendations  =sp.recommendations(seed_tracks = id_list, limit = 20 )
	display_recommendations(recommendations)

    

window = tk.Tk()
frm_search_field  = tk.Frame(master = window, width = 100)
frm_recommendations = tk.Frame(master = window)
frm_search_field.pack()
frm_recommendations.pack()
ent_search = tk.Entry(master = frm_search_field, width = 25)
ent_search.insert(0, "Sad")
btn_get_recommendations = tk.Button(master = frm_search_field, text = 'Get recommendations', command = get_recommendation ) 	
btn_get_recommendations.invoke()
ent_search.grid(row = 0,column = 0,pady =  30,padx = 30)
btn_get_recommendations.grid(row = 0 , column =1, pady = 30, padx = 30)
window.mainloop()