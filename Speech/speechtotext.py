import speech_recognition as sr
import speak
r=sr.Recognizer()#creating object for recognizer
with sr.Microphone() as source: #open microphone
    print("speak:")
    audio=r.listen(source)#recorded audio
    print("done")
p=r.recognize_google(audio)#convert the audio and store the text into variable p
speak.tts(p)#text to speech 
