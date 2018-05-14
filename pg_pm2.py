import pyautogui as pg
import time
pg.hotkey ('winleft','ctrl','d')
pg.hotkey ('winleft',)
pg.typewrite ('chrome\n',0.5)
pg.hotkey ('winleft','up')
pg.typewrite ('pink llamas mugs images\n')
time.sleep(3)
pg.hotkey ('ctrl','t')
pg.typewrite ('https://www.youtube.com/watch?v=rGxe83lXgJg\n')
