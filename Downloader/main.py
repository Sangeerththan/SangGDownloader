from tkinter import Tk

from Downloader.Cateogory.torrent import *
from Downloader.Cateogory.youtube import *
from Downloader.Cateogory.fb import fb_download_videos
from Downloader.Cateogory.insta import download_insta_images
from Downloader.UI.Widgets.widget import *
from Downloader.Utils.regex import torrent_regex, youtube_regex, fb_regex, instagram_regex


class Downloader:

    def __init__(self, root):
        self.root = root
        self.create_gui()
        ttk.style = ttk.Style()
        ttk.style.configure("Treeview", font=('helvetica', 10))
        ttk.style.configure("Treeview.Heading", font=('helvetica', 12, 'bold'))
        self.show_links([], '')

    def create_gui(self):
        create_label_frame(self)
        create_tree_view(self)
        create_scrollbar(self)

    def on_add_links_button_clicked(self):
        stream_type = self.download_type_field.get().lower()
        stream_limit = int(self.limit_field.get())
        shut = self.shutdown_field.get()
        if stream_type in ['youtube', 'utube']:
            _links = links_copied_to_clipboard(stream_limit, youtube_regex)
            self.show_links(_links, 'Started')
            self.tree.update_idletasks()
            download_videos(_links, shut)
            self.show_links(_links, 'Finished')
            self.tree.update_idletasks()

        elif stream_type == 'torrent':
            _links = links_copied_to_clipboard(stream_limit, torrent_regex)
            self.show_links(_links, 'Started')
            self.tree.update_idletasks()
            downloads(_links, shut)
            self.show_links(_links, 'Finished')
            self.tree.update_idletasks()
        elif stream_type in ['fb', 'facebook']:
            _links = links_copied_to_clipboard(stream_limit, fb_regex)
            self.show_links(_links, 'Started')
            self.tree.update_idletasks()
            fb_download_videos(_links, shut)
            self.show_links(_links, 'Finished')
            self.tree.update_idletasks()
        elif stream_type in ['insta', 'instagram']:
            _links = links_copied_to_clipboard(stream_limit, instagram_regex)
            self.show_links(_links, 'Started')
            self.tree.update_idletasks()
            download_insta_images(_links, shut)
            self.show_links(_links, 'Finished')
            self.tree.update_idletasks()

    def show_links(self, _links, status):
        items = self.tree.get_children()
        count = 0
        for item in items:
            self.tree.delete(item)
        for link in _links:
            count += 1
            self.tree.insert('', 0, text=count, values=(link, status))


if __name__ == '__main__':
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.title('Copyrigt@Sangeerththan')
    root.geometry("650x450")
    root.resizable(width=False, height=False)
    application = Downloader(root)
    root.mainloop()
