import sys, time
from PyQt4 import QtGui, QtCore
from ui import Ui_Form

class addTab(QtGui.QWidget):
    def __init__(self, parent = None):
        super(addTab, self).__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def slot_add_data_port(self):
        pass

    def slot_test(self, text):
        print text

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = addTab()
    myapp.show()
    sys.exit(app.exec_())