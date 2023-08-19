from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QMainWindow):#use for make a main window -same thing qwidget but some extra properties
    def __init__(self):
        super().__init__()
        
        self.line = QWidget()
        
        
        # self.setWindowOpacity(0.5) -> edit opacity to main window
        self.dock = QDockWidget(self)
        self.addDockWidget(Qt.LeftDockWidgetArea , self.dock , Qt.Vertical)
        
        self.setCentralWidget(self.line)
        
        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setMinimumHeight(100)
        
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.setStatusTip("Window")
        
        self.menu = QMenuBar()
        self.menu.addAction("Action 1")
        self.setMenuBar(self.menu)
        
        self.resize(800,500)
        self.show()
        
app = QApplication([])
window = main()
app.exec()