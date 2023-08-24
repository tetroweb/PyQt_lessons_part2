from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button = QPushButton("Menu Button",self)
        self.button.setGeometry(100,100,200,40)
        self.button.setFont(QFont("Tahoma",12))
        
        self.menu = QMenu()
        
        action1 = self.menu.addAction("Action 1")
        action2 = self.menu.addAction("Action 2")
        action3 = self.menu.addAction("Action 3")
        action4 = self.menu.addAction("Action 4")
        
        self.button.setMenu(self.menu)
        
        self.button2 = QPushButton("Key Sequence",self)
        self.button2.move(500,100)
        
        self.key =QKeySequenceEdit(self)
        self.key.move(650,100)
        
        self.key.editingFinished.connect(self.shortcut)
        self.button2.clicked.connect(self.succes)
        
        self.resize(800,500)
        self.show()
        
    def shortcut(self):
        self.button2.setShortcut(self.key.keySequence())
    
    def succes(self):
        print("Succes")
        
        
app = QApplication([])
window = main()
app.exec()