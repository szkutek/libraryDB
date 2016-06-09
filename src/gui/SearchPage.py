import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from AdvancedSearch import AdvancedSearch
from SimpleSearch import SimpleSearch
from Status import Status


class SearchPage(Gtk.Box):
    def __init__(self, lib):
        Gtk.Box.__init__(self)
        self.library = lib

        self.set_spacing(10)
        self.set_border_width(10)

        self.set_homogeneous(True)

        self.status = Status()
        self.simpleSearch = SimpleSearch(self.library, self.status)
        self.advSearch = AdvancedSearch(self.library, self.status)

        self.searchBox = Gtk.VBox()
        self.add(self.searchBox)
        self.searchBox.add(self.simpleSearch)
        self.searchBox.add(self.advSearch)

        self.add(self.status)
