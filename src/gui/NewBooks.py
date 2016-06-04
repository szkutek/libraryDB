import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class NewBooks(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("NEW BOOKS")
        self.label2 = Gtk.Label(" ")

        self.genreLabel = Gtk.Label("Genre:")
        self.genre = Gtk.Entry()

        self.languageSearchLabel = Gtk.Label("Language:")
        self.languageSearch = Gtk.Entry()  # COMBO BOX

        self.publishedYearLabel = Gtk.Label("Published:")
        self.publishedYear = Gtk.Entry()

        self.addedYearLabel = Gtk.Label("Added to collection:")
        self.addedYear = Gtk.Entry()

        self.buttonNewLabel = Gtk.Label(" ")
        self.buttonNew = Gtk.Button(label="SEARCH")

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.genreLabel, False, True, padding)
        self.labelBox.pack_start(self.languageSearchLabel, False, True, padding)
        self.labelBox.pack_start(self.publishedYearLabel, False, True, padding)
        self.labelBox.pack_start(self.addedYearLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonNewLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.genre, False, False, 0)
        self.valuesBox.pack_start(self.languageSearch, False, False, 0)
        self.valuesBox.pack_start(self.publishedYear, False, False, 0)
        self.valuesBox.pack_start(self.addedYear, False, False, 0)
        self.valuesBox.pack_start(self.buttonNew, False, False, 0)
