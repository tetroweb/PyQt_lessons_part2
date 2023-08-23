from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


#If we want to write an event that will affect the window, we need to write a new function.
class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        
        self.tbutton1 =QToolButton()
        self.tbutton1.setText("Click 1")
        self.tbutton1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        
        self.tbutton2 =QToolButton()
        self.tbutton2.setText("Click 2")
        self.tbutton2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        
        self.tbutton3 =QToolButton()
        self.tbutton3.setText("Click 3")
        self.tbutton3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        
        self.tbutton4 =QToolButton()
        self.tbutton4.setText("Click 4")
        self.tbutton4.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        
        self.tbutton5 =QToolButton()
        self.tbutton5.setText("Click 5")
        self.tbutton5.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        
        self.hbox.addWidget(self.tbutton1)
        self.hbox.addWidget(self.tbutton2)
        self.hbox.addWidget(self.tbutton3)
        self.hbox.addWidget(self.tbutton4)
        self.hbox.addWidget(self.tbutton5)
        
        self.resizable_button = QPushButton("Resize",self)
        self.resizable_button.move(200,50)
        self.line_succes = QLineEdit(self)
        self.line_succes.move(300,450)
        
        self.resizable_button.mousePressEvent = self.button_press
        self.resizable_button.mouseMoveEvent = self.button_resize
                
        self.resize(800,500)
        self.show()
        
    def closeEvent(self,e):
        message = QMessageBox(QMessageBox.Warning,"Exit Window","All data will be delete are you sure ?",QMessageBox.Yes | QMessageBox.No| QMessageBox.Cancel)
        message.exec()
    def button_press(self,e):
        self.first_pos = e.pos()
        self.button_size = self.resizable_button.size()
        print(e.pos())
    def button_resize(self,e):
        self.last_pos = e.pos()
        self.change = self.last_pos-self.first_pos
        self.last_size = QSize(self.button_size.width()+self.change.x(),self.button_size.height()+self.change.y())
        self.resizable_button.resize(self.last_size)
    def resizeEvent(self, e):
        if self.width()<500:
            self.hbox.setDirection(QBoxLayout.TopToBottom)
        else:
            self.hbox.setDirection(QHBoxLayout.LeftToRight)
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Enter:
            self.line_succes.setText("Succes")     
        if e.key() == Qt.Key_Escape:
            self.close()


app = QApplication([])
window = main()
app.exec()