from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Resizing widgets inserted into
class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.splitter = QSplitter(Qt.Horizontal)
        self.hbox.addWidget(self.splitter)
        
        
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.widget3 = QWidget()
        
        self.widget1.setStyleSheet("background-color : red;")
        self.widget2.setStyleSheet("background-color : green;")
        self.widget3.setStyleSheet("background-color : blue;")

        self.splitter.addWidget(self.widget1)
        self.splitter.addWidget(self.widget2)
        self.splitter.addWidget(self.widget3)

        self.splitter.setSizes([1,2,3])
        self.splitter.setStyleSheet("QSplitter::handle{background-color : yellow; height:2px;}")
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()