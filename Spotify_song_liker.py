import os
import pyautogui as pg
import time
import keyboard
import threading
import mouse

# Flag to control the spotify_like loop
spotify_running = True

def spotify_like():
    global spotify_running
    while spotify_running:
        if keyboard.is_pressed('ctrl+shift+alt+l'):
            print('Shortcut ctrl+shift+alt+L pressed')
            mouse.move(1800, 1080)
            time.sleep(0.5)
            mouse.click(button='left')
            mouse.move(1850, 1040)
            time.sleep(0.5)
            mouse.click(button='left')
            mouse.click(button='left')
            try:
                x, y = pg.locateCenterOnScreen('C:\\Users\\balaj\\VS Code\\General\\Python\\Spotify\\spotify_like_icon.png')
                pg.click(x, y, 1)
                keyboard.press_and_release('alt+f4')
                print("Song Liked!")
            except TypeError:
                print("Could not like the song, try again!")
        elif keyboard.is_pressed('ctrl+shift+alt+o'):
            print('Shortcut ctrl+shift+alt+O pressed')
            mouse.move(1800, 1080)
            time.sleep(0.5)
            mouse.click(button='left')
            mouse.move(1850, 1040)
            time.sleep(0.5)
            mouse.click(button='left')
            mouse.click(button='left')
        time.sleep(0.1)

def is_spotify_running():
    while True:
        output = os.popen('wmic process get description, processid').read()
        if 'Spotify.exe' not in output:
            break
        time.sleep(2)

spotify_task = threading.Thread(target=spotify_like)
spotify_check = threading.Thread(target=is_spotify_running)

spotify_check.start()
spotify_task.start()

# Wait for the Spotify thread to finish before exiting
spotify_check.join()

# Set the flag to stop the spotify_like loop
spotify_running = False
