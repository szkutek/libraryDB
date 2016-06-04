import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from AdvancedSearch import AdvancedSearch
from SimpleSearch import SimpleSearch
from Status import Status


class SearchPage(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

        self.set_spacing(10)
        self.set_border_width(10)

        self.set_homogeneous(True)

        self.simpleSearch = SimpleSearch()
        self.advSearch = AdvancedSearch()
        self.status = Status()

        self.searchBox = Gtk.VBox()
        self.add(self.searchBox)
        self.searchBox.add(self.simpleSearch)
        self.searchBox.add(self.advSearch)

        self.add(self.status)

