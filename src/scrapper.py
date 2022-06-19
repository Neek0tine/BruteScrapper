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

from . import exceptions_handler
import pywinauto
import logging


# from time import sleep
# from ctypes import wintypes
# from pywinauto import findwindows
# from bs4 import BeautifulSoup


def checkIfProcessRunning(processName):
    from psutil import NoSuchProcess, AccessDenied, ZombieProcess, process_iter

    """
    Check if there is any running process that contains the given name processName.

    :param processName:
    :return: boolean
    """

    for proc in process_iter():
        try:
            # Check if process name contains the given name string.
            if str(processName).lower() in proc.name().lower():
                return True
        except (NoSuchProcess, AccessDenied, ZombieProcess):
            pass
    return False


class Scrapper:
    def __init__(self, browser_type='msedge', use_current=True, log='warn',
                 logging_format='%(levelname)s::%(message)s', timings='fast'):

        from pywinauto.application import Application
        from pywinauto import Desktop
        from platform import architecture

        self.timings = timings
        self.desk = Desktop(backend='uia')
        self.app = Application(backend='uia')
        self.arch = architecture()[0]
        self.use_current = use_current
        self.browser_type = browser_type
        self.browser = ''

        if str(log).lower() == 'crit' or str(log).lower() == 'critical':
            logging.basicConfig(level=logging.CRITICAL, format=logging_format)
        elif str(log).lower() == 'err' or str(log).lower() == 'error':
            logging.basicConfig(level=logging.ERROR, format=logging_format)
        elif str(log).lower() == 'warn' or str(log).lower() == 'warning':
            logging.basicConfig(level=logging.WARNING, format=logging_format)
        elif str(log).lower() == 'info' or str(log).lower() == 'information':
            logging.basicConfig(level=logging.INFO, format=logging_format)
        elif str(log).lower() == 'debug' or str(log).lower() == 'debugging':
            logging.basicConfig(level=logging.DEBUG, format=logging_format)

        if self.use_current:
            logging.debug('use_current set to True. Will try to use available browser.')

        elif not self.use_current:
            logging.debug('use_current set to False. Will try to launch a new browser instance.')

    def start_edge(self):
        """
       Function to start Microsoft Edge

       :return: app
        """
        logging.debug("Microsoft Edge launched.")
        return self.app.start("MicrosoftEdge.exe")

    def start_chrome(self, arch):
        """
        Function to start Google Chrome.

        :param arch: 32bit/64bit
        :return: app
        """
        if arch == '32bit':
            logging.debug("Google Chrome launched.")
            return self.app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\Chrome.exe")
        elif arch == '64bit':
            logging.debug("Google Chrome launched.")
            return self.app.start("C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe")

    def connect_edge(self):
        """
       Initiating pywinauto connection to Microsoft Edge
       Connection done by searching relevant process called .*Microsoft​ Edge.*

       :return: browser
       """
        self.browser = self.app.connect(title_re=".*Microsoft​ Edge.*", timeout=10, found_index=0).top_window()
        logging.debug("Browser connected.")
        return

    def connect_chrome(self):
        """
        Initiating pywinauto connection to Google Chrome
        Connection done by searching relevant process called .*Google​ Chrome.*

        :return: browser
        """
        self.browser = self.app.connect(title_re=".*Google​ Chrome.*", timeout=10,
                                        found_index=0).top_window()
        logging.debug("Browser connected.")
        return

    def run_browser(self):

        """
        Function to start browser based on specified parameter,
        Checks user_current function before starting, False value will start a new browser instance
        starts Microsoft Edge as default and on error.

        :return: Browser Connection
        """
        if self.use_current and checkIfProcessRunning(self.browser_type):
            try:
                self.connect_edge()
                self.browser.restore().set_focus().maximize()
                return

            except pywinauto.timings.TimeoutError:
                logging.warning("Unable to connect to browser process. Launching new instance.")
                self.start_edge()
                self.run_browser()
                return

        elif self.use_current and not checkIfProcessRunning(self.browser_type):
            logging.info('use_current set to True and no available browser. Launching new instance')
            self.start_edge()
            self.run_browser()
            return

        elif not self.use_current:
            if self.browser_type == 'chrome':
                try:
                    self.start_chrome(self.arch)
                    self.connect_chrome()
                    return

                except pywinauto.application.AppStartError:
                    logging.warning('Could not find Google Chrome. Using Microsoft Edge instead.')
                    self.browser_type = 'msedge'
                    self.run_browser()
                    self.connect_chrome()
                    return

            elif self.browser_type == 'msedge' or self.browser_type is None:
                try:
                    self.start_edge()
                    self.connect_edge()
                    return
                except pywinauto.application.AppStartError:
                    logging.critical('Could not find any browser. Contact administrator.')
                    exceptions_handler.BrutescrapException('Could not find Microsoft Edge. Contact administrator.')
                    exit(1)

    def get(self, query):
        """
        A get function similar to requests' get or selenium's. Returns HTMl source
        taken from page source of target websites

        :param query: link
        :return:
        """

        self.run_browser()
        logging.debug(f"Going to {query}")

        from pyperclip import copy, paste
        from time import sleep

        _mainPage = self.browser.window(title="Microsoft Edge")
        logging.debug(f"Got browser's main handle")

        _wrapper = self.browser.window(title="App bar", control_type="ToolBar")
        logging.debug(f"Got addressbar")

        _addressBar = _wrapper.descendants(control_type='Edit')[0]
        logging.debug(f"Editing browser's addressbar {query}")

        _mainPage.type_keys("^t")
        logging.debug(f"Sending 'CTRL+T' to browser")

        _addressBar.set_text(query).type_keys('{ENTER}')
        logging.debug(f"Replaced addressbar with query and entering.")
        sleep(4.75)

        _mainPage.type_keys("^u")
        logging.debug(f"Sending 'CTRL+U' to browser")
        sleep(1)

        _mainPage.type_keys("^a")
        logging.debug(f"Sending 'CTRL+A' to browser")

        _mainPage.type_keys("^c")
        logging.debug(f"Sending 'CTRL+C' to browser")

        _mainPage.type_keys("^w^w")

        _content = paste()
        logging.debug(f"Pasted web page source from clipboard.")

        self.browser.minimize()
        return _content
