from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button = QPushButton("Dialog",self)
        self.button.clicked.connect(self.dialog_open)
        
        self.resize(800,500)
        self.show()
    def dialog_open(self):
        dialog = QDialog()
        vbox = QVBoxLayout(dialog)
        label = QLabel("Is Data bank save ?")
        vbox.addWidget(label)
        button_box = QDialogButtonBox(QDialogButtonBox.Yes| QDialogButtonBox.Ok | QDialogButtonBox.No | QDialogButtonBox.Cancel | Qt.Horizontal)
        button_box.setStandardButtons(QDialogButtonBox.Yes | QDialogButtonBox.No)
        # button_box.addButton(QDialogButtonBox.Ignore)
        button_box.button(QDialogButtonBox.Yes).setText("Evet")
        button_box.accepted.connect(self.succes)#if choosee positive choice
        button_box.rejected.connect(dialog.close)#if choosee positive choice
        
        vbox.addWidget(button_box)
        dialog.exec()
    def succes(self):
        print("Data saved succes")




app = QApplication([])
window = main()
app.exec()