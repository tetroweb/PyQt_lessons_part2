from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.hbox = QHBoxLayout(self)
        self.vbox = QVBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.label = QLabel("Label 1")
        self.button  = QPushButton("Dark")
        self.button2  = QPushButton("Light")
        self.line = QLineEdit("Line 1")
        self.line2 = QLineEdit("Line 2")
        self.check = QCheckBox("Checking")
        self.radio = QRadioButton("Radio")
        self.combo = QComboBox()
        self.combo.addItems(["item 1","item 2"])
        self.text = QTextEdit("TestEdit")
        
        
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.button2)
        self.vbox.addWidget(self.line)
        self.vbox.addWidget(self.line2)
        self.vbox.addWidget(self.check)
        self.vbox.addWidget(self.radio)
        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.text)
        
        self.list = QListWidget()
        self.item = QListWidgetItem()
        self.item.setText("item")
        self.list.addItems(["Pen","Book","Eraser","Ruler"])
        self.list.setAlternatingRowColors(True)
        self.list.setToolTip("Self.list")
        self.hbox.addWidget(self.list)
        
        self.table = QTableWidget(5,5)
        self.hbox.addWidget(self.table)
        self.table.setAlternatingRowColors(True)
        
        self.button.clicked.connect(self.dark)
        self.button2.clicked.connect(self.light)
        
        self.resize(800,500)
        self.show()
    def dark(self):
        palette = QPalette()
        palette.setColor(QPalette.Background , QColor(60,60,60))
        palette.setColor(QPalette.AlternateBase , QColor("darkkhaki"))
        palette.setColor(QPalette.Base , QColor("#bbb"))
        palette.setColor(QPalette.Text , QColor(Qt.blue))
        palette.setColor(QPalette.WindowText , QColor("goldenrod"))
        palette.setColor(QPalette.ButtonText , QColor("blue"))
        palette.setColor(QPalette.HighlightedText,QColor("blue"))
        palette.setColor(QPalette.Highlight,QColor("goldenrod"))
        
        
        self.setPalette(palette)    
    
    def light(self):
        palette = QPalette()
        palette.setColor(QPalette.Background , QColor("lightskyblue"))
        palette.setColor(QPalette.AlternateBase , QColor("lightseagreen"))
        palette.setColor(QPalette.Base , QColor("#ddd"))
        palette.setColor(QPalette.Text , QColor(Qt.black))
        palette.setColor(QPalette.WindowText , QColor("green"))
        palette.setColor(QPalette.ButtonText , QColor("blue"))
        palette.setColor(QPalette.HighlightedText,QColor("red"))
        palette.setColor(QPalette.Highlight,QColor("lightseagreen"))
        
        
        self.setPalette(palette)  
    
app = QApplication([])
window = main()
app.exec()