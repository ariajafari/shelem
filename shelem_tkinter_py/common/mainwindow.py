# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:24:11 2018

@author: Mehran Zareh
mehranzareh@gmail.com
+39 3911084002
"""


from tkinter import *

class mainWindow(Frame):
    def __init__(this, master=None):
        Frame.__init__(this, master)
        this.master = master
        this.master.title('Shelem')
        this.master.configure(background='green')
        this.master.geometry('800x550')
        
    