import webbrowser
import pyautogui as pg

computerscience = ["https://sites.google.com/gcds.net/cs2"]

fun = ["https://www.youtube.com/watch?v=hTp7PsrJBYY"]


answer = pg.prompt (
"""
Which would you like to do?
a) computer science 
b) fun

"""
    )

if answer == "a":
    for i in computerscience:
        webbrowser.open(i)

elif answer == "b":
    for i in fun:
        webbrowser.open(i)







