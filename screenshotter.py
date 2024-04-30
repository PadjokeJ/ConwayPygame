import pygame
from datetime import datetime
from datetime import date

def screenshot(_scr):
    _date = str(date.today().day) + "_" + str(date.today().month) + "_" + str(date.today().year)
    _time = str(datetime.now().hour) + "_" + str(datetime.now().minute) + "_" + str(datetime.now().second)
    _filename = "screenshot_"+ _date + "_" + _time + ".jpg"
    pygame.image.save(_scr, _filename)