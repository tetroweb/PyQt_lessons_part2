from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.widget = QWidget(self)
        self.widget.setGeometry(50,50,120,60)
        self.widget.setStyleSheet("background-color :red;")
        
        self.animation  =QVariantAnimation(
            startValue = QColor("red"),
            endValue =  QColor("blue"),
            valueChanged = self.anim,
            duration = 3000
        )
        self.animation.start()
        
        self.animation  =QVariantAnimation()
        self.animation.setStartValue(QRect(50,50,120,60))
        self.animation.setEndValue(QRect(100,100,300,150))
        self.animation.setDuration(3000)
        self.animation.valueChanged.connect(self.rect)
        self.animation.start()
        
        self.resize(800,500)
        self.show()
        
        
    def anim(self,v):
        self.widget.setStyleSheet("background-color : %s" % v.name())
    
    def rect(self,v):
        self.widget.setGeometry(v)
    
app = QApplication([])
window = main()
app.exec()