# import python module

import pyshorteners

shortener=pyshorteners.Shortener()

long_link=input("enter the long link: ")
short_link=shortener.tinyurl.short(long_link)
print(short_link)