from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.logo = QLabel()
        self.slider = QSlider(Qt.Horizontal)
        self.volume = QLabel("0")
        
        self.resize(800,500)
        self.show()
        
        
        
app = QApplication([])
window = main()
app.exec()