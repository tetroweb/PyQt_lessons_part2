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
        background-color : whitesmoke;
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
        
        
        self.title = QLabel("Title of this window")
        self.title.setStyleSheet("color : rgb(191,191,191)")
        
        self.hbox.addWidget(self.title)
        
        self.hbox2 = QHBoxLayout()
        self.hbox.addLayout(self.hbox2)
        
        self.hbox3 = QHBoxLayout()
        self.hbox.addLayout(self.hbox3)
        
        
        
        self.tbutton1 = QToolButton()
        self.tbutton2 = QToolButton()
        self.tbutton3 = QToolButton()

        self.tbutton1.setStyleSheet(css)
        self.tbutton2.setStyleSheet(css)
        self.tbutton3.setStyleSheet(css)

        self.tbutton1.setIcon(QIcon("minimize.png"))
        self.tbutton2.setIcon(QIcon("maximize.png"))
        self.tbutton3.setIcon(QIcon("close.png"))
        
        self.tbutton1.setFixedHeight(self.menubar.sizeHint().height())
        self.tbutton2.setFixedHeight(self.menubar.sizeHint().height())
        self.tbutton3.setFixedHeight(self.menubar.sizeHint().height())
        
        self.tbutton1.clicked.connect(self.showMinimized)
        self.tbutton2.clicked.connect(self.showMaxNormal)
        self.tbutton3.clicked.connect(self.close)
        
        
        self.hbox3.addWidget(self.tbutton1)
        self.hbox3.addWidget(self.tbutton2)
        self.hbox3.addWidget(self.tbutton3)

        self.hbox3.setAlignment(Qt.AlignRight)
        self.hbox2.setContentsMargins(self.menubar.sizeHint().width(),0,0,0)
        self.hbox2.setAlignment(Qt.AlignCenter)
        
        
        
        self.toolbar = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea , self.toolbar)
        self.toolbar.setMinimumWidth(60)
        self.toolbar.setMovable(False)
        self.toolbar.setStyleSheet("background-color : rgb(51,51,51) ; border : none;")
        
        self.tbutton4 = QToolButton()
        self.tbutton4.setIcon(QIcon("search_logo.png"))
        self.tbutton4.setIconSize(QSize(30,30))
        self.tbutton4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolbar.addWidget(self.tbutton4)
        
        self.tbutton5 = QToolButton()
        self.tbutton5.setIcon(QIcon("search_logo.png"))
        self.tbutton5.setIconSize(QSize(30,30))
        self.tbutton5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolbar.addWidget(self.tbutton5)
        
        self.tbutton6 = QToolButton()
        self.tbutton6.setIcon(QIcon("search_logo.png"))
        self.tbutton6.setIconSize(QSize(30,30))
        self.tbutton6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        
        
        self.toolbar.setStyleSheet("""QToolBar{background-color : rgb(51,51,51) ;border: none ;}QToolButton{ padding: 5px;}""")
        
        self.widget = QWidget()
        self.widget.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Expanding)
        
        self.toolbar.addWidget(self.widget)
        self.toolbar.addWidget(self.tbutton6)
        
        self.toolbar2 = QToolBar()
        self.addToolBar(Qt.BottomToolBarArea , self.toolbar2)
        self.toolbar2.setMovable(False)
        self.toolbar2.setFixedHeight(20)
        self.toolbar2.setStyleSheet("QToolBar{background-color : rgb(0,122,204); border : none;}QToolButton{color: white; margin:0px;}QToolButton::hover{background-color : rgb(0,155,220)}")
        
        self.toolbar2.addAction("  Python  ")
        self.toolbar2.addAction("  Error 0  ")
        
        self.widget_size = QWidget()
        self.widget_size.setFixedSize(20,20)
        self.toolbar2.addWidget(self.widget_size)
        self.grip = QSizeGrip(self.widget_size)
        self.grip.move(10,7)
        
        
        self.widget = QWidget()
        self.widget.setSizePolicy(QSizePolicy.Expanding ,QSizePolicy.Expanding )
        self.toolbar2.addWidget(self.widget)
        
        self.toolbar2.addAction("  Spaces: 4  ")
        self.toolbar2.addAction("  UTF-8  ")
        
        self.resize(800,500)
        self.show()
        self.title.mousePressEvent = self.first
        self.title.mouseMoveEvent = self.last
        self.title.mouseReleaseEvent = self.reset
        
        self.title.setContextMenuPolicy(Qt.CustomContextMenu)
        self.title.customContextMenuRequested.connect(self.menu_open)
        
    def menu_open(self,p):
        menu = QMenu()
        action1 = menu.addAction("Minimize")
        action2 =menu.addAction("Maximize")
        action3 = menu.addAction("Close")
        
        action1.triggered.connect(self.showMinimized)
        action2.triggered.connect(self.showMaximized)
        action3.triggered.connect(self.close)
        menu.exec(self.title.mapToGlobal((p)))
    def showMaxNormal(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    def first(self,e):
        if e.button() == Qt.LeftButton:
            self.control = True
            self.mouse_pos = self.mapToGlobal(e.pos())
            self.window_pos = self.pos()
    def last(self,e):
            if self.control == True:
                change_pos = self.mapToGlobal(e.pos())-self.mouse_pos
                self.move(self.window_pos+change_pos)
            
    def reset(self,e):
            self.control = False
        
        
app = QApplication([])
window = main()
app.exec()