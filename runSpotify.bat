@echo off
start spotify.exe
timeout /t 3 /nobreak
cd "C:\Users\balaj\VS Code\General\Python\Spotify"
python3 Spotify_song_liker.py
exit