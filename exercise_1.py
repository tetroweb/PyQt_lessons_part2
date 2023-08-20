from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#FrmaelessWindowHint
#WindowTitleHint
#WindowMinimizeButtonHint
#WindowMaximizeButtonHint
#WindowMinMaxButtonHint
#WindowStaysOnTopHint
#WindowStaysOnBottomHint

css = """
    QMenuBar{
        background-color : rgb(60,60,60);
        height : 30px;
    }
    QMenuBar::item{
        margin : 0px;
        color : rgb(191,191,191);
    }
    QMenuBar::item::selected{
        background-color : rgb(100,100,100);
    }
    QToolButton{
        background-color : transparent;
        }
    QToolButton::hover{
        background-color : rgb(100,100,100);
    }
"""



class main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.menubar = QMenuBar()
        self.menubar.addMenu("  File  ")
        self.menubar.addMenu("  Edit  ")
        self.menubar.addMenu("  Selection  ")
        self.menubar.addMenu("  View  ")
        self.menubar.addMenu("  Go  ")
        self.menubar.addMenu("  Run  ")
        self.menubar.addMenu("  Terminal  ")
        self.menubar.addMenu("  Run  ")
        self.setMenuBar(self.menubar)
        self.menubar.setStyleSheet(css)
        
        
        self.logo = QLabel()
        self.logo.setStyleSheet("padding: 6px;")
        self.pixmap = QPixmap("vs_logo.png")
        self.logo.setPixmap(self.pixmap.scaled(QSize(20,20),Qt.KeepAspectRatio))
        self.menubar.setCornerWidget(self.logo , Qt.TopLeftCorner)
        
        self.hbox = QHBoxLayout(self.menubar)
        self.hbox.setContentsMargins(self.menubar.sizeHint().width(),0,0,0)
        self.hbox.setAlignment(Qt.AlignCenter)
        
        self.title = QLabel("Title of this window")
        self.title.setStyleSheet("color : rgb(191,191,191)")
        
        self.hbox.addWidget(self.title)
        
        self.tbutton1 = QToolButton()
        self.tbutton2 = QToolButton()
        self.tbutton3 = QToolButton()

        self.tbutton1.setStyleSheet(css)
        self.tbutton2.setStyleSheet(css)
        self.tbutton3.setStyleSheet(css)

        self.tbutton1.setIcon(QIcon("minimize.png"))
        self.tbutton2.setIcon(QIcon("maximize.png"))
        self.tbutton3.setIcon(QIcon("close.png"))
        
        self.hbox.addWidget(self.tbutton1)
        self.hbox.addWidget(self.tbutton2)
        self.hbox.addWidget(self.tbutton3)

        
        
        self.resize(800,500)
        self.showMaximized()
        
app = QApplication([])
window = main()
app.exec()