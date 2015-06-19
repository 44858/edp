#Hello Widget
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class HelloWidget(QWidget):
    Back = pyqtSignal()
    def __init__(self):
        super().__init__()
        #components
        self.message = QLabel()
        self.button = QPushButton("Back")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.button.clicked.connect(self.back_pushed)

    def back_pushed(self):
        print("back pushed")
        self.Back.emit()
        
