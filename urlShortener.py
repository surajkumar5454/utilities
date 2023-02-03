import pyshorteners

link = "www.google.com"

shorturl = pyshorteners.Shortener().tinyurl.short(link)

print(shorturl)
