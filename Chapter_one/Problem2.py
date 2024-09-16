#install, import and use your first external module

import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.say("Primarily there are following data types in python")
engine.runAndWait()