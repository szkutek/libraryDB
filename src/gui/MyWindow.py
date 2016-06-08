import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from src.model.Library import Library
from src.utility.DBConnector import DBConnector
from RegisterPage import RegisterPage
from AddPage import AddPage
from LoansPage import LoansPage
from SearchPage import SearchPage
from NewAndPopularPage import NewAndPopularPage


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Library")

        self.library = Library(dbC=DBConnector(user='root', password='root1234', database='library'))

        # gui
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.addPg = AddPage(lib=self.library)
        self.addPg.utilities.buttonAuthor.connect("clicked", self.run)

        self.addUtiPage = Gtk.Box()
        self.addUtiPage.set_border_width(10)
        self.addUtiPage.add(self.addPg)
        self.notebook.append_page(self.addUtiPage, Gtk.Label("Add"))

        self.registerPg = RegisterPage(lib=self.library)

        self.registerPage = Gtk.Box()
        self.registerPage.set_border_width(10)
        self.registerPage.add(self.registerPg)
        self.notebook.append_page(self.registerPage, Gtk.Label('Register'))

        self.loansPg = LoansPage(lib=self.library)

        self.loanPage = Gtk.Box()
        self.loanPage.set_border_width(10)
        self.loanPage.add(self.loansPg)
        self.notebook.append_page(self.loanPage, Gtk.Label('Loans'))

        self.searchPg = SearchPage(lib=self.library)

        self.searchPage = Gtk.Box()
        self.searchPage.set_border_width(10)
        self.searchPage.add(self.searchPg)
        self.notebook.append_page(self.searchPage, Gtk.Label('Search'))

        self.newAndPopular = NewAndPopularPage(lib=self.library)

        self.newAndPop = Gtk.Box()
        self.newAndPop.set_border_width(10)
        self.newAndPop.add(self.newAndPopular)
        self.notebook.append_page(self.newAndPop, Gtk.Label('New and popular books'))

    def run(self, x):
        cursor = self.library.query.advanced(parameters=('asi', 'asi', 'found', 1970, 's', '12345'))
        result = "Executed query: {query}\nResult:\n"
        for (author, title, publish_year, language, publisher, available) in cursor:
            result += (
                str(author) + ',' + str(title) + ',' + str(publish_year) + ',' + str(language) + ',' + str(
                    publisher) + ',' + str(available))
        buff = self.addPg.status.textView.get_buffer()
        buff.set_text(result)

        # self.library


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
