"""
BruteScrapper

A webscrapper utilizing mouse manipulation. Prevention for this kind of webscrapping
is currently non-existant, hence a last resort.

Learn more at:
    https://github.com/Neek0tine/BruteScrapper

Required modules:
    clipboard
    pyautogui
    time
    ctypes
    psutil
    bs4

"""
import pywinauto.findwindows
from psutil import NoSuchProcess, AccessDenied, ZombieProcess, process_iter
from . import exceptions_handler
from time import sleep
from ctypes import wintypes
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import Desktop


class Scrapper:
    def __init__(self, browser):
        self.browser = browser
        self.desktop = Desktop(backend='uia')
        self.app = Application(backend='uia')
        self.activeBrowser = self.openBrowser()

    def openBrowser(self):
        if self.isBrowserRunning:
            return self.app.connect(title_re=".*Microsoft​ Edge.*", timeout=10, found_index=0).top_window()
        else:
            self.app.start(f'{self.browser}.exe')
            return self.app.connect(title_re=".*Microsoft​ Edge.*", timeout=10, found_index=0).top_window()

    def isBrowserRunning(self):
        for proc in process_iter():
            try:
                if self.browser.lower() in proc.name().lower():
                    return True
            except (NoSuchProcess, AccessDenied, ZombieProcess):
                pass
        return False

    def get(self, query):
        self.activeBrowser.type_keys("^t")
        _wrapper = self.activeBrowser.child_window(title="App bar", control_type="ToolBar")
        _addressBar = wrapper.descendants(control_type='Edit')[0]
        _addressBar.set_text(query).type_keys('{ENTER}')
        return self


