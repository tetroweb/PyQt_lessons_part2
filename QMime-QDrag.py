from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel("<a href = 'www.youtube.com'>Youtube</a>",self)
        self.label.move(40,40)
        self.label.resize(140,50)
        self.label.setFrameShape(QFrame.Panel)
        
        self.label.setFont(QFont("Consolas",15))
        
        self.label.mouseMoveEvent = self.drag
        
        self.label2 = label("Move Here",self)
        self.label2.setGeometry(250,40,140,50)
        self.label2.setFrameShape(QFrame.Panel)
        self.label2.setAcceptDrops(True)
        self.label2.setFont(QFont("Consolas",15))
        
        self.label3 = QLabel(self)
        self.label3.setGeometry(100,100,60,60)
        self.label3.setPixmap(QPixmap("search_logo.png"))
        self.label3.setScaledContents(True)
        
        self.label3.mouseMoveEvent = self.drag
        
        self.label4 = QLabel("Color",self)
        self.label4.setGeometry(40,200,140,50)
        self.label4.setStyleSheet("background-color: red;")
        
        self.label4.mouseMoveEvent = self.drag
        
        self.resize(800,500)
        self.show()
    
    def drag(self,e):
        drag = QDrag(self)
        mimeData = QMimeData()
        mimeData.setColorData(self.label4.palette().color(QPalette.Background))
        mimeData.setImageData(self.label3.pixmap())
        mimeData.setText(self.label.text())
        mimeData.setHtml(self.label.text())
        drag.setMimeData(mimeData)
        drag.exec()


class label(QLabel):
    def __init__(self,text,parent):
        super().__init__(text,parent)
        
    def dragEnterEvent(self, e) :
        e.accept()
    
    def dropEvent(self, e):
        # self.setText(e.mimeData().text())
        # self.setText(e.mimeData().html())
        
        # if e.mimeData().hasImage():
        #     self.setPixmap(e.mimeData().imageData())
        #     self.setScaledContents(True)
        
        if e.mimeData().hasColor():
            self.setStyleSheet("background-color: %s" %e.mimeData().colorData().name())
        
app = QApplication([])
window = main()
app.exec()