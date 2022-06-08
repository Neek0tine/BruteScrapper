import brutescrap as bs

# 'get', 'close', 'next_tab', 'last_page', 'parse', 'closeLastPage', 'goto', 'batch_get', 'quit_window'

c = bs.get("https://steamdb.info/app/275850/info/", "msedge").parse()
print(type(c))
# <class 'bs4.BeautifulSoup'>

source = bs.get("https://steamdb.info/app/275850/info/", "msedge").page_source()
print(type(source))
# <class 'str'>

