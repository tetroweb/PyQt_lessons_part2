from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.central = QScrollArea()
        
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.setSizeGripEnabled(False)
        
        # self.status.showMessage("Succes",1000)
        self.setStatusTip("Window")
        self.status.addPermanentWidget(QLabel("Message"),1)
        
        self.setCentralWidget(self.central)
        self.resize(800,500)
        self.show()
        
app = QApplication([])
window = main()
app.exec()