import pyautogui as pg

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.3)
pg.hotkey('winleft','up')
pg.typewrite('gcds.net\n',0.1)
pg.moveTo(1199, 185, 3)
pg.moveTo(1072, 185, 1)
pg.click()
pg.typewrite('athletics\n',0.3)



