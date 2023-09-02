from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        # self.message = QMessageBox(QMessageBox.Information , "Info","This is a info message")
        # self.message.exec()
        
        self.message = QMessageBox()
        self.message.setIcon(QMessageBox.Question)
        self.message.setWindowTitle("Question")
        self.message.setText("This is an question")
        self.message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.message.exec()
        
        if self.message.clickedButton() == self.message.button(QMessageBox.Yes):
            print("Yes")
        elif self.message.clickedButton() == self.message.button(QMessageBox.No):
            print("No")
        
        self.resize(800,500)
        self.show()
        
        
        
app = QApplication([])
window = main()
app.exec()