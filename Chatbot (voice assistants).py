import pygame
from gtts import gTTS
from playsound import playsound
import sys
import time
import speech_recognition as sr
import pyttsx3
from bardapi import Bard
import os
c = '0'
def bard1(q):
    os.environ['_BARD_API_KEY']="XAgZzWrwb9i5Trv--owOZ2mD-L66K8ANFEJ3y0QXrcnsxafCrbk5a7UYuKv7cNCegfauZQ."

    input_text = "very short answer "+ q
    print(Bard().get_answer(input_text)['content'])
    return Bard().get_answer(input_text)['content']
def SpeakText(command):
	
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
def WW(x):
    x = str(x)
    tts=gTTS(x)
    tts.save(c +".mp3")
def play_audio(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(3)
    #time.sleep(10)
def Stt():
    while True:
        try:
            r1 = sr.Recognizer()
            with sr.Microphone() as source2:
                r1.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r1.listen(source2)
                MyText = r1.recognize_google(audio2)
                MyText = MyText.lower()
                print("You said:", MyText)
                SpeakText(MyText)
                break
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")
    return MyText        
 
 
r1 = sr.Recognizer()
while(1):
    ss = bard1(Stt())
    WW(ss)
    mp3_file5 = r"C:\Users\Hamad\OneDrive\المستندات\Python programs\Chatbot (voice assistants)\\"+ c +'.mp3'
    play_audio(mp3_file5)
    c=c+'1'