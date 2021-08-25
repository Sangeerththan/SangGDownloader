from tkinter import Button, Label, LabelFrame, W, E, Entry, Scrollbar
from tkinter import ttk


def create_label_frame(self):
    labelframe = LabelFrame(self.root, text='SAN G DOWNLOADER', bg="#e009d9", font=("Monotype Sorts", 15))
    labelframe.grid(row=0, column=1, padx=8, pady=8, sticky='e')
    Label(labelframe, text='Download Type   :', bg="#040d57", fg="white").grid(row=1, column=1, sticky=W, pady=2,
                                                                          padx=15)
    self.download_type_field = Entry(labelframe)
    self.download_type_field.grid(row=1, column=2, sticky=W, padx=5, pady=2)
    Label(labelframe, text='ShutDown yes/no:', bg="#040d57", fg="white").grid(row=2, column=1, sticky=W, pady=2,
                                                                            padx=15)
    self.shutdown_field = Entry(labelframe)
    self.shutdown_field.grid(row=2, column=2, sticky=W, padx=5, pady=2)
    Label(labelframe, text='Download Limit  :', bg="#040d57", fg="white").grid(row=3, column=1, sticky=W, pady=2,
                                                                           padx=15)
    self.limit_field = Entry(labelframe)
    self.limit_field.grid(row=3, column=2, sticky=W, padx=5, pady=2)
    Button(labelframe, text='Add Links', command=self.on_add_links_button_clicked, bg="blue", fg="white").grid(
        row=4, column=2, sticky=E, padx=5, pady=5)
    Button(labelframe, text='   clear   ', command=self.on_clear_links_button_clicked, bg="blue", fg="white").grid(
        row=4, column=1, sticky='e', padx=15, pady=5)


def create_tree_view(self):
    self.tree = ttk.Treeview(height=10, columns=("link", "status"), style='Treeview')
    self.tree.grid(row=6, column=0, columnspan=3, ipadx=15, ipady=25, sticky='e')
    self.tree.heading('#0', text='Count', anchor='center')
    self.tree.heading("link", text='Download Link', anchor='center')
    self.tree.heading("status", text='Download status', anchor='center')
    self.tree.grid_columnconfigure(1, weight=1)
    self.tree.grid_columnconfigure(2, weight=1)


def create_scrollbar(self):
    self.scrollbar = Scrollbar(orient='vertical', command=self.tree.yview)
    self.scrollbar.grid(row=6, column=3, rowspan=10, sticky='sn')
