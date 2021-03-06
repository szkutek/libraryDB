import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class SimpleSearch(Gtk.Box):
    def __init__(self, lib, stat):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.library = lib
        self.status = stat

        self.label = Gtk.Label("SIMPLE SEARCH")
        self.label2 = Gtk.Label(" ")

        self.simpleSearchLabel = Gtk.Label("Search for:")
        self.simpleSearch = Gtk.Entry()
        self.simpleSearch.set_max_length(100)

        self.languageLabel = Gtk.Label("Language:")
        self.language = Gtk.Entry()  # COMBO BOX

        self.publishYearLabel = Gtk.Label("Published (from/to):")
        self.publishYear1 = Gtk.Entry()
        self.publishYear2 = Gtk.Entry()

        self.buttonSimpleLabel = Gtk.Label(" ")
        self.buttonSimple = Gtk.Button(label="SEARCH")
        self.buttonSimple.connect("clicked", self.search)

        padding = 7
        self.labelBox = Gtk.VBox(spacing=8)
        self.add(self.labelBox)
        self.labelBox.pack_start(self.label, False, True, padding)
        self.labelBox.pack_start(self.simpleSearchLabel, False, True, padding)
        self.labelBox.pack_start(self.languageLabel, False, True, padding)
        self.labelBox.pack_start(self.publishYearLabel, False, True, padding)
        self.labelBox.pack_start(self.buttonSimpleLabel, False, True, padding)

        self.valuesBox = Gtk.VBox(spacing=10)
        self.add(self.valuesBox)
        self.valuesBox.pack_start(self.label2, False, False, padding)
        self.valuesBox.pack_start(self.simpleSearch, False, False, 0)
        self.valuesBox.pack_start(self.language, False, False, 0)

        self.yearBox = Gtk.Box(spacing=5)
        self.valuesBox.add(self.yearBox)
        self.yearBox.pack_start(self.publishYear1, False, False, 0)
        self.yearBox.pack_start(self.publishYear2, False, False, 0)

        self.valuesBox.pack_start(self.buttonSimple, False, False, 0)

    def search(self, button):
        language = str(self.language.get_text())
        publishYear1 = int(self.publishYear1.get_text())
        publishYear2 = int(self.publishYear2.get_text())
        query = str(self.simpleSearch.get_text())
        queries = query.split(' ')
        results = self.library.query.simple(parameters=(queries, language, publishYear1, publishYear2))

        res = ""
        for k in results:
            res += k + '\n'
        self.status.append('Simple search results:')
        self.status.append(res)
