from tkinter import ttk


def create_tree_view(self):
    self.tree = ttk.Treeview(height=10, columns=("link", "status"), style='Treeview')
    self.tree.grid(row=6, column=0, columnspan=3, ipadx=10, ipady=10, sticky='ew')
    self.tree.heading('#0', text='Count', anchor='W')
    self.tree.heading("link", text='Download Link', anchor='W')
    self.tree.heading("status", text='Download status', anchor='W')
    self.tree.grid_columnconfigure(1, weight=1)
    self.tree.grid_columnconfigure(2, weight=1)
