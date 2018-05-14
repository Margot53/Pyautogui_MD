import pyautogui as pg
import webbrowser
import time

answer = pg.prompt(
    """
Are you hungry?
a)Yes
b)No

""")

if answer == "b":
    answer = pg.prompt(
        """
Kk Bye!
""")
    
elif answer == "a":
    food= pg.confirm("What kind of food would you like?", title="Choose food", buttons=['Chinese Food', 'Mexican Food', 'Italian Food', 'Healthy Food', 'Other Food'])


    if food == "Chinese Food":
        webbrowser.open("http://www.orientalgourmetct.com/")

    elif food == "Mexican Food":
        webbrowser.open("https://www.mexipes.com/popular-mexican-food/")

    elif food == "Italian Food":
        webbrowser.open("https://www.walksofitaly.com/blog/all-around-italy/the-16-most-iconic-foods-to-eat-in-italy")

    elif food == "Healthy Food":
        webbrowser.open("https://www.bbcgoodfood.com/recipes/category/healthy")

    elif food == "Other Food":
        webbrowser.open("https://www.plated.com/?utm_ad=25Dx2&cvosrc=ppcbrand.google.PR_BRD-Platedv2-D-EX_Plated_EX&utm_medium=ppcbrand&utm_source=google&utm_content=PR_BRD-Platedv2-D-EX_Plated_EX&utm_term=plated&cvo_campaign=PR_BRD-Platedv2-D-EX&utm_campaign=PR_BRD-Platedv2-D-EX&gclid=EAIaIQobChMIrPLfzJC_2gIVCl8NCh1kMQB2EAAYASAAEgK5NvD_BwEhttps://www.plated.com/?utm_ad=25Dx2&cvosrc=ppcbrand.google.PR_BRD-Platedv2-D-EX_Plated_EX&utm_medium=ppcbrand&utm_source=google&utm_content=PR_BRD-Platedv2-D-EX_Plated_EX&utm_term=plated&cvo_campaign=PR_BRD-Platedv2-D-EX&utm_campaign=PR_BRD-Platedv2-D-EX&gclid=EAIaIQobChMIrPLfzJC_2gIVCl8NCh1kMQB2EAAYASAAEgK5NvD_BwE")

        
        
    

  









   
