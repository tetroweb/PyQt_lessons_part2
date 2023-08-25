from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.line = QLineEdit(self)
        self.line.setGeometry(50,10,300,30)
        self.line.setFont(QFont("Tahoma",12))
        
        self.list = QListWidget(self)
        self.list.setGeometry(50,50,300,400)
        self.list.setFont(QFont("Consolas",14))
        
        self.list.addItems(["Nissan","Opel","Hundai","Honda","Mercedes","bmw","Toyota","Ford",""])
        
        self.list.item(0).setFlags(Qt.ItemIsEditable | self.list.item(0).flags())
        
        self.line.textEdited.connect(self.search)
        
        self.button = QPushButton("Click")
        self.list.setItemWidget(self.list.item(self.list.count()-1),self.button)
        
        self.resize(800,500)
        self.show()
        
    def search(self):
        search_list = self.list.findItems(self.line.text(),Qt.MatchContains)
        
        for i in range(self.list.count()):
            self.list.item(i).setHidden(False)
            
            if self.list.item(i) not in search_list :
                self.list.item(i).setHidden(True)
                
                
        
        
        
app = QApplication([])
window = main()
app.exec()