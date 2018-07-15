# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:16:22 2018

@author: Mehran Zareh
mehranzareh@gmail.com
+39 3911084002
"""


from common.mainwindow import mainWindow, Tk, Label
from PIL import ImageTk,Image

root = Tk(screenName='main window')
app = mainWindow(root)
#app.master.title('Shelem')

def game_initializer():
    file_names = [r'.\resources\cards\\'+ x+'.png' for x in  ['2D', '2S', '2H'] ]
    return file_names

initial_cards = game_initializer()
#image = [Image.open(x) for x in initial_cards]


#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(initial_cards[0]))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(app, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")


app.mainloop()
