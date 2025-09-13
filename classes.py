from tkinter import *

class LegacyScrollableFrame(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.canvas = Canvas(self, highlightthickness = 0)
        self.canvas.pack(side = LEFT, fill = BOTH, expand = True)

        self.scrollbar = Scrollbar(self, orient = VERTICAL, command = self.canvas.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)

        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window = self.inner_frame, anchor = NW)

        self.inner_frame.bind("<Configure>", self.update_scrollregion)

    def update_scrollregion(self, event):
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion = self.canvas.bbox(ALL))