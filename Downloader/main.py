from tkinter import Tk, Button, PhotoImage, Label, LabelFrame, W, E, Entry, Scrollbar
from tkinter import ttk

from Downloader.Utils.tasks import links_copied_to_clipboard
from Downloader.Utils.regex import *
from Downloader.Cateogory.youtube import *
from Downloader.Cateogory.torrent import *


class Downloader:

    def __init__(self, root):
        self.root = root
        self.create_gui()
        ttk.style = ttk.Style()
        ttk.style.configure("Treeview", font=('helvetica', 10))
        ttk.style.configure("Treeview.Heading", font=('helvetica', 12, 'bold'))

    def create_gui(self):
        self.create_label_frame()
        self.create_tree_view()
        self.create_scrollbar()

    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text='SAN G DOWNLOADER', bg="sky blue", font="helvetica 10")
        labelframe.grid(row=0, column=1, padx=8, pady=8, sticky='ew')
        Label(labelframe, text='Download Type:', bg="green", fg="white").grid(row=1, column=1, sticky=W, pady=2,
                                                                              padx=15)
        self.download_type_field = Entry(labelframe)
        self.download_type_field.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text='ShutDown yes/no:', bg="brown", fg="white").grid(row=2, column=1, sticky=W, pady=2,
                                                                                padx=15)
        self.shutdown_field = Entry(labelframe)
        self.shutdown_field.grid(row=2, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text='Download Limit:', bg="black", fg="white").grid(row=3, column=1, sticky=W, pady=2,
                                                                               padx=15)
        self.limit_field = Entry(labelframe)
        self.limit_field.grid(row=3, column=2, sticky=W, padx=5, pady=2)
        Button(labelframe, text='Add Links', command=self.on_add_links_button_clicked, bg="blue", fg="white").grid(
            row=4, column=2, sticky=E, padx=5, pady=5)

    def create_tree_view(self):
        self.tree = ttk.Treeview(height=10, columns=("link", "status"), style='Treeview')
        self.tree.grid(row=6, column=0, columnspan=3, ipadx=10, ipady=10, sticky='ew')
        self.tree.heading('#0', text='Name', anchor=W)
        self.tree.heading("link", text='link', anchor=W)
        self.tree.heading("status", text='staus', anchor=W)

    def create_scrollbar(self):
        self.scrollbar = Scrollbar(orient='vertical', command=self.tree.yview)
        self.scrollbar.grid(row=6, column=3, rowspan=10, sticky='sn')

    def on_add_links_button_clicked(self):
        stream_type = self.download_type_field.get()
        stream_limit = int(self.limit_field.get())
        shut = self.shutdown_field.get()
        print(stream_type)
        if stream_type == 'Youtube':
            links_copied_to_clipboard(stream_limit, youtube_regex)
        elif stream_type == 'Torrent':
            _links = links_copied_to_clipboard(stream_limit, torrent_regex)
            downloads(_links)


if __name__ == '__main__':
    root = Tk()
    root.title('Fast downloader By San G')
    root.geometry("800x1000")
    root.resizable(width=False, height=False)
    application = Downloader(root)
    root.mainloop()
