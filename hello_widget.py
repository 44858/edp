#Hello Widget
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class HelloWidget(QWidget):
    BackPressed = pyqtSignal()
    def __init__(self):
        super().__init__()
        #components
        self.hello = QLabel("Hello")
        self.message = QLabel()
        self.button = QPushButton("Back")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello)
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.back_pushed)

    def back_pushed(self):
        self.BackPressed.emit()
        
