import pyautogui as pg
import time
import webbrowser

points = 0

# Question 1
answer = pg.prompt(
"""
What are you most likely to do?

a)Eat 38 hot dogs in 8 minutes
b)Become a famous news figure 
c)Say I love you on a first date
d)Make everyday legendary 
"""
    )



# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question 2
answer = pg.prompt(
"""
What are you most likely to become?

a)Kindergarden teacher 
b)Newscaster   
c)Architect  
d)Undetermined    
"""
    )



# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4

# Question 3
answer = pg.prompt(
"""
Where are you from?

a)New York 
b)Canada   
c)Cleavland    
d)From different places   
"""
    )



# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4 

# Question
answer = pg.prompt(
"""
How is your love life now or in the future?

a)Found my special someone, have been with him/her and only him/her
b)Focussed on my job, not my love life 
c)Desperate, looking everywhere to find the right person
d)Feel empty inside, don't know how to love   
"""
    )


# Give Points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
elif answer == "d":
    points += 4 


# END OF SURVERY

pg.alert("You are...")

# Lily
if points < 7:
   pg.alert("Lily Aldrin")
   webbrowser.open("https://www.youtube.com/watch?v=jJZ4lxS32v0")
# Robin
elif points >= 7 and points < 10:
   pg.alert("Robin Scherbatsky or Robin Sparkles")
   webbrowser.open("https://www.youtube.com/watch?v=IY_bhVSGKEg ")
# Ted
elif points >= 10 and points < 14:
    pg.alert("Ted Mosby")
    webbrowser.open("https://www.youtube.com/watch?v=FDHi-Qe0DR0")
# Barney 
elif points >= 14:
    pg.alert("Barney Stinson")
    webbrowser.open("https://www.youtube.com/watch?v=lzuycUY1K3k")
            
    


