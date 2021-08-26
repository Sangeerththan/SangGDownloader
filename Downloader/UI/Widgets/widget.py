from tkinter import Button, Label, LabelFrame, W, E, Entry, Scrollbar
from tkinter import ttk
from tkinter.ttk import Progressbar


def create_label_frame(self):
    labelframe = LabelFrame(self.root, text='SAN G DOWNLOADER', fg='white', bg="#253f59", font=("Monotype Sorts", 15))
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
    self.tree = ttk.Treeview(height=10, columns=("link", "status"), style='Custom.Treeview')
    self.tree.grid(row=6, column=0, columnspan=3, ipadx=15, ipady=25, sticky='e')
    self.tree.heading('#0', text='Count', anchor='center')
    self.tree.heading("link", text='Download Link', anchor='center')
    self.tree.heading("status", text='Download status', anchor='center')
    self.tree.grid_columnconfigure(1, weight=1)
    self.tree.grid_columnconfigure(2, weight=1)
    style = ttk.Style()
    style.element_create("Custom.Treeheading.border", "from", "default")
    style.layout("Custom.Treeview.Heading", [
        ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
        ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                ("Custom.Treeheading.text", {'sticky': 'we'})
            ]})
        ]}),
    ])
    style.configure("Custom.Treeview.Heading",
                    background="blue", foreground="white", relief="flat")
    style.map("Custom.Treeview.Heading",
              relief=[('active', 'groove'), ('pressed', 'sunken')])


def create_scrollbar(self):
    self.scrollbar = Scrollbar(orient='vertical', command=self.tree.yview)
    self.scrollbar.grid(row=6, column=3, rowspan=10, sticky='sn')


def create_progress_bar(self):
    self.progress_bar = Progressbar(orient='horizontal')
    self.progress_bar.grid(row=6, column=3, rowspan=10, sticky='ew')
