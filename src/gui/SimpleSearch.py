import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class SimpleSearch(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.label = Gtk.Label("SIMPLE SEARCH")
        self.label2 = Gtk.Label(" ")

        self.simpleSearchLabel = Gtk.Label("Search for:")
        self.simpleSearch = Gtk.Entry()
        self.simpleSearch.set_max_length(100)

        self.languageSearchLabel = Gtk.Label("Language:")
        self.languageSearch = Gtk.Entry()  # COMBO BOX

        self.publishYearLabel = Gtk.Label("Published (from/to):")
        self.publishYear = Gtk.Entry()

        self.buttonSimpleLabel = Gtk.Label(" ")
        self.buttonSimple = Gtk.Button(label="SEARCH")

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.labelBox.set_homogeneous(True)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.simpleSearchLabel, False, True, padding)
        self.labelBox.pack_start(self.languageSearchLabel, False, True, padding)
        self.labelBox.pack_start(self.publishYearLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonSimpleLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.simpleSearch, False, False, 0)
        self.valuesBox.pack_start(self.languageSearch, False, False, 0)
        self.valuesBox.pack_start(self.publishYear, False, False, 0)
        self.valuesBox.pack_start(self.buttonSimple, False, False, 0)
