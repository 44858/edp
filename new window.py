#Main Window
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from name_widget import *
from hello_widget import *

class MyWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.name_widget = NameWidget()
        self.hello_widget = HelloWidget()
        self.setCentralWidget(self.name_widget)
        self.name_widget.NameEntered.connect(self.name_provided)
        self.hello_widget.BackPressed.connect(self.back_pressed)

        self.hello_widget = HelloWidget()
        self.stack = QStackedLayout()
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.hello_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)
        self.setCentralWidget(self.widget)

    def name_provided(self):
        self.stack.setCurrentIndex(1)
        name = self.name_widget.username.text()
        self.hello_widget.message.setText(name)
        self.hello_widget.BackPressed.connect(self.back_pressed)

    def back_pressed(self):
        self.stack.setCurrentIndex(0)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
