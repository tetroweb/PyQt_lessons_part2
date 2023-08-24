from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.widget1= QWidget(self)
        self.widget2 = QWidget(self.widget1)
        self.widget3 = QWidget(self.widget2)
        
        self.widget1.setGeometry(50,50,400,400)
        self.widget2.setGeometry(50,50,300,300)
        self.widget3.setGeometry(50,50,100,100)
        
        self.widget1.setMouseTracking(True)
        self.widget2.setMouseTracking(True)
        self.widget3.setMouseTracking(True)
        
        self.button = QPushButton("Click",self.widget3)
        self.button.setGeometry(10,40,80,20)
        
        self.widget1.setStyleSheet("background-color :red;")
        self.widget2.setStyleSheet("background-color :green;")
        self.widget3.setStyleSheet("*{background-color :blue;}QPushButton{background-color:white;}")
        
        self.label = QLabel("Position",self)
        self.label.move(550,100)
        self.label.setFont(QFont("Calibri",30))
        
        pos = self.button.pos()
        pos = self.widget3.mapToParent(self.button.pos())#button position according to widget 2
        pos = self.widget3.mapTo(self.widget1,self.button.pos())
        pos = self.widget3.mapToGlobal(self.button.pos())
        
        print(pos.x(),pos.y())
        
        self.setMouseTracking(True)
        
        self.resize(800,500)
        self.show()
    def mouseMoveEvent(self,e):
        self.label.setText("{}-{}".format(str(e.pos().x()),str(e.pos().y())))
        
    
    
app = QApplication([])
window = main()
app.exec()