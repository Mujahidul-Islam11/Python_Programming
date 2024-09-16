#install, import and use your first external module

import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.say("Hey, I am here with my latest food ordering platform ui. Just have completed the front-end also will create a back-end server for real time data implementing")
engine.runAndWait()