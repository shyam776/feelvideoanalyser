# -*- coding: utf-8 -*-
import os
import speech_recognition as sr

def video_to_audio():
    files = os.listdir("./")
    for f in files:
        if f.lower()[-3:] == "mp4":
            print("processing",f)
            process(f)
def audio_to_text():
    files = os.listdir("./")
    for f in files:
        if f.lower()[-3:] == "mp3":
            print("Converting to text",f)
            cprocess(f)
def cprocess(f):
    audio =f
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio = r.record(source)
        print("Done")
    try:
        text = r.recognize_google(audio)
        print(text)
    except Exception as e:
        print(e)
            
    
def process(f):
    inFile = f
    outFile = f[:-3] + "mp3"
    cmd = "ffmpeg -i {} -vn -ac 2 -ar 44100 -ab 320k -f mp3 {}".format(inFile, outFile)
    os.popen(cmd)
video_to_audio()
audio_to_text()