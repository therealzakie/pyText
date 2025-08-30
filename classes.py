from tkinter import *

class ScrollableFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.canvas = Canvas(self, highlightthickness = 0)
        self.canvas.pack(side = "left", fill = "both", expand = True)

        self.scrollbar = Scrollbar(self, orient = "vertical", command = self.canvas.yview)
        self.scrollbar.pack(side = "right", fill = "y")

        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window = self.inner_frame, anchor = 'nw')

        self.inner_frame.bind("<Configure>", self.update_scrollregion)

    def update_scrollregion(self, event):
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion = self.canvas.bbox("all"))