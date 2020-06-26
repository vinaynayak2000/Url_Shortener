#pip install  pyshorteners

import pyshorteners             

link = input("Enter the URL:")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)