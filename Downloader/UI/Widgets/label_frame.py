from tkinter import Button, Label, LabelFrame, W, E, Entry, Scrollbar


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