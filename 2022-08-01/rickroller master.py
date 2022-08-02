from tkinter import Y
import webbrowser
url1 ='www.youtube.com/watch?v=PnKgygXPxm4&ab_channel=Vitalicus'
url2 ='www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'

pirmas = input("Ar tu mldc? (y/n) = ")

if pirmas == "y":
    webbrowser.open_new(url1)
else:
    webbrowser.open_new(url2)