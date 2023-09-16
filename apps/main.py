from PySide6 import QtGui, QtWidgets
import pyperclip
from ressources import *

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Répertoire de contacts")
        self.setWindowIcon(QtGui.QIcon(DIR_PATH + "\\data\icon.ico"))
        self.initUI()
        self.loadDatabase()

    def initUI(self):
        # --- Creates components ---
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.le_search = QtWidgets.QLineEdit()
        self.lw_names_list = QtWidgets.QListWidget()
        self.lbl_num = QtWidgets.QLabel()
        self.btn_copy_num = QtWidgets.QPushButton()
        self.btn_add_num = QtWidgets.QPushButton()
        self.btn_del_num = QtWidgets.QPushButton()

        # --- Adds components ---
        self.main_layout.addWidget(self.le_search)
        self.main_layout.addWidget(self.lw_names_list)
        self.main_layout.addWidget(self.lbl_num)
        self.main_layout.addWidget(self.btn_copy_num)
        self.main_layout.addWidget(self.btn_add_num)
        self.main_layout.addWidget(self.btn_del_num)

        # --- Links components ---
        self.lw_names_list.itemClicked.connect(self.displayNum)
        self.le_search.textChanged.connect(self.search)
        self.btn_copy_num.clicked.connect(self.copyNum)
        self.btn_add_num.clicked.connect(self.createContact)
        self.btn_del_num.clicked.connect(self.deleteContact)

        # --- Component settings ---
        self.le_search.setPlaceholderText("Rechercher")
        self.btn_copy_num.setText("Copier")
        self.btn_add_num.setText("Nouveau")
        self.btn_del_num.setText("Supprimer")

    def loadDatabase(self):
        "Loads the content of the json database into `lw_names_list`."
        database = loadJsonFile()
        self.lw_names_list.clear()
        for key in database.keys():
            self.lw_names_list.addItem(database[key][0])
    
    def displayNum(self):
        "Displays the phone number (in the label `lbl_num`) of the selected contact in `lbl_num`."
        database = loadJsonFile()
        for key in database.keys():
            if self.lw_names_list.currentItem().text() == database[key][0]:
                self.lbl_num.setText(interToFrench(database[key][1], True))
    
    def copyNum(self):
        "Copies the content of `lbl_num` into the clipboard."
        pyperclip.copy(frenchToInter(self.lbl_num.text()))

    def deleteContact(self):
        "Deletes the selected contact from the json database and updates the contents of `lw_names_list`."
        if self.lw_names_list.currentItem():
            database = loadJsonFile()
            del database[str(self.lw_names_list.currentRow())]
            writeJsonFile(formatDict(database))
            self.loadDatabase()
            self.lbl_num.clear()
            self.le_search.clear()

    def createContact(self):
        "Adds a contact (name and phone number) into the json database and updates the content of `lw_names_list` "
        database = loadJsonFile()

        name = QtWidgets.QInputDialog.getText(self, ' ', 'Entrez le nom du contact :')[0]
        if name in database.keys():
            raise(TypeError("You can't create the same two contacts"))

        num = QtWidgets.QInputDialog.getText(self, ' ', 'Entez le numéro de télépone (format international) :')[0]
        if not (num[0] == "+" and num[1:].isdigit()) :
            raise(TypeError("The phone number must be in international format and contain only digits"))

        # Set new key to increment by 1, otherwise key is set to 0
        i = int(list(database.keys())[-1]) if len(database.keys()) != 0 else -1
        database[str(i+1)] = [name, num]
        writeJsonFile(database)
        self.loadDatabase()
        self.lw_names_list.setCurrentItem(self.lw_names_list.item(self.lw_names_list.count() - 1))
        self.lbl_num.setText(num)
    
    def search(self):
        "Searches for a matching string in the database."
        # If the query is empty, we load the content of all the database into `lw_names_list`
        self.lbl_num.clear()
        query = self.le_search.text()
        if query == "":
            self.loadDatabase()
            return None

        db = loadJsonFile()
        search_result = []

        # If the list `items` which contains :
        if items := [
                # Creates a list of tuples containing the name and phone number ONLY if the following condition is True
                (db[key][0], db[key][1]) for key in db.keys()
                # If `query` matches a name
                if query.lower().replace(" ", "") in db[key][0].lower().replace(" ", "") 
                # OR a phone number
                or query.replace(" ", "") in db[key][1] or query.replace(" ", "") in interToFrench(db[key][1])
            ]:
            search_result = [item[0] for item in items] # gets all the names that match the query

        # If there is at least one result, it/they is/are displayed in `lw_names_list`
        self.lw_names_list.clear()
        if search_result:
            for item in search_result:
                self.lw_names_list.addItem(item)

if __name__ == '__main__': 
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec()