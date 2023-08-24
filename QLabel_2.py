
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel("<a href ='www.youtube.com'>Youtube</a>",self)
        self.label.setGeometry(100,100,250,200)
        self.label.setFont(QFont("Tahoma",24))
        
        # self.label.setTextInteractionFlags(Qt.TextEditable | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse | Qt.LinksAccessibleByMouse | Qt.LinksAccessibleByKeyboard )
        self.label.setTextInteractionFlags(Qt.TextEditorInteraction | Qt.TextBrowserInteraction)# 3 in 1
        self.label.setOpenExternalLinks(True)
        
        self.resize(800,500)
        self.show()
        
        
app = QApplication([])
window = main()
app.exec()