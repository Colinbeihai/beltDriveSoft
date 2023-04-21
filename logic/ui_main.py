"""
在此编写调用几个页面的逻辑
"""

import sys
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtWidgets
from uiPy.login import Ui_Dialog

if __name__ == "__main__":

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app= QtWidgets.QApplication(sys.argv)

    MainWindow = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())