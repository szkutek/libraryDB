import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class PopularBooks(Gtk.Box):
    def __init__(self, lib):
        Gtk.Box.__init__(self)

        self.library = lib

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("POPULAR BOOKS")
        self.label2 = Gtk.Label(" ")

        self.authorLabel = Gtk.Label("Author:")
        self.authorName = Gtk.Entry()
        self.authorSurname = Gtk.Entry()

        self.genreLabel = Gtk.Label("Genre:")
        self.genre = Gtk.Entry()

        self.popularSinceLabel = Gtk.Label("Most popular since:")
        self.popularSince = Gtk.Entry()

        # self.defaultLabel = Gtk.Label(" ")
        # self.default = Gtk.Button(label="Set default")

        self.buttonSearchLabel = Gtk.Label(" ")
        self.buttonSearch = Gtk.Button(label="SEARCH")
        self.buttonSearch.connect("clicked", self.popularBooks)

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.authorLabel, False, True, padding)
        self.labelBox.pack_start(self.genreLabel, False, True, padding)
        self.labelBox.pack_start(self.popularSinceLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonSearchLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)

        self.authorBox = Gtk.Box(spacing=5)
        self.valuesBox.add(self.authorBox)
        self.authorBox.pack_start(self.authorName, False, False, 0)
        self.authorBox.pack_start(self.authorSurname, False, False, 0)

        self.valuesBox.pack_start(self.genre, False, False, 0)
        self.valuesBox.pack_start(self.popularSince, False, False, 0)
        self.valuesBox.pack_start(self.buttonSearch, False, False, 0)

    def popularBooks(self, button):
        authorName = str(self.authorName.get_text())
        authorSurname = str(self.authorSurname.get_text())
        genre = str(self.genre.get_text())
        popularSince = str(self.popularSince.get_text())

        self.library.query.popularBooks(parameters=(authorName, authorSurname, genre, popularSince))
