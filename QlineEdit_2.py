from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.line1 = QLineEdit(self)
        self.line2 = QLineEdit(self)
        self.line1.setGeometry(50,50,250,50)
        self.line2.setGeometry(450,50,250,50)
        
        self.label = QLabel("Move Here",self)
        self.label.setGeometry(260,300,250,50)
        self.label.setAlignment(Qt.AlignCenter)
        self.line1.setFont(QFont("Tahoma",20))
        self.line2.setFont(QFont("Tahoma",20))
        self.label.setFont(QFont("Tahoma",20))
        
        self.line1.textEdited.connect(self.control)#textedit içine yazı yazarken olmasını istediğin olaylar eklenir
        self.line1.setDragEnabled(True)
        self.label.setAcceptDrops(True)
        
        self.label.dragEnterEvent = QDragEnterEvent.accept
        self.label.dropEvent = self.drop
        
        self.resize(800,500)
        self.show()
    def control(self):
        # self.label.setText(self.line1.text())
        if self.line1.text() =="":
            self.line1.setStyleSheet("border : 2px solid red;")
        else:
            self.line1.setStyleSheet("border : 2px solid skyblue;")
    def drop(self,e):
        self.label.setText(e.mimeData().text())
        
app = QApplication([])
window = main()
app.exec()