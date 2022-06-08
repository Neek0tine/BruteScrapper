import pyautogui as pag
import clipboard as cp
import time


class Scrapper:
    def __init__(self):
        self.screenW, self.screenH = pag.size()

    def get(self, query):
        pag.hotkey('win', 'r')
        pag.write("msedge")
        pag.press("enter")
        time.sleep(0.2)
        pag.write(query)
        pag.press('enter')
        time.sleep(1)
        pag.hotkey("ctrl", "u")
        time.sleep(2)
        pag.hotkey("ctrl", "a")
        time.sleep(0.2)
        pag.hotkey("ctrl", "c")
        return cp.paste()


s = Scrapper()
print(s.get('https://steamdb.info/app/275850/info/'))
