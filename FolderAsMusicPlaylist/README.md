# CREATE AND MAINTAIN PLEX MUSIC PLAYLIST FROM FOLDERS

## Thanks to:
Big thanks to **PyCoding-A** for his work: [GitHub Project](https://github.com/PyCoding-A/plex.audio_folder_to_playlist/blob/main/plex_folder_to_playlist.py)

## What can this script do?

- **Create** Music Playlist from folders.
- **Check** if song is already in playlist or not.
- **Add** new songs from folders.
- **Remove** song from playlist if file removed from folder.

## What do you need to amend to use?
- plex_base_url => Add your plex URL
- plex_token => Get your own plex token. You can use the following article: [Plex Support Article](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)
- plex_root => Root folder of your environment. Needed to be defined if Plex and the script running environment are using different locations
- plex_playlist_location => The full path how Plex can connect to the playlist folder location
- folder_location => The full path how the script running environment connect to the playlist folder location

## Synology Scheduled Task
- The script can be setup as a Scheduled Task in Synology.
- Use the following articles to run a custom python script on your NAS:

[Synology Python Scheduled Script](https://synoguide.com/2023/01/21/schedule-python-scripts-on-your-synology/)

[Synology Python Installation](https://synoguide.com/2023/01/21/install-and-use-python-3-9-in-your-synology/)

## Issues?
- Raise an issue in GitHub. 
