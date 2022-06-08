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
from bs4 import BeautifulSoup
from ctypes import *
from time import sleep
from psutil import NoSuchProcess, AccessDenied, ZombieProcess, process_iter


# Checks
def checkIfProcessRunning(processName):
    # Check if there is any running process that contains the given name processName.
    # Iterate over the all the running process

    for proc in process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (NoSuchProcess, AccessDenied, ZombieProcess):
            pass
    return False


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
    def __init__(self, query, browser, new_instance=False):
        self.new_instance = new_instance
        self.browserOpened = checkIfProcessRunning(browser)
        self.query = query
        self.browser = browser
        self.content = ''
        self.websiteInterval = 3
        pag.PAUSE = 0.25
        self.paste = ''
        self.block = windll.user32.BlockInput(True)

        pag.hotkey('win', 'r')
        pag.write(browser)
        pag.press("enter")
        pag.write(query)
        pag.press('enter')
        sleep(self.websiteInterval)
        self.block = windll.user32.BlockInput(False)

    def page_source(self):
        self.block = windll.user32.BlockInput(True)
        pag.hotkey("ctrl", "u")
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

    def quit_window(self):
        self.block = windll.user32.BlockInput(True)
        pag.hotkey("alt", "f4")
        self.block = windll.user32.BlockInput(False)


def goto(tab):
    self.block = windll.user32.BlockInput(True)
    pag.hotkey("ctrl", str(tab))
    self.block = windll.user32.BlockInput(False)


def new_tab():
    self.block = windll.user32.BlockInput(True)
    pag.hotkey("ctrl", "t")
    self.block = windll.user32.BlockInput(False)


class batch_get:
    def __init__(self, array):
        self.array = array

        for link in self.array:
            new_tab()
            pag.write(str(link))
            pag.press('enter')


__all__ = ['get', 'close', 'next_tab', 'last_page', 'parse', 'closeLastPage', 'goto', 'batch_get', 'quit_window']
