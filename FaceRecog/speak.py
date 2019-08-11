from gtts import gTTS

import pyglet #used to play the audio

import os

def tts(text):
    file = gTTS(text)#google text to speech converter
    filename='temp.mp3'#name given to file

    # Saving the converted audio in mp3 format
    file.save(filename)

    music=pyglet.media.load(filename,streaming = False)#loading the audio file
    music.play()# Playing the audio file

    os.remove(filename) #To delete saved file

