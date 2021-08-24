from tkinter import Scrollbar


def create_scrollbar(self):
    self.scrollbar = Scrollbar(orient='vertical', command=self.tree.yview)
    self.scrollbar.grid(row=6, column=3, rowspan=10, sticky='sn')
