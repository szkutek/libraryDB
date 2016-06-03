import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from RegisterPage import RegisterPage
from AddPage import AddPage
from  src.model.Library import Library
from src.utility.connector import DBConnector


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Library")

        self.library = Library(DBConnector(user='root', password='root1234', database='library'))

        # gui
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.addPage = AddPage()
        self.addPage.utilities.buttonAuthor.connect("clicked",self.run)

        self.addUtiPage = Gtk.Box()
        self.addUtiPage.set_border_width(10)
        self.addUtiPage.add(self.addPage)
        self.notebook.append_page(self.addUtiPage, Gtk.Label("Add"))

        self.regPage = RegisterPage()

        self.registerPage = Gtk.Box()
        self.registerPage.set_border_width(10)
        self.registerPage.add(self.regPage)
        self.notebook.append_page(self.registerPage, Gtk.Label('Register'))

        self.updatePage = Gtk.Box()
        self.updatePage.set_border_width(10)
        self.updatePage.add(Gtk.Label('Loans:'))
        self.notebook.append_page(self.updatePage, Gtk.Label('Loans'))

        self.searchPage = Gtk.Box()
        self.searchPage.set_border_width(10)
        self.searchPage.add(Gtk.Label('Search'))
        self.notebook.append_page(self.searchPage, Gtk.Label('Search'))

        self.newAndPop = Gtk.Box()
        self.newAndPop.set_border_width(10)
        self.newAndPop.add(Gtk.Label('NEW AND POPULAR:'))
        self.notebook.append_page(self.newAndPop, Gtk.Label('New and popular books'))

    def run(self,x):
        cursor = self.library.advQuery.advanced(parameters=('asi', 'asi', 'found', 1970, 's', '12345'))
        result = "Executed query: {query}\nResult:\n"
        for (author, title, publish_year, language, publisher, available) in cursor:
            result += (
                str(author) + ',' + str(title) + ',' + str(publish_year) + ',' + str(language) + ',' + str(
                    publisher) + ',' + str(available))
        buff = self.addPage.status.get_buffer()
        buff.set_text(result)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
