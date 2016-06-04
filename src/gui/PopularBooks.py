import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class PopularBooks(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("POPULAR BOOKS")
        self.label2 = Gtk.Label(" ")

        self.authorLabel = Gtk.Label("Author:")
        self.author = Gtk.Entry()

        self.genreLabel = Gtk.Label("Genre:")
        self.genre = Gtk.Entry()

        self.popularSinceLabel = Gtk.Label("Most popular since:")
        self.popularSince = Gtk.Entry()

        # self.defaultLabel = Gtk.Label(" ")
        self.default = Gtk.Button(label="Set default")

        # self.searchLabel = Gtk.Label(" ")
        self.search = Gtk.Button(label="SEARCH")

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.authorLabel, False, True, padding)
        self.labelBox.pack_start(self.genreLabel, False, True, padding)
        self.labelBox.pack_start(self.popularSinceLabel, False, True, padding)
        self.labelBox.pack_start(self.default, False, True, 0)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.author, False, False, 0)
        self.valuesBox.pack_start(self.genre, False, False, 0)
        self.valuesBox.pack_start(self.popularSince, False, False, 0)
        self.valuesBox.pack_start(self.search, False, False, 0)
