#Hello Widget
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class HelloWidget(QWidget):
    Back = pyqtSignal()
    def __init__(self):
        super().__init__()
        
