#Main Window
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from name_widget import *

class MyWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.name_widget = NameWidget()
        self.hello_widget = HelloWidget()
        self.setCentralWidget(self.name_widget)
        self.name_widget.NameEntered.connect(self.name_provided)

    def name_provided(self):
        self.setCentralWidget.username.text()
        self.hello_widget.label.setText(name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
