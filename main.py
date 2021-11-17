from ui import interface_main_window
from PyQt5 import QtWidgets
import sys


def main():
    qapp = QtWidgets.QApplication(sys.argv)
    window = interface_main_window.MainWindow(app=qapp)
    window.show()
    sys.exit(qapp.exec_())


if __name__ == '__main__':
    main()
