from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        
        self.tbutton1 =QToolButton()
        self.tbutton1.setText("Click 1")
        
        self.tbutton2 =QToolButton()
        self.tbutton2.setText("Click 2")
        
        self.tbutton3 =QToolButton()
        self.tbutton3.setText("Click 3")
        
        self.tbutton4 =QToolButton()
        self.tbutton4.setText("Click 4")
        
        self.tbutton5 =QToolButton()
        self.tbutton5.setText("Click 5")
        
        self.hbox.addWidget(self.tbutton1)
        self.hbox.addWidget(self.tbutton2)
        self.hbox.addWidget(self.tbutton3)
        self.hbox.addWidget(self.tbutton4)
        self.hbox.addWidget(self.tbutton5)
        
        
        
        
        self.resize(800,500)
        self.show()
        
        
        
        
        
        
app = QApplication([])
window = main()
app.exec()