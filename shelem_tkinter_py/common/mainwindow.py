# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:24:11 2018

@author: Mehran Zareh
mehranzareh@gmail.com
+39 3911084002
"""


from tkinter import *

class mainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('Shelem')
        self.master.configure(background='green')