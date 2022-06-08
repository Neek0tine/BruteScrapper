"""
BruteScrapper

A webscrapper utilizing mouse manipulation. Prevention for this kind of webscrapping
is currently non-existant, hence a last resort.

Usage:
    import brutescrap as bs
    bs.get("https://example.com")

Required modules:
    clipboard
    pyautogui
    time

"""

__version__ = '0.0.1'

import pyautogui as pag
import clipboard as cp
from bs4 import  BeautifulSoup
from ctypes import *
from time import sleep

SCREEN_WIDTH, SCREEN_HEIGHT = pag.size()


# Exceptions
class BrutescrapException(RuntimeError):
    pass


class BrutescrapWindowException(BrutescrapException):
    def __init__(self, message):
        message += " (%s)" % ctypes.WinError()
        super(BrutescrapWindowException, self).__init__(message)


class BrutescrapTimeoutException(BrutescrapException):
    pass


# Functions

class get:
    def __init__(self, query, browser):
        self.query = query
        self.browser = browser
        self.content = ''
        self.websiteInterval = 3
        self.processInterval = 0.25
        self.paste = ''
        self.block = windll.user32.BlockInput(True)

        pag.hotkey('win', 'r')
        pag.write(browser)
        pag.press("enter")
        sleep(self.processInterval)
        pag.write(query)
        pag.press('enter')
        sleep(self.websiteInterval)
        self.block = windll.user32.BlockInput(False)

    def page_source(self):
        self.block = windll.user32.BlockInput(True)
        pag.hotkey("ctrl", "u")
        sleep(self.processInterval)
        pag.hotkey("ctrl", "a")
        pag.hotkey("ctrl", "c")
        sleep(self.websiteInterval)
        pag.hotkey("ctrl", "w")
        self.paste = cp.paste()
        self.block = windll.user32.BlockInput(False)
        return self.paste

    def close(self):
        self.block = windll.user32.BlockInput(True)
        pag.hotkey("ctrl", "w")
        self.block = windll.user32.BlockInput(False)

    def next_tab(self):
        self.block = windll.user32.BlockInput(True)
        pag.press("pgdown")
        self.block = windll.user32.BlockInput(False)

    def last_page(self):
        self.block = windll.user32.BlockInput(True)
        pag.press("pgup")
        self.block = windll.user32.BlockInput(False)

    def parse(self):
        if self.paste == '':
            self.page_source()

        return BeautifulSoup(self.paste, "html.parser")



__all__ = ['get', 'close', 'next_tab', 'last_page', 'parse', 'closeLastPage', 'quit_browser']
