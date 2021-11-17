from ui import main_window
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, app=None):
        super(MainWindow, self).__init__(parent)
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.ui.btn.clicked.connect(self.btn_pressed)

    def btn_pressed(self):
        print('Pressed button!')
