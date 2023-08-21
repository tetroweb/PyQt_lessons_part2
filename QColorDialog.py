from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button = QPushButton("Color setting",self)
        self.button.setGeometry(50,50,190,60)
        self.button.setFont(QFont("Agency FB",24))
        
        self.button.setStyleSheet("background-color : blue ; color : white;")
        
        self.button.clicked.connect(self.set_color)
        
        
        self.resize(800,500)
        self.show()
    def button_style(self,c):
        self.button.setStyleSheet("background-color : %s ; color : white;" %c.name())
        
    
    def set_color(self):
        dialog = QColorDialog()
        dialog.currentColorChanged.connect(self.button_style)
        dialog.exec()
        
        # self.color = dialog.selectedColor()
        # self.button.setStyleSheet("background-color : %s ; color : white;" %self.color.name())
        
        
        
app = QApplication([])
window = main()
app.exec()