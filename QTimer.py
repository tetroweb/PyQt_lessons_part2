from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.succes)
        self.control = 0
        
        self.button = QPushButton(self)
        
        self.resize(800,500)
        self.show()
    
    def succes(self):
        self.control +=1
        if self.control == 5:
            self.timer.stop()
            self.timer.singleShot(3000, Qt.PreciseTimer , self.button_resize)
        self.button.resize(self.button.width()+10,self.button.height())
    def button_resize(self):
        self.button.resize(self.button.width()+50,self.button.height()+20)
    
    
app = QApplication([])
window = main()
app.exec()