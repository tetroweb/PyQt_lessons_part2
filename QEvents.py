from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class main(QWidget):
    def __init__(self):
        super().__init__()
        
        
        
        
        
        
        
        
        self.resize(800,500)
        self.show()
    def closeEvent(self,event):
        print("Exit is succes")
        # event.ignore()
    def showEvent(self,event):
        print("Window opened")
    def enterEvent(self,e): 
        print("Enter the window")
    def leaveEvent(self, event):
        print("Exit the window")
    def moveEvent(self, event):
        print(self.pos())
    def keyPressEvent(self, event):
        print("Clicked the button")
    def keyReleaseEvent(self, event):
        print("hand pulled away")    
    def mouseMoveEvent(self,event):
        print(event.pose())
    def mousePressEvent(self,event):
        print("Clicked mouse")
    def mouseReleaseEvent(self,event):
        print("Mouse pulled away")
    def mouseDoubleClickedEvent(self,event):
        print("Double-click to mouse")
    def resizeEvent(self,event):
        print(self.size())
        
app = QApplication([])
window = main()
app.exec()