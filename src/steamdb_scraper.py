from brutescrapper import Scrapper

s = Scrapper(browser="MicrosoftEdge")
print(s.get('https://steamdb.info/app/275850/info/'))
# s.focusBrowser()
# s.openBrowser()