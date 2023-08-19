from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.central = QWidget()
        
        self.dock = QDockWidget()
        self.addDockWidget(Qt.LeftDockWidgetArea,self.dock,Qt.Vertical)
        self.dock.setWidget(QScrollArea())
        
        self.dock.setWindowTitle("Dock Widget")
        
        self.dock.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        
        # self.dock.setFloating(True)
        
        self.setCentralWidget(self.central)
        
        
        self.resize(800,500)
        self.show()
        
app = QApplication([])
window = main()
app.exec()