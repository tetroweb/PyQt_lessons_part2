from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.menu = QMenu()
        self.menu.addAction("Action 1")
        self.menu.addSeparator()
        self.menu.addAction("Action 2")
        menu1 = self.menu.addMenu("Menu 1")
        menu1.addAction("Action 3")
        menu1.addAction("Action 4")
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.menu_open1)
        
        self.text =QTextEdit(self)
        self.text.setGeometry(50,50,500,400)        
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.menu_open1)
        
        self.resize(800,500)
        self.show()
    
    def menu_open1(self,p):
        self.menu.exec(self.mapToGlobal((p)))
    def menu_open2(self,p):
        self.menu.exec(self.text.mapToGlobal((p)))
        
app = QApplication([])
window = main()
app.exec()