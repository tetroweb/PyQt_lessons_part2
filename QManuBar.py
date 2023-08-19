from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QMainWindow):#use for make a main window -same thing qwidget but some extra properties
    def __init__(self):
        super().__init__()
        
        self.menubar = QMenuBar()
        
        menu1 = self.menubar.addMenu("Menu 1")
        menu2 = self.menubar.addMenu("Menu 2")
        
        action1 = self.menubar.addAction("Action1")
        action2 = self.menubar.addAction("Exit")
        action2.triggered.connect(self.close)
        
        action3 = menu1.addAction("Action3")
        action4 = menu1.addAction("Action4")
        action4.setShortcut("Ctrl+X")
        action5 = menu1.addAction("Action5")
        
        menu3 = menu1.addMenu("Menu 3")
        action6 = menu3.addAction("Action 6 ")
        
        self.setMenuBar(self.menubar)
        
        self.resize(800,500)
        self.show()
        
app = QApplication([])
window = main()
app.exec()