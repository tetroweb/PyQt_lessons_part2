from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.text = QTextEdit("Book Pen Ruler Note")
        self.text.setFixedWidth(400)
        self.font_dialog = QFontDialog()
        self.combo = QComboBox()
        self.combo.addItems(["green","blue","yellow"])
        self.hbox.addWidget(self.font_dialog)
        self.hbox.addWidget(self.combo)
        self.hbox.addWidget(self.text)
        
        self.font_dialog.currentFontChanged.connect(self.font_changed)
        self.combo.currentTextChanged.connect(self.color_changed)
        
        self.resize(800,500)
        self.show()
        
    def font_changed(self,f):
        self.text.setCurrentFont(f)
    
    def color_changed(self,t):
        self.text.setTextColor(QColor("%s"%t))
     
app = QApplication([])
window = main()
app.exec()