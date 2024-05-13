#!/usr/bin/env python3
#https://python-plexapi.readthedocs.io/en/latest/introduction.html

from plexapi.server import PlexServer
import os
from datetime import datetime


#https://www.geeksforgeeks.org/python-list-all-files-in-directory-and-subdirectories/
def list_files_recursive(path='.', listOfFiles=[]):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            list_files_recursive(full_path)
        else:
            listOfFiles.append(full_path.replace('\\', '/'))
    return listOfFiles

start = datetime.now()
#Sourced from: https://github.com/PyCoding-A/plex.audio_folder_to_playlist/blob/main/plex_folder_to_playlist.py
plex_base_url = "<YOUR PLEX IP ADDRESS>:32400/"
#https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
plex_token = "<YOUR PLEX TOKEN>"
plex_root = "/volume1/" #CHANGE IT TO YOUR ENVIRONMENT
plex_playlist_location = "/volume1/music/Playlists/" #CHANGE IT TO YOUR ENVIRONMENT
folder_location = "/volume1/music/Playlists/"        #CHANGE IT TO YOUR ENVIRONMENT
section_name = "Music"

#Plex authentication
plex = PlexServer(plex_base_url, plex_token)
try:
    print("Connected to: " + str(plex.myPlexAccount()).replace('<MyPlexAccount:https://plex.tv/user:', '').replace('>',''))
except:
    print("Unable to connect. Check URL and Token.")
    quit()

#Plex playlist location
playlist_files = list_files_recursive(folder_location)
if plex_playlist_location != folder_location:
    if folder_location.find(":") > 0:
        drive_label = folder_location.split("/")[0]
        #print(playlist_files)
        playlist_files = [sub.replace(drive_label + '/', plex_root) for sub in playlist_files]
        #print(playlist_files)

#Loop through the music files and create the playlist with the items
for section in plex.library.sections():
    music = plex.library.section(section.title)
    if section.type == "artist":
        print(music)
        for mus in music.searchTracks():
            location = mus.locations[0]
            #Only grab files from the given location
            if location.startswith(plex_playlist_location):
                file_name = os.path.basename(location)
                playlist_name = location.replace(plex_playlist_location, '').split('/')[0]
                #If file is in the root folder of the playlist then it should not create a playlist
                if playlist_name != file_name:
                    #Search for playlist name and see if it exists
                    playlist = [playlist for playlist in plex.playlists() if playlist.title == playlist_name]
                    #Creating Playlist and adding items
                    if not playlist:
                        plex.createPlaylist(playlist_name, items=mus)
                        print('Playlist ' + playlist_name + ' created.')
                        print('Song ' + mus.title + ' is added to ' + playlist_name)
                    else:
                        if location in playlist_files:
                            if mus not in plex.playlist(playlist_name):
                                #Add song to playlist
                                plex.playlist(playlist_name).addItems(mus)
                                print('Song ' + mus.title + ' is added to ' + playlist_name)
                        else:
                            if mus in plex.playlist(playlist_name):
                                #Remove song from playlist
                                plex.playlist(playlist_name).removeItems(mus)
                                print(mus.title + ' removed from ' + playlist_name)
        #plex.library(music).refresh()
endInSeconds = int((datetime.now() - start).total_seconds())
print('Script completed in ' + str(endInSeconds) + ' seconds.')
