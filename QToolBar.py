from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QMainWindow):#use for make a main window -same thing qwidget but some extra properties
    def __init__(self):
        super().__init__()
        
        self.toolbar = QToolBar()
        self.toolbar.addAction("Click 1")
        self.toolbar.addAction("Click 2")
        self.toolbar.addSeparator()
        self.toolbar.addAction("Click 3")
        self.toolbar.addAction("Click 4")
        
        self.toolbar.setAllowedAreas(Qt.TopToolBarArea)#Allow the are which movable for the toolbar
        self.toolbar.setFloatable(False)#toolbar does not left the window
        self.toolbar.setMovable(False) #toolbar does not movable
        
        self.addToolBar(Qt.LeftToolBarArea , self.toolbar)# first value for the location 
        
        self.resize(800,500)
        self.show()
        
app = QApplication([])
window = main()
app.exec()