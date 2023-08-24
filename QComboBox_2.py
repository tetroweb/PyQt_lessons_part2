from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.combo = QComboBox(self)
        self.combo.setGeometry(100,100,200,40)
        self.combo.setFont(QFont("Tahoma",18))
        
        # self.combo.setMaxCount(5)
        # self.combo.setMaxVisibleItems(2)
        
        self.combo.setEditable(True)
        self.combo.setDuplicatesEnabled(True)
        
        self.combo.addItems(["1","2","3","4","5","6","7","adana","antalya","ankara"])
        
        # i = self.combo.findText("an",Qt.MatchStartsWith)#return index 
        # print(i)
        # i = self.combo.findText("ya",Qt.MatchEndsWith)#return index 
        # print(i)
        # i = self.combo.findText("an",Qt.MatchContains)#return index 
        # print(i)
        # i = self.combo.findText("an",Qt.MatchExactly)#return index 
        # print(i)
        
        self.combo.currentIndexChanged.connect(self.change_index)
        self.combo.currentTextChanged.connect(self.change_text)
        
        self.resize(800,500)
        self.show()
        
    def change_index(self,i):
        print(i)
    
    def change_text(self,t):
        print(t) 
        
app = QApplication([])
window = main()
app.exec()