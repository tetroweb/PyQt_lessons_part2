from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        vbox = QVBoxLayout(self)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMaximumSize(500,400)
        button = QPushButton("Choose File")
        button.setFont(QFont("Consolas",16))
        button.setFixedSize(240,35)
        vbox.addWidget(self.label)
        vbox.addWidget(button)
        
        self.label.setStyleSheet("border : 5px dashed;")
        
        button.clicked.connect(self.set_pixmap)
        
        
        self.resize(500,400)
        self.show()
        
    def set_pixmap(self):
            dialog = QFileDialog.getOpenFileName(filter = "images(*.png *.jpg)")
            pix = QPixmap(dialog[0])
            self.label.setPixmap(pix)    
            if pix.width() > 500 or pix.height() >400:
                self.label.setScaledContents(True)
            else:
                self.label.setScaledContents(False)
app = QApplication([])
window = main()
app.exec()