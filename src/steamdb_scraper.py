import brutescrap as bs

c = bs.get("https://steamdb.info/app/275850/info/", "msedge").parse()
print(type(c))

