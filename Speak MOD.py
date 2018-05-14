import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Hello greatest person of all time")

answer = pg.prompt("Enter your favorite color.")

if answer == "blue":
    speak.Speak("I don't like that color its ugly.")

elif answer =="green":
    speak.Speak("I love that color.")

else:
    speak.Speak("You like the color " + answer)

speak.Speak("What kind of video should we watch?")

video = pg.prompt("Enter video below.")

speak.Speak("Ok, let's look for it" + video + "on youtube and see what we find.")

wb.open("https://www.youtube.com/results?search_query=" + video)
